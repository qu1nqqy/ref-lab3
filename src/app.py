from fastapi import FastAPI
from src.user import router as user_router
from src.order import router as order_router
from src.product import router as product_router

app_ = FastAPI()
app_.include_router(user_router)
app_.include_router(order_router)
app_.include_router(product_router)