from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app

client = TestClient(app)


def test_root_must_return_hello_world():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}
