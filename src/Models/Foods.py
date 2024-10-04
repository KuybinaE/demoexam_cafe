#Модель описывающая сущность из таблицы еды
from src.Models.Base import *

class Foods(Base):
    id = PrimaryKeyField()
    name = CharField()
    price = DecimalField()
