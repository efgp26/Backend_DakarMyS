import peewee

from app.utils.database import db
from app.model.bike_model import Bike

class Service(peewee.Model):
    nombre = peewee.CharField()
    descripcion = peewee.CharField()
    fecha = peewee.DateField()
    bike_id = peewee.ForeignKeyField(Bike, backref='service', unique=True)
    
    class Meta:
        database = db