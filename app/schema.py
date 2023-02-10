from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional



class user_base(BaseModel):
    email : EmailStr
    password : str

class user_update(BaseModel):
    password : str

class user_respone(BaseModel):
    id : int
    email : EmailStr
    create_at : datetime

    class Config:
        orm_mode = True


class new_post(BaseModel):
    title : str
    content : str
    published : bool = True

class update_post(BaseModel):
    title : str
    content : str
    published : bool

class post_respone(BaseModel):
    id : int
    title : str
    content : str
    published : bool
    create_at : datetime
    owner_id : int
    owner : user_respone

    class Config:
        orm_mode = True

class new_post_respone(BaseModel):
    post : post_respone
    votes : int

class token(BaseModel):
    access_token : str
    token_type : str

class token_data(BaseModel):
    id : Optional[str] = None

class vote_form(BaseModel):
    post_id : int
    dir : conint(le=1)

