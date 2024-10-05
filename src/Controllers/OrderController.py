from src.Models.Orders import *

class OrderController():
    #вывести список заказов
    @classmethod
    def get(cls):
        return Orders.select()
    #создать заказ
    @classmethod
    def add_order(self,count_cliens,table_id,drink_id,food_id,shift_id):
        Orders.create(count_cliens=count_cliens,table_id=table_id,drink_id=drink_id,food_id=food_id,shift_id=shift_id,status_id=1)
    #изменить статус на готов
    @classmethod
    def update_order_ready(cls,order_id):
        Orders.update({Orders.status_id : 4}).where(Orders.id==order_id).execute()
    #изменить статус на оплачен
    @classmethod
    def update_order_pay(cls,order_id):
        Orders.update({Orders.status_id : 2}).where(Orders.id==order_id).execute()
    #метод вывода заказов заданной смены
    @classmethod
    def show(cls,shift_id):
        return Orders.select().where(Orders.shift_id==shift_id)
    #изменить статус на готовится
    @classmethod
    def update_order_cooking(cls,order_id):
        Orders.update({Orders.status_id: 3}).where(Orders.id == order_id).execute()


if __name__ == "__main__":
    ord = OrderController()
    OrderController.add_order(3,3,3,3,3)
    # OrderController.update_order_ready(2)
    # OrderController.update_order_pay(7)
    # OrderController.update_order_cooking(8)
    # for order in OrderController.show(2):
    #     print(order.id,order.count_cliens,order.table_id,order.drink_id.name)
    # for row in ord.get():
    #     print(row.id, row.count_cliens,row.table_id.number,row.drink_id.name,row.food_id.name,row.shift_id,row.status_id.name)

    for order in OrderController.get():
        print(order.id, order.count_cliens, order.table_id, order.drink_id.name,'Статус заказа: ',order.status_id.name,'Еда',order.food_id.name)

