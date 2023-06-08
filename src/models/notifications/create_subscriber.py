from pydantic import (
    BaseModel,
)


class CreateSubscriberRequest(BaseModel):
    device_token: str
