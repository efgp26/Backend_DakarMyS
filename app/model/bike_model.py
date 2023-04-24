import peewee

from app.utils.database import db
from app.model.user_model import User

class Bike(peewee.Model):
    placa = peewee.CharField(unique=True, index=True)
    cilindraje = peewee.FloatField()
    modelo = peewee.IntegerField()
    marca = peewee.CharField()
    referencia = peewee.CharField()
    kilometraje = peewee.FloatField()
    usuario_id = peewee.ForeignKeyField(User, backref="bikes")
    
    class Meta:
        database = db