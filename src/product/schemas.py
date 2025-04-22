from pydantic import BaseModel


class GetProductResponse(BaseModel):
    id: int
    name: str
    description: str
    cost: float


class AddProductResponse(BaseModel):
    msg: str = "added"
