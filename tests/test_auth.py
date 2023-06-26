import src.auth.validation as validation
import jwt
from unittest.mock import patch


def test_decode_base64_to_dict():
    base64_string = "eyJ1c2VybmFtZSI6ImFkbWluIn0="
    decoded = validation.decode_base64_to_dict(base64_string)
    assert decoded == {"username": "admin"}


@patch("src.auth.validation.firebase_admin.initialize_app")
def test_initialize_firebase_app(mock_initialize_app):
    validation.initialize_firebase_app()
    mock_initialize_app.return_value = None
    mock_initialize_app.assert_called_once()


@patch("src.auth.validation.auth.verify_id_token")
def test_validate_firebase_token(mock_verify_token):
    mock_verify_token.return_value = {"email_verified": True}
    validation.validate_firebase_token("token")
    mock_verify_token.assert_called_once_with("token", check_revoked=True)


@patch("src.auth.validation.auth.verify_id_token")
def test_validate_invalid_firebase_token(mock_verify_token):
    mock_verify_token.side_effect = Exception
    validation.validate_firebase_token("token")
    mock_verify_token.assert_called_once_with("token", check_revoked=True)


@patch("src.auth.validation.auth.verify_id_token")
def test_validate_not_verified_mail(mock_verify_token):
    mock_verify_token.return_value = {"email_verified": False}
    try:
        validation.validate_firebase_token("token")
    except Exception as e:
        assert e.status_code == 401
        assert e.error_code == "G4"
        assert e.description == "User does not have a verified email"


@patch("src.auth.validation.jwt.decode")
@patch("src.auth.validation.base64.b64decode")
def test_validate_admin_token(mock_b64decode, mock_decode):
    mock_b64decode.return_value = bytes("public_key_bytes", "utf-8")
    mock_decode.return_value = {"username": "admin"}
    token = validation.validate_admin_token("token")
    mock_b64decode.assert_called_once_with(validation.USERS_JWT_KEY)
    mock_decode.assert_called_once_with(
        "token", "public_key_bytes", algorithms=["RS256"], options={"verify_exp": True}
    )
    assert token == {"username": "admin"}


@patch("src.auth.validation.jwt.decode")
@patch("src.auth.validation.base64.b64decode")
def test_validate_invalid_admin_token(mock_b64decode, mock_decode):
    mock_b64decode.return_value = bytes("public_key_bytes", "utf-8")
    mock_decode.side_effect = jwt.exceptions.InvalidTokenError
    token = validation.validate_admin_token("token")
    mock_b64decode.assert_called_once_with(validation.USERS_JWT_KEY)
    mock_decode.assert_called_once_with(
        "token", "public_key_bytes", algorithms=["RS256"], options={"verify_exp": True}
    )
    assert token is None


@patch("src.auth.validation.validate_firebase_token")
@patch("src.auth.validation.validate_admin_token")
def test_validate_token_user_token(
    mock_validate_admin_token, mock_validate_firebase_token
):
    mock_validate_admin_token.return_value = None
    mock_validate_firebase_token.return_value = {"uid": "uid"}
    token = validation.validate_token("token")
    mock_validate_admin_token.assert_called_once_with("token")
    mock_validate_firebase_token.assert_called_once_with("token")
    assert token == {"uid": "uid"}


@patch("src.auth.validation.validate_admin_token")
def test_validate_token_admin_token(mock_validate_admin_token):
    mock_validate_admin_token.return_value = {"username": "admin"}
    token = validation.validate_token("token")
    mock_validate_admin_token.assert_called_once_with("token")
    assert token == {"username": "admin"}


def test_validate_deleter_admin():
    usr_to_validate = {"username": "admin", "is_admin": True}
    usr_to_delete = "uid"
    validation.validate_deleter(usr_to_validate, usr_to_delete)


def test_validate_delete_same_user():
    usr_to_validate = {"username": "pepe", "uid": "user"}
    usr_to_delete = "user"
    validation.validate_deleter(usr_to_validate, usr_to_delete)


def test_validate_delete_other_user():
    usr_to_validate = {"username": "pepe", "uid": "user"}
    usr_to_delete = "other_user"
    try:
        validation.validate_deleter(usr_to_validate, usr_to_delete)
    except Exception as e:
        assert e.status_code == 401
        assert e.error_code == "G3"
        assert e.description == "User cannot delete another user"


def test_validate_delete_no_uid_or_is_admin():
    usr_to_validate = {"username": "pepe"}
    usr_to_delete = "other_user"
    try:
        validation.validate_deleter(usr_to_validate, usr_to_delete)
    except Exception as e:
        assert e.status_code == 401
        assert e.error_code == "G3"
        assert e.description == "Could not validate the deleter"
