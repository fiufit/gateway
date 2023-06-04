from pydantic import BaseModel


class UpdateExerciseSessionRequest(BaseModel):
    id: int
    done: bool


class UpdateTrainingSessionRequest(BaseModel):
    done: bool
    step_count: int
    seconds_count: int
    exercise_sessions: list[UpdateExerciseSessionRequest]
