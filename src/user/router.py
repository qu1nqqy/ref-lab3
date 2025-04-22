from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import service
from .schemas import SignUpResponse, LoginResponse
from src import SessionDep

router = APIRouter(tags=["user"])


@router.post("/signup", response_model=SignUpResponse)
def signup(
        phone: str,
        password: str,
        db: Session = Depends(SessionDep)
):
    return service.signup(
        phone=phone,
        password=password,
        db=db
    )


@router.post("/login", response_model=LoginResponse)
def login(
        db: Session = Depends(SessionDep),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    return service.login(
        db=db,
        form_data=form_data
    )
