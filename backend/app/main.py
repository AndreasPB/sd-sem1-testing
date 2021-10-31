from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.helper_methods import calc_purchase
from app.models import Purchase, Total, CellPhone, InternetConnection, PhoneLine

app = FastAPI()


origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"msg": "Hello! :wave:"}


@app.post("/totalprice/", response_model=Total)
async def running_total(purchase: Purchase):
    return calc_purchase(purchase) if purchase else 0


@app.get("/internetconnection", response_model=InternetConnection)
async def get_internet_connection():
    return jsonable_encoder(InternetConnection())


@app.get("/phoneline", response_model=PhoneLine)
async def get_phoneline():
    return jsonable_encoder(PhoneLine(amount=1))


@app.get("/cellphones", response_model=list[CellPhone])
async def get_cellphones():

    services = [
        CellPhone(name="Motorola G99", price=800),
        CellPhone(name="iPhone 99", price=6000),
        CellPhone(name="Samsung Galaxy 99", price=1000),
        CellPhone(name="Sony Xperia 99", price=900),
        CellPhone(name="Huawei 99", price=900),
    ]

    return jsonable_encoder(services)


def foo(bar: str) -> str:
    string = f"foo{bar}"
    print(string)
    return string
