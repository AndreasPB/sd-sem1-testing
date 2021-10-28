import pytest

from pydantic.error_wrappers import ValidationError

from app.models import (
    Purchase,
    PhoneLine,
    Total,
    CellPhone,
    InternetConnection,
    Regularity,
)


def test_purchase():
    assert Purchase(
        internet_connection=InternetConnection(),
        phone_lines=PhoneLine(amount=3),
        cell_phones=[
            CellPhone(name="Nokia 3310", price=1337),
            CellPhone(name="Sony Ericsson XPREIA X10 mini pro", price=1337),
        ],
    )


def test_total():
    assert Total(total_price=1337)
    assert Total(total_price=0)

    with pytest.raises(ValidationError):
        assert Total(total_price=-420)


def test_internet_connection():
    assert InternetConnection(price=200, regularity=Regularity.MONTHLY)

    with pytest.raises(ValidationError):
        assert InternetConnection(price=0, regularity=Regularity.MONTHLY)

    with pytest.raises(ValidationError):
        assert InternetConnection(price=200, regularity="foobarbaz")


def test_cell_phone():
    assert CellPhone(name="Nokia 3310", price=1337, regularity=Regularity.ONCE)

    with pytest.raises(ValidationError):
        assert CellPhone(name="Nokia 3310", price=420, regularity=Regularity.ONCE)

    with pytest.raises(ValidationError):
        assert CellPhone(name="Nokia 3310", price=1337, regularity="foobarbaz")


def test_phone_line():
    assert PhoneLine(price=150, amount=3, regularity=Regularity.MONTHLY)

    with pytest.raises(ValidationError):
        assert PhoneLine(price=123, amount=3, regularity=Regularity.MONTHLY)

    with pytest.raises(ValidationError):
        assert PhoneLine(price=150, amount=0, regularity=Regularity.MONTHLY)

    with pytest.raises(ValidationError):
        assert PhoneLine(price=150, amount=3, regularity="foobarbaz")
