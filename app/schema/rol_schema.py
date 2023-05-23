from typing import Optional
from pydantic import BaseModel
from pydantic import Field



class RolBase(BaseModel):
    type_rol_model: str = Field(
        ...,
        example="usermon"
    )

class Rol(RolBase):
    id: int = Field(
        ...,
        example="5"
    )