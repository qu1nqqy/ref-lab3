from sqlalchemy.orm import Session
from src.core.models import Product
from .schemas import AddProductResponse, GetProductResponse
from src import Pagination


def get_product(
        pagination: Pagination,
        db: Session
) -> GetProductResponse:
    return (
        db.query(Product)
        .offset(pagination.offset)
        .limit(pagination.limit)
        .all()
    )


def add_product(
        name: str,
        description: str,
        cost: float,
        db: Session
) -> AddProductResponse:
    product = Product(
        name=name,
        description=description,
        cost=cost)
    db.add(product)
    db.commit()
    return {"msg": "added"}
