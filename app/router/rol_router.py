from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.schema import rol_schema
from app.service import rol_service
from app.utils.database import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/rol/",
    tags=["rols"],
    status_code=status.HTTP_201_CREATED,
    response_model=rol_schema.Rol,
    dependencies=[Depends(get_db)],
    summary="Creacion de un nuevo rol"
)
def create_rol(rol: rol_schema.RolBase = Body(...)):
    """
    ## Crear nuevo usuario enla app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for authentication

    ### Returns
    - user: User info
    """
    return rol_service.create_rol(rol)