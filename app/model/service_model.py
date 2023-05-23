import peewee

from app.utils.database import db
from app.model.bike_model import Bike
from app.model.mechanic_model import Mechanic

class Service(peewee.Model):
    name = peewee.CharField()
    description = peewee.CharField()
    date_admission = peewee.DateField()
    departure_date = peewee.DateField()
    value_service = peewee.FloatField()
    bike_id = peewee.ForeignKeyField(Bike, backref='service', unique=True)
    mechanic_id = peewee.ForeignKeyField(Mechanic, backref='mechanic', unique=True)
    
    class Meta:
        database = db