from typing import Optional
from pydantic import BaseModel


class GetNotificationsRequest(BaseModel):
    read: Optional[bool]
    limit: Optional[int]
    next_cursor: Optional[str]

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            query.append(f"{param}={str(value).lower()}")
        return "&".join(query)
