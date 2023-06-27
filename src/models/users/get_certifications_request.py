from models.pagination import Pagination
from typing import Optional


class GetCertificationsRequest(Pagination):
    user_id: Optional[str]
    status: Optional[str]

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            query.append(f"{param}={value}")
        return "&".join(query)
