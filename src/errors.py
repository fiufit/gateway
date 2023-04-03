from fastapi import (
    HTTPException,
)
from fastapi.responses import (
    JSONResponse,
)

ERR_INTERNAL = "G0"
ERR_BAD_REQUEST = "G1"
ERR_AUTHORIZATION = "G2"


class CustomException(HTTPException):
    def __init__(
        self,
        status_code: int,
        error_code: str,
        description: str,
    ):
        self.status_code = status_code
        self.error_code = error_code
        self.description = description

    def create_json_response(
        self,
    ):
        return JSONResponse(
            status_code=self.status_code,
            content={
                "error": {
                    "code": self.error_code,
                    "description": self.description,
                }
            },
        )
