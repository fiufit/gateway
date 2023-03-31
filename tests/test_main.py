from fastapi.testclient import TestClient
from unittest.mock import patch

import src.main as main

client = TestClient(main.app)

@patch("src.main.make_request") # OJO en el patch hay que usar el path entero
def test_successful_register(mock_make_request):
    mock_make_request.return_value = {"success": True}
    response = client.post("/users/register", json={"email": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json() == {"success": True}



def test_incorrect_email_format_in_body_register():
    response = client.post("/users/register", json={"e-mail": "test@example.com", "password": "testpassword"})
    assert response.status_code == 400
    response_body = response.json()
    assert response_body['error']['code'] == 'CODIGO_LOCO'
    assert response_body['error']['description'] == "Request validation error - ('body', 'email'): field required"



def test_incorrect_password_format_in_body_register():
    response = client.post("/users/register", json={"email": "test@example.com", "pw": "testpassword"})
    assert response.status_code == 400
    response_body = response.json()
    assert response_body['error']['code'] == 'CODIGO_LOCO'
    assert response_body['error']['description'] == "Request validation error - ('body', 'password'): field required"



def test_incorrect_email_and_password_format_in_body_register():
    response = client.post("/users/register", json={"e-mail": "test@example.com", "pw": "testpassword"})
    assert response.status_code == 400
    response_body = response.json()
    assert response_body['error']['code'] == 'CODIGO_LOCO'
    assert response_body['error']['description'] == "Request validation error - ('body', 'email'): field required, ('body', 'password'): field required"



def test_finish_register_without_authorization_header():
    headers = {"NotAuth": "Bearer fake_token"}
    response = client.post("/users/finish_register", json={"name": "Test User"}, headers=headers)
    assert response.status_code == 401
    response_body = response.json()
    assert response_body['error']['code'] == 'CODIGO_LOCO'
    assert response_body['error']['description'] == "Authorization header is missing"



def test_finish_register_without_bearer_keyword_in_header():
    headers = {"Authorization": "fake_token"}
    response = client.post("/users/finish_register", json={"name": "Test User"}, headers=headers)
    assert response.status_code == 401
    response_body = response.json()
    assert response_body['error']['code'] == 'CODIGO_LOCO'
    assert response_body['error']['description'] == "Invalid authentication scheme"



def test_finish_register_with_other_keyword_in_header():
    headers = {"Authorization": "NotBearer fake_token"}
    response = client.post("/users/finish_register", json={"name": "Test User"}, headers=headers)
    assert response.status_code == 401
    response_body = response.json()
    assert response_body['error']['code'] == 'CODIGO_LOCO'
    assert response_body['error']['description'] == "Invalid authentication scheme"


@patch("src.main.make_request")
@patch("src.main.get_validated_user")
def test_successful_finish_register(mock_get_validated_user, mock_make_request):
    mock_make_request.return_value = {"success": True}
    mock_get_validated_user.return_value = {"name":"Lionel Messi", "uid":"fake_uid"}
    headers = {"Authorization": "Bearer fake_token"}
    body = {
        "nickname": "LioMessi",
        "displayname": "Lionel Messi",
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
        ]
    }
    response = client.post("/users/finish_register", json=body, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"success": True}


