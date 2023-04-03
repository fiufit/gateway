from pydantic import BaseModel
from datetime import date


class RegisterRequest(BaseModel):
    email: str
    password: str

class FinishRegisterRequest(BaseModel):
    nick_name: str
    display_name: str
    is_male: bool
    birth_date: str
    height: int
    weight: int
    main_location: str
    interests: list[str]