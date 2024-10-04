#Базовая модель peewee
from src.Connection import *
from peewee import *
from src.Connection.connect import connect


class Base(Model):
    class Meta:
        database = connect
