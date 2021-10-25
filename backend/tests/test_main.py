from app.main import foo, app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_foo():
    assert foo("bar") == "foobar"


def test_false_foo():
    assert foo("foo") != "foobar"


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello! :wave:"}
