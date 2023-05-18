from pydantic import (
    BaseModel,
)


class CreateReviewRequest(BaseModel):
    score: int
    comment: str
