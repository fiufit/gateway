import firebase_admin
from firebase_admin import (
    credentials,
)
from firebase_admin import (
    auth,
)
from fastapi.security import (
    HTTPBearer,
)
from config import (
    FIREBASE_ADMIN,
)
import base64
import json

from fastapi import (
    Request,
)
from errors import (
    CustomException,
    ERR_BAD_REQUEST,
    ERR_AUTHORIZATION,
)


def decode_base64_to_dict(
    base64_string,
):
    decoded_bytes = base64.b64decode(base64_string)
    decoded_str = decoded_bytes.decode("utf-8")
    decoded_json = json.loads(decoded_str)

    return decoded_json


def initialize_firebase_app():
    certificate = decode_base64_to_dict(FIREBASE_ADMIN)
    cred = credentials.Certificate(certificate)
    firebase_admin.initialize_app(cred)


def validate_token(
    token: str,
):
    try:
        decoded_token = auth.verify_id_token(
            token,
            check_revoked=True,
        )
        return decoded_token
    except Exception:
        return None


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
