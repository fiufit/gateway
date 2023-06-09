from pydantic import BaseModel

from typing import Optional


class UpdateGoalRequest(BaseModel):
    title: Optional[str]
    value: Optional[int]
    deadline: Optional[str]
