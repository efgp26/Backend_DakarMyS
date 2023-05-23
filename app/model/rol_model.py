import peewee

from app.utils.database import db

class Rol(peewee.Model):
    type_rol_model = peewee.CharField()    
    
    class Meta:
        database = db