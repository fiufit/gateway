from pydantic import (
    BaseModel,
)
from typing import Optional


class Pagination(BaseModel):
    page: Optional[int]
    page_size: Optional[int]

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            query.append(f"{param}={value}")
        return "&".join(query)
