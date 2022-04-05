from peewee import *

db = SqliteDatabase('db')

class Country(Model):
    name = CharField()
    code = CharField()
    class Meta:
        database = db

class Region(Model):
    name = CharField()
    code = CharField()
    country = ForeignKeyField(Country, backref="country")

    class Meta:
        database = db

class Node(Model):
    address = CharField()
    url = CharField()
    hostname = CharField()
    region = ForeignKeyField(Region, backref='region')

    class Meta:
        database = db


db.connect()
db.create_tables([Country, Region, Node])
