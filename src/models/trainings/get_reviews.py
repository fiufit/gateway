from typing import Optional
from models.pagination import Pagination


class GetReviewsRequest(Pagination):
    comment: Optional[str]
    user_id: Optional[str]
    min_score: Optional[int]
    max_score: Optional[int]

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            query.append(f"{param}={value}")
        return "&".join(query)
