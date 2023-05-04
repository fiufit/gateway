from pydantic import (
    BaseModel,
)
from typing import Optional


class Pagination(BaseModel):
    page: Optional[int]
    page_size: Optional[int]
