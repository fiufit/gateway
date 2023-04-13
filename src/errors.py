from fastapi import (
    HTTPException,
)
from fastapi.responses import (
    JSONResponse,
)

ERR_INTERNAL = "G0"
ERR_BAD_REQUEST = "G1"
ERR_BAD_AUTH_TOKEN = "G2"
ERR_NOT_AUTHORIZED = "G3"
ERR_EMAIL_NOT_VERIFIED = "G4"


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


"""
Handler for exceptions raised due to validations errors in the request
"""


def handle_validation_error(_, exc) -> JSONResponse:
    error_messages = []
    for error in exc.errors():
        field_name = error["loc"]
        error_messages.append(f"{field_name}: {error['msg']}")
    message = ", ".join(error_messages)
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": ERR_BAD_REQUEST,
                "description": f"Request validation error - {message}",
            }
        },
    )


def handle_custom_exception(_, exc) -> JSONResponse:
    return exc.create_json_response()
