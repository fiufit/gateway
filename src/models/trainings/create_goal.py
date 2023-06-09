from pydantic import BaseModel

from typing import Optional


class CreateGoalRequest(BaseModel):
    title: str
    type: str
    subtype: Optional[str]
    value: int
    deadline: str
