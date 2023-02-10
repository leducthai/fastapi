from sqlalchemy import TIMESTAMP, Column , Integer , String , Boolean, text , ForeignKey
from .database import base
from sqlalchemy.orm import relationship

class post(base):
    __tablename__ = 'posts1'

    id = Column(Integer , primary_key= True , nullable= False)
    title = Column(String , nullable= False)
    content = Column(String , nullable= False)
    published = Column(Boolean , server_default= 'TRUE', nullable= False)
    create_at = Column(TIMESTAMP(timezone=True) , nullable= False , server_default= text('now()'))
    owner_id = Column(Integer , ForeignKey('users.id' , ondelete='CASCADE') , nullable= False)

    owner = relationship('user')

class user(base):
    __tablename__ = 'users'

    id = Column(Integer , primary_key= True , nullable= False)
    email = Column(String , nullable = False , unique= True)
    password = Column(String , nullable= False )
    create_at = Column(TIMESTAMP(timezone=True) , nullable= False , server_default= text('now()'))

class Vote(base):
    __tablename__ = 'vote'
    
    post_id = Column(Integer , ForeignKey('posts1.id' , ondelete='CASCADE') , primary_key= True)
    user_id = Column(Integer , ForeignKey('users.id' , ondelete='CASCADE') , primary_key= True)