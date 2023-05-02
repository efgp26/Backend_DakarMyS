from app.model.bike_model import Bike
from app.model.service_model import Service
from app.model.soat_model import Soat
from app.model.tecno_model import Tecno
from app.model.user_model import User

from app.utils.database import db

def create_tables():
    with db:
        db.create_tables([Bike,Service,Soat,Tecno,User])