import peewee

from app.utils.database import db
from app.model.user_model import User

class Bike(peewee.Model):
    license_plate = peewee.CharField(unique=True, index=True)
    displacement = peewee.FloatField()
    model = peewee.IntegerField()
    brand = peewee.CharField()
    reference = peewee.CharField()
    mileage = peewee.FloatField()
    user_id = peewee.ForeignKeyField(User, backref="bikes")
    
    class Meta:
        database = db