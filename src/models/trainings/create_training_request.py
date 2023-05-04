from pydantic import (
    BaseModel,
)


class CreateExerciseRequest(BaseModel):
    title: str
    description: str


class CreateTrainingRequest(BaseModel):
    name: str
    description: str
    difficulty: str
    duration: int
    exercises: list[CreateExerciseRequest]
