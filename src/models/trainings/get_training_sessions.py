from typing import Optional
from models.pagination import Pagination


class GetTrainingSessionsRequest(Pagination):
    training_id: Optional[int]

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            query.append(f"{param}={value}")
        return "&".join(query)
