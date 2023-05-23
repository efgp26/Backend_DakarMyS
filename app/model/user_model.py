import peewee

from app.utils.database import db
from app.model.rol_model import Rol

class User(peewee.Model):
    name = peewee.CharField()
    last_name = peewee.CharField()
    email = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()
    born_year = peewee.DateField()
    data_create = peewee.DateField()
    phone = peewee.CharField()
    rol_id = peewee.ForeignKeyField(Rol, backref="rols")

    class Meta:
        database = db