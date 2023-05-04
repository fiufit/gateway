from pydantic import (
    BaseModel,
)
from typing import Optional


class UpdateUserRequest(BaseModel):
    nickname: Optional[str]
    display_name: Optional[str]
    is_male: Optional[bool]
    birth_date: Optional[str]
    height: Optional[int]
    weight: Optional[int]
    main_location: Optional[str]
