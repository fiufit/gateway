from pydantic import (
    BaseModel,
)
from typing import Optional


class CreateExerciseRequest(BaseModel):
    title: str
    description: str


class CreateTrainingRequest(BaseModel):
    name: str
    description: str
    difficulty: str
    duration: int
    exercises: list[CreateExerciseRequest]
    tags: Optional[list[str]]
