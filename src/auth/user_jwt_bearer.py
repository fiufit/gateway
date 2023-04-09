from jwt_bearer import JWTBearer
from fastapi import Request


from .validation import validate_firebase_token


class UserJWTBearer(JWTBearer):
    def __init__(self):
        super(
            UserJWTBearer,
            self,
        ).__init__()

    async def __call__(
        self,
        request: Request,
    ):
        super(
            UserJWTBearer,
            self,
        ).__call__(request=request)

    def verify_jwt(
        self,
        jwtoken: str,
    ) -> bool:
        return validate_firebase_token(jwtoken)
