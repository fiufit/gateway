from pydantic import (
    BaseModel,
)
from typing import Optional


class UpdateTrainingRequest(BaseModel):
    name: Optional[str]
    description: Optional[str]
    difficulty: Optional[str]
    duration: Optional[int]
