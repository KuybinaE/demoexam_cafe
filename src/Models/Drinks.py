#Модель описывающая сущность из таблицы напитков
from src.Models.Base import *

class Drinks(Base):
    id = PrimaryKeyField()
    name = CharField()
    price = DecimalField()