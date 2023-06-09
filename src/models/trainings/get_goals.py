from typing import Optional
from models.pagination import Pagination


class GetGoalsRequest(Pagination):
    type: Optional[str]
    subtype: Optional[str]
    deadline: Optional[str]

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            query.append(f"{param}={value}")
        return "&".join(query)
