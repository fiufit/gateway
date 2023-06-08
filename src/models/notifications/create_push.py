from pydantic import (
    BaseModel,
)
from typing import List, Dict, Any


class CreateNotificationRequest(BaseModel):
    to_user_id: List[str]
    title: str
    subtitle: str
    body: str
    sound: str
    data: Dict[str, Any]
