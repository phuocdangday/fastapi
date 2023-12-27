from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
