from sqlalchemy import Column, Integer, String
from src.core.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    hashed_password = Column(String)
