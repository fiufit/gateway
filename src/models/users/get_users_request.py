from typing import Optional
from models.pagination import Pagination


class GetUsersRequest(Pagination):
    name: Optional[str]
    nickname: Optional[str]
    location: Optional[str]
    is_verified: Optional[bool]
    disabled: Optional[bool]

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            query.append(f"{param}={value}")
        return "&".join(query)
