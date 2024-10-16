#Управление пользователями

from src.Models.Users import *

class UserController():
    #метод авторизации
    def log_in(self,input_login,input_password):
        user = Users.get_or_none(Users.login == input_login, Users.password == input_password)
        if user:
            return True
        else:
            return False
    #вызов пользователей
    def get(self):
        return Users.select().execute()
    #добавить пользователя
    def add(self,input_login,input_password,input_name,input_role_id):
        Users.create(login = input_login,password = input_password,name = input_name,role_id =input_role_id)
    #уволить - изменить статус на False
    def update_status(self,id_user):
        Users.update({Users.status:False}).where(Users.id == id_user).execute()
    #метод КЛАССА
    @classmethod
    #метод, который выводит id по имени
    def show(cls,login):
        return Users.get(Users.login==login)
    #Вывод списка в зависимости от роль
    @classmethod
    def show_user(cls,role_id):
        return Users.select().where(Users.role_id==role_id)
    @classmethod
    def list_user(cls,role_id):
        list = []
        for user in UserController.show_user(role_id):
            list.append(user.login)
        return list
if __name__ == "__main__":
    # users = UserController()
    # print(users.log_in('admin_Ekaterina','11111'))
    # for row in users.get():
    #     print(row.login)
    #
    # # users.add('waiter_Ivan','0000','Ivan','3')
    #
    # for row in users.get():
    #     print(row.id,row.login,row.status)
    # users.update_status(9)
    # for row in users.get():
    #     print(row.id,row.login,row.status)
    # print(users.show('waiter_Ivan'))
    # print(UserController.show('admin_Ekaterina').role_id)
    for row in UserController.show_user(3):
        print(row.login)
    print(UserController.list_user(3))