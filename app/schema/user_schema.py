from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="myemail@gmail.com"
    )
    name: str = Field(
        ...,
        min_length=3,
        max_length=25,
        example="Juan Jose"
    )
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=25,
        example="Gaviria"
    )
    born_year: datetime = Field(
        ...,        
    )
    data_create: datetime = Field(
        ...,        
    )
    phone: str = Field(
        ...,   
        min_length=8,
        max_length=10,     
    )
    
    


class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )


class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=16,
        example="strongpass"
    )