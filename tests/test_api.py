import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_api_status():
    assert client.get("/health").status_code == 200


def test_api_body():
    assert client.get("/health").json() == {"status": "ok"}


def test_echo_valid():
    response = client.post("/echo", json={"mensaje": "hola", "veces": 3})
    assert response.status_code == 200
    assert response.json() == {"resultado": "hola hola hola", "longitud": 14}


@pytest.mark.parametrize(
    "payload, statuscode",
    [
        ({"veces": 3}, 422),
        ({"mensaje": "hola", "veces": 325}, 422),
        ({"mensaje": "hola", "veces": "tres"}, 422),
    ],
)
def test_echo_invalid(payload, statuscode):
    assert client.post("/echo", json=payload).status_code == statuscode
