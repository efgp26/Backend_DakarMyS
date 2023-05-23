from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.schema import user_schema
from app.service import user_service
from app.utils.database import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Creacion de un nuevo usuario"
)
def create_user(user: user_schema.UserRegister = Body(...)):
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
    return user_service.create_user(user)