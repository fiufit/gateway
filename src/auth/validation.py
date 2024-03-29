import firebase_admin
from firebase_admin import (
    credentials,
)
from firebase_admin import (
    auth,
)

from config import FIREBASE_ADMIN, USERS_JWT_KEY
import base64
import json
import jwt
from errors import CustomException, ERR_NOT_AUTHORIZED, ERR_EMAIL_NOT_VERIFIED


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


def validate_firebase_token(
    token: str,
):
    try:
        user = auth.verify_id_token(
            token,
            check_revoked=True,
        )
    except Exception:
        return None
    if user["email_verified"] is False:
        raise CustomException(
            status_code=401,
            error_code=ERR_EMAIL_NOT_VERIFIED,
            description="User does not have a verified email",
        )
    return user


def validate_admin_token(
    token: str,
):
    public_key_bytes = base64.b64decode(USERS_JWT_KEY)
    public_key_str = public_key_bytes.decode("utf-8")
    try:
        decoded_token = jwt.decode(
            token, public_key_str, algorithms=["RS256"], options={"verify_exp": True}
        )
        return decoded_token
    except jwt.exceptions.InvalidTokenError:
        return None


def validate_token(
    token: str,
):
    admin = validate_admin_token(token)
    if admin is not None:
        return admin
    user = validate_firebase_token(token)
    return user


def validate_deleter(
    usr_to_validate: dict,
    usr_to_delete: str,
):
    if "is_admin" in usr_to_validate.keys():
        if usr_to_validate["is_admin"]:
            return
        raise CustomException(
            status_code=401,
            error_code=ERR_NOT_AUTHORIZED,
            description="User is not an admin",
        )
    if "uid" in usr_to_validate.keys():
        if usr_to_validate["uid"] == usr_to_delete:
            return
        raise CustomException(
            status_code=401,
            error_code=ERR_NOT_AUTHORIZED,
            description="User cannot delete another user",
        )
    raise CustomException(
        status_code=401,
        error_code=ERR_NOT_AUTHORIZED,
        description="Could not validate the deleter",
    )
