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


def test_post_total_price():
    response = client.post(
        "/totalprice/",
        json={
            "internet_connection": {"price": 200, "regularity": "Monthly"},
            "phone_lines": {"price": 150, "amount": 2, "regularity": "Monthly"},
            "cell_phones": [
                {
                    "name": "Motorola G99",
                    "price": 800,
                    "amount": 4,
                    "regularity": "Once",
                },
                {"name": "iPhone 99", "price": 6000, "amount": 1, "regularity": "Once"},
            ],
        },
    )
    assert response.status_code == 200
    assert response.json() == {"total_price": 9700}


def test_post_total_price_phone_lines_error_message():
    response = client.post(
        "/totalprice/",
        json={
            "phone_lines": {"price": 150, "amount": 10, "regularity": "Monthly"},
            "cell_phones": [
                {
                    "name": "Motorola G99",
                    "price": 800,
                    "amount": 2,
                    "regularity": "Once",
                },
            ],
        },
    )

    assert response.status_code == 422


def test_post_total_price_empty_request():
    response = client.post("/totalprice/", json={})

    assert response.json() == {"total_price": 0}


def test_read_cellphones():
    response = client.get("/cellphones")

    assert response.status_code == 200
    assert response.json() == [
        {"name": "Motorola G99", "price": 800, "amount": 1, "regularity": "Once"},
        {"name": "iPhone 99", "price": 6000, "amount": 1, "regularity": "Once"},
        {"name": "Samsung Galaxy 99", "price": 1000, "amount": 1, "regularity": "Once"},
        {"name": "Sony Xperia 99", "price": 900, "amount": 1, "regularity": "Once"},
        {"name": "Huawei 99", "price": 900, "amount": 1, "regularity": "Once"},
    ]
