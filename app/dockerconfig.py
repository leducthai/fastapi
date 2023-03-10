import os

class Setting:
    def __init__(self) -> None:
        self.database_hostname = os.environ.get('DATABASE_HOSTNAME')
        self.database_port = os.environ.get('DATABASE_PORT')
        self.database_password = os.environ.get('DATABASE_PASSWORD')
        self.database_name = os.environ.get('DATABASE_NAME')
        self.database_username = os.environ.get('DATABASE_USERNAME')
        self.secret_key = os.environ.get('SECRET_KEY')
        self.algorithm = os.environ.get('ALGORITHM')
        self.access_token_expire_minutes = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')

settings = Setting()