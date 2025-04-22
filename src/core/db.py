from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import User, Order, Product
from .base import Base

engine = create_engine("sqlite:///shop.db", connect_args={"check_same_thread": False})
new_session = sessionmaker(bind=engine)


def get_session():
    with new_session() as session:
        yield session


Base.metadata.create_all(bind=engine)
