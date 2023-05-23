from fastapi import HTTPException, status

from passlib.context import CryptContext

from app.model.user_model import User as UserModel
from app.schema import user_schema
from app.schema import rol_schema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    """_summary_

    Args:
        password (_type_): _description_

    Returns:
        _type_: _description_
    """
    return pwd_context.hash(password)

def create_user(user: user_schema.UserRegister, rol: rol_schema.Rol):
    #todo hacer validacion tambien por placa
    get_user = UserModel.filter((UserModel.email == user.email)).first()
    if get_user:
        msg = "Email already registered"        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(        
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        password=get_password_hash(user.password),        
        born_year=user.born_year,        
        data_create=user.data_create,
        phone=user.phone,
        rol_id=rol.id
    )

    db_user.save()

    return user_schema.User(
        id = db_user.id,
        name = db_user.name,
        last_name = db_user.last_name,
        email = db_user.email,
        born_year=db_user.born_year,
        data_create = db_user.data_create,
        phone = db_user.phone
    )