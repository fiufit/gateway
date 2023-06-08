from pydantic import (
    BaseModel,
)
from typing import Optional


class CreateMetricRequest(BaseModel):
    type: str
    subtype: Optional[str]
