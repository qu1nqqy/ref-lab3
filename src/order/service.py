from sqlalchemy.orm import Session
from src.core.models import Order
from .schemas import BuyResponse, GetOffersResponse
from src import Pagination


def buy(
        user_id: int,
        product_id: int,
        quantity: float,
        db: Session
) -> BuyResponse:
    order = Order(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity
    )
    db.add(order)
    db.commit()
    return {"msg": "bought"}


def get_orders(
        user_id: int,
        pagination: Pagination,
        db: Session
) -> GetOffersResponse:
    return (
        db.query(Order)
        .filter(Order.user_id == user_id)
        .offset(pagination.offset)
        .limit(pagination.limit)
        .all()
    )
