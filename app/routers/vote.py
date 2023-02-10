from fastapi import HTTPException, status, Depends , APIRouter, Response
from .. import models , schema , oauth2
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ['votes']
)

@router.post('/vote', status_code=status.HTTP_201_CREATED )
def voting(vote : schema.vote_form , db : Session = Depends(get_db) , cur_user : int = Depends(oauth2.get_curent_user)):

    check_post = db.query(models.post).filter(models.post.id == vote.post_id).first()

    if not check_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post id {vote.post_id} does not exist !")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == cur_user.id)
    get_post = vote_query.first()
    if vote.dir == 1:
        if not get_post :
            new_vote = models.Vote(post_id= vote.post_id, user_id= cur_user.id)
            db.add(new_vote)
            db.commit()

            return {"message" : "successfully add vote !"}

        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail= f"user with id {cur_user.id} have already voted for post with id{vote.post_id}")

    else:
        if not get_post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"user id {cur_user.id} haven't voted for post id {vote.post_id}")
        
        vote_query.delete( synchronize_session= False)
        db.commit()

        return {"message" : "successfully delete vote !"}
        