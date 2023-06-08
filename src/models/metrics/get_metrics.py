from pydantic import BaseModel
from typing import Optional


class GetMetricsRequest(BaseModel):
    type: str
    subtype: Optional[str]
    fromDate: Optional[str]
    to: Optional[str]

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            if param == "fromDate":
                query.append(f"from={value}")
            else:
                query.append(f"{param}={value}")
        return "&".join(query)
