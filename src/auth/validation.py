import firebase_admin
from firebase_admin import (
    credentials,
)
from firebase_admin import (
    auth,
)

from config import (
    FIREBASE_ADMIN,
)
import base64
import json


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
