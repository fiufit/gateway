from jwt_bearer import JWTBearer
from fastapi import Request


from .validation import validate_admin_token


class AdminJWTBearer(JWTBearer):
    def __init__(self):
        super(
            AdminJWTBearer,
            self,
        ).__init__()

    async def __call__(
        self,
        request: Request,
    ):
        super(
            AdminJWTBearer,
            self,
        ).__call__(request=request)

    def verify_jwt(
        self,
        jwtoken: str,
    ) -> bool:
        return validate_admin_token(jwtoken)