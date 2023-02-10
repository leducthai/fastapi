
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException, status, Depends , APIRouter
from .. import models , schema , utils
from ..database import get_db

router = APIRouter(
    tags = ['users']
)

@router.get("/users" , response_model=List[schema.user_respone])
def get_all_users(db: Session = Depends(get_db)):

    users = db.query(models.user).all()
    return users

@router.post('/users', status_code=status.HTTP_201_CREATED , response_model=schema.user_respone )
def create_user(user: schema.user_base , db: Session = Depends(get_db)):

    user.password = utils.hash_pw(user.password)
    new_user = models.user(**user.dict())
    cur_email = user.email
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , 
                            detail= f'user with email {cur_email} already existed !')

@router.get('/users/{id}' , response_model= schema.user_respone)
def get_one_user(id : int , db: Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f'post with id: {id} is not found')
    return user

@router.post('/tsssss')
def root(user_credential: schema.user_base):
    user = user_credential.dict()
    return {"message": user}