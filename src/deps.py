from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends
from src.core.db import get_session
from pydantic import BaseModel

SessionDep = Annotated[Session, Depends(get_session)]


class Pagination(BaseModel):
    limit: int
    offset: int


PaginationDep = Annotated[Pagination, Depends(Pagination)]
