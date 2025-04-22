from pydantic import BaseModel, Field


class SignUpResponse(BaseModel):
    msg: str = "ok"


class LoginResponse(BaseModel):
    msg: str = "welcome"
    user_id: int = Field(...)
