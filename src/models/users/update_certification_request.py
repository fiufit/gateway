from pydantic import (
    BaseModel,
)


class UpdateCertificationRequest(BaseModel):
    status: str

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            query.append(f"{param}={value}")
        return "&".join(query)
