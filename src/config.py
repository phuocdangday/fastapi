import os
from dotenv import load_dotenv

load_dotenv()


class Settings():
    DATABASE_URL = os.getenv('DATABASE_URL') or ''

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or '09d25e094faa6ca2556c818'
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM') or 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')) or 30


settings = Settings()
