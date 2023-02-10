from fastapi import HTTPException, status, Depends ,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models , schema , utils, oauth2

router = APIRouter(
    tags = ['auther']
)

@router.post('/login' , response_model= schema.token)
def login(user_credential : schema.user_base, db: Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.email == user_credential.email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail= 'invalid !')
    
    if not utils.validation(user_credential.password , user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail= 'invalid !')

    
    access_token = oauth2.authenticate_user({"user_id" : user.id })

    return {"access_token" : access_token , "token_type" : "bearer"}

