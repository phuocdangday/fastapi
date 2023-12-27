from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

from src.config import settings

engine = create_engine(settings.DATABASE_URL)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(session_factory)

Base = declarative_base()


def get_session():
    return Session()


def init_database():
    Base.metadata.create_all(engine)
