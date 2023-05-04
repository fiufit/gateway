from typing import Optional
from models.pagination import Pagination


class GetTrainingsRequest(Pagination):
    name: Optional[str]
    description: Optional[str]
    difficulty: Optional[str]
    trainer_id: Optional[str]
    min_duration: Optional[int]
    max_duration: Optional[int]

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            query.append(f"{param}={value}")
        return "&".join(query)
