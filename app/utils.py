from passlib.context import CryptContext

hash_func = CryptContext(schemes= 'bcrypt' , deprecated= 'auto')

def hash_pw(password : str):
    return hash_func.hash(password)

def validation(raw_password , hashed_password):
    return hash_func.verify(raw_password , hashed_password)