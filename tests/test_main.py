from fastapi.testclient import TestClient
from unittest.mock import patch

import src.main
import src.auth.jwt_bearer

client = TestClient(src.main.app)

"""
Recordatorio:
Hay que tener cuidado con el path que se le pasa a patch
En este caso queremos mockear make_request, pero para eso hay que
hacer patch desde el modulo que estas testeando hasta la función
O sea, hacer:
patch(src.request.make_request) NO funciona
patch(src.routers.users.make_request) NO funciona
Hay que seguir la linea de los imports:
En main: from routers import users
En users: from request import make_request
Entonces el patch queda:
src -> main -> users -> make_request
"""


@patch("src.main.users.make_request")
def test_successful_register(mock_make_request):
    mock_make_request.return_value = {"success": True}
    response = client.post(
        "/v1/users/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"success": True}


def test_incorrect_email_format_in_body_register():
    response = client.post(
        "/v1/users/register",
        json={"e-mail": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 400
    response_body = response.json()
    assert response_body["error"]["code"] == "G1"
    assert (
        response_body["error"]["description"]
        == "Request validation error - ('body', 'email'): field required"
    )


def test_incorrect_password_format_in_body_register():
    response = client.post(
        "/v1/users/register", json={"email": "test@example.com", "pw": "testpassword"}
    )
    assert response.status_code == 400
    response_body = response.json()
    assert response_body["error"]["code"] == "G1"
    assert (
        response_body["error"]["description"]
        == "Request validation error - ('body', 'password'): field required"
    )


def test_incorrect_email_and_password_format_in_body_register():
    response = client.post(
        "/v1/users/register", json={"e-mail": "test@example.com", "pw": "testpassword"}
    )
    assert response.status_code == 400
    response_body = response.json()
    assert response_body["error"]["code"] == "G1"
    error_description = response_body["error"]["description"]
    assert "('body', 'email'): field required" in error_description
    assert "('body', 'password'): field required" in error_description


def test_finish_register_without_authorization_header():
    headers = {"NotAuth": "Bearer fake_token"}
    response = client.post(
        "/v1/users/finish-register", json={"name": "Test User"}, headers=headers
    )
    assert response.status_code == 401
    response_body = response.json()
    assert response_body["error"]["code"] == "G1"
    assert response_body["error"]["description"] == "Authorization header is missing"


def test_finish_register_without_bearer_keyword_in_header():
    headers = {"Authorization": "fake_token"}
    response = client.post(
        "/v1/users/finish-register", json={"name": "Test User"}, headers=headers
    )
    assert response.status_code == 401
    response_body = response.json()
    assert response_body["error"]["code"] == "G1"
    assert response_body["error"]["description"] == "Invalid authentication scheme"


def test_finish_register_with_other_keyword_in_header():
    headers = {"Authorization": "NotBearer fake_token"}
    response = client.post(
        "/v1/users/finish-register", json={"name": "Test User"}, headers=headers
    )
    assert response.status_code == 401
    response_body = response.json()
    assert response_body["error"]["code"] == "G1"
    assert response_body["error"]["description"] == "Invalid authentication scheme"


@patch("src.main.users.make_request")
@patch("src.main.users.JWTBearer.__call__")
def test_successful_finish_register(mock_bearer_class, mock_make_request):
    mock_make_request.return_value = {"success": True}
    mock_bearer_class.return_value = {
        "name": "Lionel Messi",
        "uid": "fake_uid",
        "email_verified": True,
    }
    headers = {"Authorization": "Bearer fake_token"}
    body = {
        "nick_name": "LioMessi",
        "display_name": "Lionel Messi",
        "is_male": True,
        "birth_date": "18/12/2022",
        "height": 169,
        "weight": 67,
        "main_location": "Qatar",
        "interests": [
            "fubol",
            "futbol",
            "la pelota",
            "la del mundo",
        ],
    }
    response = client.post("/v1/users/finish-register", json=body, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"success": True}
