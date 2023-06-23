from pydantic import (
    BaseModel,
)


class SendVerificationPinRequest(BaseModel):
    phone_number: str
