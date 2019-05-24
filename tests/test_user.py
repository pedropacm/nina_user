import io

from mock import call, MagicMock, mock_open
import falcon
from falcon import testing
import json
import pytest

import nina_user.app
import nina_user.user


@pytest.fixture
def client():
    api = nina_user.app.create_app()
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_post_user_with_right_input(client):
    user_payload = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "12345"
    }
    response = client.simulate_post(
        '/api/v1/user/register',
        body = json.dumps(user_payload, ensure_ascii=False),
        headers={'content-type': falcon.MEDIA_JSON}
    )

    expected_response_body = {
        "status": "OK"
    }
    assert response.status == falcon.HTTP_OK
    assert response.json == expected_response_body

def test_post_user_missing_input_values(client):
    user_payload = {
        "name": "Test User",
        "email": "test@example.com"
    }
    response = client.simulate_post(
        '/api/v1/user/register',
        body = json.dumps(user_payload, ensure_ascii=False),
        headers={'content-type': falcon.MEDIA_JSON}
    )

    expected_response_body = {
        "status": "Bad Request"
    }
    assert response.status == falcon.HTTP_BAD_REQUEST
    assert response.json == expected_response_body

def test_auth_user(client):
    auth_payload = {
        "email": "test@example.com",
        "password": "12345"
    }
    response = client.simulate_post(
        '/api/v1/user/auth',
        body = json.dumps(auth_payload, ensure_ascii=False),
        headers={'content-type': falcon.MEDIA_JSON}
    )

    expected_response_body = {
        "status": "OK",
        "token": "token string"
    }
    assert response.status == falcon.HTTP_OK
    assert response.json == expected_response_body

def test_auth_user_wrong_password(client):
    auth_payload = {
        "email": "test@example.com",
        "password": "wrong_password"
    }
    response = client.simulate_post(
        '/api/v1/user/auth',
        body = json.dumps(auth_payload, ensure_ascii=False),
        headers={'content-type': falcon.MEDIA_JSON}
    )

    expected_response_body = {
        "status": "Bad Request"
    }
    assert response.status == falcon.HTTP_BAD_REQUEST
    assert response.json == expected_response_body

def test_auth_user_not_found(client):
    auth_payload = {
        "email": "usernotfound@example.com",
        "password": "pwd"
    }
    response = client.simulate_post(
        '/api/v1/user/auth',
        body = json.dumps(auth_payload, ensure_ascii=False),
        headers={'content-type': falcon.MEDIA_JSON}
    )

    expected_response_body = {
        "status": "Not Found"
    }
    assert response.status == falcon.HTTP_NOT_FOUND
    assert response.json == expected_response_body