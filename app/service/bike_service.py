from fastapi import HTTPException, status


from app.model.user_model import User as UserModel
from app.schema import bike_schema



def create_user(bike: bike_schema.UserRegister):
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
        rol_id = rol
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