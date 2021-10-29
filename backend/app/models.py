from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field
from pydantic.class_validators import validator


class Regularity(Enum):
    MONTHLY = "Monthly"
    ONCE = "Once"


class BaseConfig(BaseModel):
    class Config:
        orm_mode = True


class InternetConnection(BaseConfig):
    price: int = 200
    regularity: Regularity = Regularity.MONTHLY

    @validator("price")
    def correct_price(cls, v):
        if v != 200:
            raise ValueError("Price can only be 200")
        return int(v)


class PhoneLine(BaseConfig):
    price: int = 150
    amount: int = Field(..., min=1, max=8, desc="The amount of phone lines")
    regularity: Regularity = Regularity.MONTHLY

    @validator("price")
    def correct_price(cls, v):
        if v != 150:
            raise ValueError("Price can only be 150")
        return int(v)

    @validator("amount")
    def correct_amount_between(cls, v):
        if not (1 <= v <= 8):
            raise ValueError("Amount needs to be between 1 and 8")
        return int(v)


class CellPhone(BaseConfig):
    name: str
    price: int
    amount: int = Field(1, min=1, desc="The amount of phones")
    regularity: Regularity = Regularity.ONCE

    @validator("price")
    def correct_total_price(cls, v):
        if v < 800:
            raise ValueError("Price cannot be less than the cheapest phone")
        return int(v)

    @validator("amount")
    def correct_amount_between(cls, v):
        if v < 1:
            raise ValueError("Amount needs to be at least 1")
        return int(v)


class Purchase(BaseConfig):
    internet_connection: Optional[InternetConnection]
    phone_lines: Optional[PhoneLine]
    cell_phones: Optional[list[CellPhone]]


class Total(BaseConfig):
    total_price: int = Field(..., min=0)

    @validator("total_price")
    def correct_total_price(cls, v):
        if v < 0:
            raise ValueError("Total price cannot be a negative number")
        return int(v)
