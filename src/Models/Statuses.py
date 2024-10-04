#Модель описывающая сущность из таблицы статусов заказов
from src.Models.Base import *

class Statuses(Base):
    id = PrimaryKeyField()
    name = CharField()
