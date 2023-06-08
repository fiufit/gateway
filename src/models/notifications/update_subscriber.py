from pydantic import (
    BaseModel,
)


class UpdateSubscriberRequest(BaseModel):
    device_token: str
    subscribed: bool
