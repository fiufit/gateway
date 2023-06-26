from typing import Optional, List
from models.pagination import Pagination
from pydantic import Field
from fastapi import Query


class GetTrainingsRequest(Pagination):
    name: Optional[str]
    description: Optional[str]
    difficulty: Optional[str]
    trainer_id: Optional[str]
    user_id: Optional[str]
    tags: Optional[List[str]] = Field(Query([]))
    min_duration: Optional[int]
    max_duration: Optional[int]
    disabled: Optional[bool]

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            if isinstance(value, list):
                for list_value in value:
                    query.append(f"{param}[]={list_value}")
            else:
                query.append(f"{param}={value}")
        return "&".join(query)
