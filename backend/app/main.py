from fastapi import FastAPI
from app.helper_methods import calc_purchase
from app.models import (
    Purchase,
    Total,
)

app = FastAPI()


@app.get("/")
async def index():
    return {"msg": "Hello! :wave:"}


@app.post("/totalprice/", response_model=Total)
async def running_total(purchase: Purchase):
    return calc_purchase(purchase) if purchase else 0


def foo(bar: str) -> str:
    string = f"foo{bar}"
    print(string)
    return string
