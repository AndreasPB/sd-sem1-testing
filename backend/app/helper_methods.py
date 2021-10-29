from app.models import (
    Purchase,
    Total,
)


def calc_purchase(purchase: Purchase) -> Total:
    total_price = 200 if purchase.internet_connection else 0

    if purchase.cell_phones:
        for cell_phone in purchase.cell_phones:
            total_price += cell_phone.price * cell_phone.amount
    if purchase.phone_lines:
        total_price += purchase.phone_lines.price * purchase.phone_lines.amount

    return Total(total_price=total_price)
