from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2 
from psycopg2.extras import RealDictCursor
from time import sleep
from .dockerconfig import settings

                            #'postgresql://<user>:<password>@<ip address or host name>:port/<database>'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionlocal = sessionmaker(autocommit=False , autoflush=False, bind=engine )

base = declarative_base()

# Dependency
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost' , database='fastapi' , user='postgres' , password= 'thai1234', cursor_factory=RealDictCursor)
#         cur = conn.cursor()
#         print('database connection success !')
#         break
#     except Exception as erro:
#         print('Connecting to database failed !')
#         print('Error :', erro)
#         sleep(2)