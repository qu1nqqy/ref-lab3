from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .schemas import BuyResponse, GetOffersResponse
from . import service
from src import SessionDep, PaginationDep, Pagination

router = APIRouter(tags=["order"])


@router.post("/buy", response_model=BuyResponse)
def buy(
        user_id: int,
        product_id: int,
        quantity: int,
        db: Session = Depends(SessionDep)
):
    return service.buy(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity,
        db=db
    )


@router.get("/orders", response_model=List[GetOffersResponse])
def get_orders(
        user_id: int,
        pagination: Pagination = Depends(PaginationDep),
        db: Session = Depends(SessionDep)
):
    return service.get_orders(
        user_id=user_id,
        pagination=pagination,
        db=db
    )
