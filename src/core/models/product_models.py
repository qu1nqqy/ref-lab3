from sqlalchemy import Column, Integer, String, Float
from src.core.base import Base


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    cost = Column(Float)
