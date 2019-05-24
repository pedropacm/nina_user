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

    print(response)

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

    print(response)

    assert response.status == falcon.HTTP_BAD_REQUEST
    assert response.json == expected_response_body
