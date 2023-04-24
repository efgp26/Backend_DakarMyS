import peewee

from app.utils.database import db

class User(peewee.Model):
    nombre = peewee.CharField()
    apellido = peewee.CharField()
    correo = peewee.CharField(unique=True, index=True)
    contrasena = peewee.CharField()
    ano_nacimiento = peewee.DateField()
    tipo_usuario = peewee.BooleanField()
    
    class Meta:
        database = db