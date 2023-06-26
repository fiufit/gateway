from typing import Optional, List
from pydantic import Field
from fastapi import Query
from models.pagination import Pagination


class GetUsersRequest(Pagination):
    name: Optional[str]
    nickname: Optional[str]
    is_verified: Optional[bool]
    disabled: Optional[bool]
    tags: Optional[List[str]] = Field(Query([]))

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


class GetClosestUsersRequest(Pagination):
    distance: int

    def to_query_string(self):
        params = self.dict()
        query = []
        for param, value in params.items():
            if value is None:
                continue
            query.append(f"{param}={value}")
        return "&".join(query)
