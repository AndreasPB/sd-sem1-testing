from app.helper_methods import calc_purchase
from app.models import (
    Purchase,
    PhoneLine,
    Total,
    CellPhone,
    InternetConnection,
)


def test_calculate_total():
    assert (
        calc_purchase(
            Purchase(
                internet_connection=InternetConnection(),
                phone_lines=PhoneLine(amount=2),
                cell_phones=[CellPhone(name="Motorola G99", price=800, amount=2)],
            )
        )
        == Total(total_price=2100)
    )
