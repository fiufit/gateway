from pydantic import (
    BaseModel,
)


class UpdateNotificationRequest(BaseModel):
    read: bool
