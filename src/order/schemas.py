from pydantic import BaseModel


class BuyResponse(BaseModel):
    msg: str = "bought"


class GetOffersResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
