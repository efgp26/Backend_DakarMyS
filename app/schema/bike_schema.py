from pydantic import BaseModel
from pydantic import Field
from datetime import datetime


class BikeBase(BaseModel):
    license_plate: str = Field(
        ...,
        min_length=3,
        max_length=25,
        example="RGB206"
    )
    displacement: float = Field(
        ...,
        min_length=2,
        max_length=25,
        example="1000"
    )
    model: int = Field(
        ...,
        min_length=4,
        max_length=4,
        example="2023"
    )
    brand: str = Field(
        ...,
        min_length=3,
        max_length=25,
        example="suzuki"
    )
    reference: str = Field(
        ...,
        min_length=3,
        max_length=25,
        example="fz 2.0"
    )
    mileage: float = Field(
        ...,
        min_length=1,
        max_length=25,
        example="17000"
    )
    

class Bike(BikeBase):
    id: int = Field(
        ...,
        example="5"
    )
