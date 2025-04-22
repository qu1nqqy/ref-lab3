from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from . import service
from .schemas import AddProductResponse, GetProductResponse
from src import SessionDep, PaginationDep, Pagination

router = APIRouter(tags=["product"])


@router.get("/prods", response_model=List[GetProductResponse])
def get_product(
        pagination: Pagination = Depends(PaginationDep),
        db: Session = Depends(SessionDep)
):
    return service.get_product(
        pagination=pagination,
        db=db
    )


@router.post("/add", response_model=AddProductResponse)
def add_product(
        name: str,
        description: str,
        cost: float,
        db: Session = Depends(SessionDep)
):
    return service.add_product(
        name=name,
        description=description,
        cost=cost,
        db=db
    )
