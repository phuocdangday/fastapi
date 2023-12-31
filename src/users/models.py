from sqlalchemy import Column, Text, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(Text, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    name = Column(Text)
    created_at = Column(
        DateTime(timezone=True),
        default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now()
    )

    todos = relationship('Todo', back_populates='user')
