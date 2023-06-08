from pydantic import (
    BaseModel,
)


class RegisterRequest(BaseModel):
    email: str
    password: str


class FinishRegisterRequest(BaseModel):
    nickname: str
    display_name: str
    is_male: bool
    birth_date: str
    height: int
    weight: int
    latitude: float
    longitude: float
    interests: list[str]
    method: str
