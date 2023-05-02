from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from datetime import datetime


class UserBase(BaseModel):
    correo: EmailStr = Field(
        ...,
        example="myemail@gmail.com"
    )
    nombres: str = Field(
        ...,
        min_length=3,
        max_length=25,
        example="Juan Jose"
    )
    apellidos: str = Field(
        ...,
        min_length=3,
        max_length=25,
        example=""
    )
    ano_nacimiento: datetime.date = Field(
        ...,
        min_length=3,
        max_length=15,
        example="Juan"
    )
    tipo_usuario: bool = Field(
        ...,
        min_length=3,
        max_length=25,
        example=""
    )
    


class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )


class UserRegister(UserBase):
    contrasena: str = Field(
        ...,
        min_length=8,
        max_length=16,
        example="strongpass"
    )