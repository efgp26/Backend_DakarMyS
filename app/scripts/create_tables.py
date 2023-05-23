from app.model.bike_model import Bike
from app.model.service_model import Service
from app.model.rol_model import Rol
from app.model.mechanic_model import Mechanic
from app.model.user_model import User

from app.utils.database import db

def create_tables():

    with db:
        db.create_tables([Bike,Service,Rol,Mechanic,User])