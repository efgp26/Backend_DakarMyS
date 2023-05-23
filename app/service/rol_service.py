from fastapi import HTTPException, status

from passlib.context import CryptContext

from app.model.rol_model import Rol as RolModel
from app.schema import rol_schema


def create_rol(rol: rol_schema.RolBase):
    get_rol = RolModel.filter((RolModel.type_rol_model == rol.type_rol_model)).first()
    if get_rol:
        msg = "Rol already registered"        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_rol = RolModel(        
        type_rol_model=rol.type_rol_model
    )

    db_rol.save()

    return rol_schema.Rol(
        id=db_rol.id,
        type_rol_model=db_rol.type_rol_model
    )