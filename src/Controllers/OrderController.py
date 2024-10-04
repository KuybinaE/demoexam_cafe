from src.Models.Orders import *

class OrderController():
    def get(self):
        return Orders.select().execute()
    def add(self,count_cliens,table_id,drink_id,food_id,shift_id):
        Orders.create(count_cliens=count_cliens,table_id=table_id,drink_id=drink_id,food_id=food_id,shift_id=shift_id,status_id=3)
    #изменить статус на готов
    @classmethod
    def update_order_ready(cls,order_id):
        Orders.update({Orders.status_id : 4}).where(Orders.id==order_id).execute()
    def update_order_pay(cls,order_id):
        Orders.update({Orders.status_id : 2}).where(Orders.id==order_id).execute()
if __name__ == "__main__":
    ord = OrderController()
    OrderController.update_order_ready(2)
    ord.add(1,1,1,1,1)
    for row in ord.get():
        print(row.id, row.count_cliens,row.table_id.number,row.drink_id.name,row.food_id.name,row.shift_id,row.status_id.name)
