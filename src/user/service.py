from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from sqlalchemy.orm import Session
from src.core.models import User
from .schemas import LoginResponse, SignUpResponse


def signup(
        phone: str,
        password: str,
        db: Session
) -> SignUpResponse:
    user = (
        db.query(User)
        .filter(User.phone == phone)
        .first()
    )
    if user:
        raise HTTPException(status_code=400, detail="already")
    user = User(
        phone=phone,
        hashed_password=bcrypt.hash(password)
    )
    db.add(user)
    db.commit()
    return SignUpResponse


def login(
        db: Session,
        form_data:
        OAuth2PasswordRequestForm
) -> LoginResponse:
    user = (
        db.query(User)
        .filter(User.phone == form_data.username)
        .first()
    )
    if not user or not bcrypt.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="bad")
    return LoginResponse(user_id=user.id)
