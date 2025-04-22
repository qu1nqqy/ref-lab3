from sqlalchemy import Column, Integer, ForeignKey
from src.core.base import Base


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer)
