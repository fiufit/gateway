from fastapi.security import (
    HTTPBearer,
)

from fastapi import (
    Request,
)

from errors import (
    CustomException,
    ERR_BAD_REQUEST,
    ERR_AUTHORIZATION,
)

from .validation import validate_token


class JWTBearer(HTTPBearer):
    def __init__(self):
        super(
            JWTBearer,
            self,
        ).__init__()

    async def __call__(
        self,
        request: Request,
    ):
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            raise CustomException(
                status_code=401,
                error_code=ERR_BAD_REQUEST,
                description="Authorization header is missing",
            )
        try:
            (
                scheme,
                token,
            ) = authorization.split()
        except Exception:
            raise CustomException(
                status_code=401,
                error_code=ERR_BAD_REQUEST,
                description="Invalid authentication scheme",
            )
        if not scheme.lower() == "bearer":
            raise CustomException(
                status_code=401,
                error_code=ERR_BAD_REQUEST,
                description="Invalid authentication scheme",
            )
        user = self.verify_jwt(token)
        if not user:
            raise CustomException(
                status_code=401,
                error_code=ERR_AUTHORIZATION,
                description="Invalid authorization token",
            )
        return user

    def verify_jwt(
        self,
        jwtoken: str,
    ) -> bool:
        return validate_token(jwtoken)
