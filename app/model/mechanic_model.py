import peewee

from app.utils.database import db

class Mechanic(peewee.Model):
    name = peewee.CharField()
    last_name = peewee.CharField()
    phone = peewee.CharField()
    date_admission = peewee.DateField()
    departure_date = peewee.DateField()
    
    class Meta:
        database = db