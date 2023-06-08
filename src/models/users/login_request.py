from pydantic import BaseModel


class NotifyLoginRequest(BaseModel):
    method: str
