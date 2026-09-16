from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_api_status():
    assert client.get("/health").status_code == 200


def test_api_body():
    assert client.get("/health").json() == {"status": "ok"}
