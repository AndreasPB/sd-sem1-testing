from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from app.helper_methods import calc_purchase
from app.models import (
    Purchase,
    Total,
    CellPhone,
    Regularity,
)

app = FastAPI()


@app.get("/")
async def index():
    return {"msg": "Hello! :wave:"}


@app.post("/totalprice/", response_model=Total)
async def running_total(purchase: Purchase):
    return calc_purchase(purchase) if purchase else 0


@app.get("/cellphones", response_model=list[CellPhone])
async def get_cellphones():

    services = [
        CellPhone(name="Motorola G99", price=800, regularity=Regularity.ONCE),
        CellPhone(name="iPhone 99", price=6000, regularity=Regularity.ONCE),
        CellPhone(name="Samsung Galaxy 99", price=1000, regularity=Regularity.ONCE),
        CellPhone(name="Sony Xperia 99", price=900, regularity=Regularity.ONCE),
        CellPhone(name="Huawei 99", price=900, regularity=Regularity.ONCE),
    ]

    return jsonable_encoder(services)


def foo(bar: str) -> str:
    string = f"foo{bar}"
    print(string)
    return string
