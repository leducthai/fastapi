
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import HTTPException, status, Depends , APIRouter, Response
from .. import models , schema , oauth2
from ..database import get_db

router = APIRouter(
    tags = ['posts']
)



@router.get("/posts" , response_model=List[schema.new_post_respone])
def get_post(db: Session = Depends(get_db), cur_user :int = Depends(oauth2.get_curent_user),
limit: int = 10, skip : int =0 , search : Optional[str] = ""):
    # cur.execute(""" SELECT * FROM posts """)
    # posts = cur.fetchall()
    #posts = db.query(models.post).filter(models.post.published == True or models.post.owner_id == cur_user.id).all()
    #posts = db.query(models.post).filter(models.post.title.contains(search)).limit(limit).offset(skip).all()

    result = db.query(models.post , func.count(models.Vote.post_id).label('votes')).join(models.Vote, models.post.id == models.Vote.post_id , isouter=True).group_by(models.post.id).filter(models.post.title.contains(search)).limit(limit).offset(skip).all()
    #print(result)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='no post')
    return result

@router.post('/posts', status_code=status.HTTP_201_CREATED , response_model= schema.post_respone)
def create_post(post: schema.new_post , db: Session = Depends(get_db) , cur_user :int = Depends(oauth2.get_curent_user)):
    # cur.execute("""INSERT INTO posts (title , content , published) VALUES (%s , %s , %s) returning * """ , 
    #             (post.title , post.content , post.published))
    # new_p = cur.fetchone()
    # conn.commit()

    new_post = post.dict()
    new_post.update({'owner_id' : cur_user.id})
    new_p = models.post(**new_post) # ** transform ':' to '='
    db.add(new_p)
    db.commit()
    db.refresh(new_p)

    return new_p

@router.get('/posts/{id}' , response_model= schema.new_post_respone)
def get_post(id : int , db: Session = Depends(get_db), cur_user: int = Depends(oauth2.get_curent_user)):
    # cur.execute(""" SELECT * FROM posts WHERE id = %s """ , (str(id)))
    # post = cur.fetchone()
    
    post = db.query(models.post , func.count(models.Vote.post_id).label('votes')).join(models.Vote, models.post.id == models.Vote.post_id , isouter=True).group_by(models.post.id).filter(models.post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
                            detail= f'post with id: {id} is not found')

    if post.post.owner_id != cur_user.id:
        if post.post.published ==False:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="you're not allow to see this post!")

    return post


@router.delete('/posts/delete/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id : int , db: Session = Depends(get_db), cur_user :int = Depends(oauth2.get_curent_user)):
    # cur.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """ , (str(id)))
    # deleted_post = cur.fetchone()

    # conn.commit()
    deleted_post = db.query(models.post).filter(models.post.id == id)
    print(deleted_post)
    if not deleted_post.first() :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
                            detail= f'post with id: {id} is not found')
                            
    if deleted_post.first().owner_id != cur_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , 
                            detail= "you're not allow to do this task!")

    deleted_post.delete( synchronize_session= False )
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/posts/{id}' , response_model= schema.post_respone)
def update_post(id : int, post: schema.update_post , db: Session = Depends(get_db), cur_user :int = Depends(oauth2.get_curent_user)):
    # cur.execute(""" UPDATE posts SET title = %s , content = %s , published = %s WHERE id = %s RETURNING * """ ,
    #             (post.title , post.content , post.published , str(id)))
    # u_post = cur.fetchone()
    # conn.commit()
    u_post = db.query(models.post).filter(models.post.id == id)

    if u_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
                            detail= f'post with id: {id} is not found')

    if u_post.first().owner_id != cur_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , 
                            detail= "you're not allow to do this task!")

    u_post.update(post.dict() , synchronize_session=False)
    db.commit()

    return u_post.first()