#Окно-панель администратора
from tkinter import *
from src.Controllers.OrderController import OrderController
from src.Controllers.ShiftController import ShiftController
from src.Controllers.UserController import UserController
from tkinter import ttk
def admin():
    #Функционал
    #Создание диалогового окна
    def status_false(id):
        button_login.configure(text="Уволен",background='grey')
        user.update_status(id)
        update()
    def add_user(login,name,passwd,role):
        user.add(login,passwd,name,role)
        admin_panel.after(1000,update)
    def add_shift(date,cook_id,oficiant_1_id,oficiant_2_id):
        shift.add(date,cook_id,oficiant_1_id,oficiant_2_id)
        admin_panel.after(1000, update)
    #обновление окна
    def update():
        admin_panel.destroy()
        admin()
    #Отрисовка
    admin_panel = Tk()
    admin_panel.geometry('2000x1100')
    admin_panel.title("Панель администратора")
    #Заголовок
    title_window = Label(admin_panel,text='Панель администратора',font=(24),
                         anchor='center',width=45)
    title_window.grid(column=0,row=0,columnspan=12,padx=650,pady=10)
    #Сотрудники
    title_employee = Label(admin_panel, text="Сотрудники",font=(24))
    title_employee.grid(column=1,row=1,padx=1,pady=10)
    #логин,должность и кнопка
    user = UserController()
    list_user = user.get()
    count_row = 3
    for row in list_user:
        if row.status:
            login_title = Label(admin_panel, text="ИМЯ")
            login_title.grid(column=0, row=2, padx=1, pady=1)
            login_title = Label(admin_panel,text=row.login)
            login_title.grid(column=0,row=count_row,padx=1,pady=1)
            login_role = Label(admin_panel,text="ДОЛЖНОСТЬ")
            login_role.grid(column=1,row=2,padx=0,pady=1)
            login_role = Label(admin_panel,text=row.role_id.role)
            login_role.grid(column=1,row=count_row,padx=0,pady=1)
            button_login=Button(admin_panel,
                                text='Уволить',
                                height=2,
                                width=8,
                                background='red',
                                foreground='white',
                                command=lambda id=row.id:status_false(id))
            button_login.grid(column=2,row=count_row,padx=0,pady=1)

            print(row.login,row.status)
            count_row+=1
    #список заказов
    title_employee = Label(admin_panel, text="Список заказов", font=(24))
    title_employee.grid(column=6, row=1, padx=1, pady=10)
    order = OrderController()
    list_order = order.get()
    count_row = 3
    for row in list_order:
        login_table_id = Label(admin_panel, text="СТОЛИК")
        login_table_id.grid(column=5, row=2, padx=1, pady=1)
        login_table_id = Label(admin_panel,text=row.table_id.number)
        login_table_id.grid(column=5, row=count_row, padx=1, pady=1)
        login_count_cliens = Label(admin_panel, text="КОЛИЧЕСТВО КЛИЕНТОВ")
        login_count_cliens.grid(column=6, row=2, padx=1, pady=1)
        login_count_cliens = Label(admin_panel, text=row.count_cliens)
        login_count_cliens.grid(column=6, row=count_row, padx=0, pady=1)
        login_food_id = Label(admin_panel, text="БЛЮДА")
        login_food_id.grid(column=7, row=2, padx=1, pady=1)
        login_food_id = Label(admin_panel, text=row.food_id.name)
        login_food_id.grid(column=7, row=count_row, padx=0, pady=1)
        count_row += 1
    #список смен
    title_employee = Label(admin_panel, text="Список смен", font=(24))
    title_employee.grid(column=9, row=1, padx=1, pady=10)
    shift = ShiftController()
    list_order = shift.get()
    count_row = 3
    for row in list_order:
        login_datetime = Label(admin_panel, text="НОМЕР СМЕНЫ")
        login_datetime.grid(column=8, row=2, padx=1, pady=1)
        login_datetime = Label(admin_panel, text=row.date)
        login_datetime.grid(column=8, row=count_row, padx=1, pady=1)
        login_cook_id = Label(admin_panel, text="ПОВАР")
        login_cook_id.grid(column=9, row=2, padx=1, pady=1)
        login_cook_id= Label(admin_panel, text=row.cook_id.name)
        login_cook_id.grid(column=9, row=count_row, padx=0, pady=1)
        login_oficiant_1_id = Label(admin_panel, text="ОФИЦИАНТ")
        login_oficiant_1_id.grid(column=10, row=2, padx=1, pady=1)
        login_oficiant_1_id = Label(admin_panel, text=row.oficiant_1_id.name)
        login_oficiant_1_id.grid(column=10, row=count_row, padx=0, pady=1)
        login_oficiant_2_id = Label(admin_panel, text="ОФИЦИАНТ")
        login_oficiant_2_id.grid(column=11, row=2, padx=1, pady=1)
        login_oficiant_2_id = Label(admin_panel, text=row.oficiant_2_id.name)
        login_oficiant_2_id.grid(column=11, row=count_row, padx=0, pady=1)
        count_row += 1
    #добавить пользователя
    input_login = Entry(admin_panel,width=20)
    name_input_login = Label(admin_panel,text="Введите логин")
    name_input_login.grid(column=3,row =2)
    input_login.grid(column=3,row =3)

    input_name = Entry(admin_panel, width=20)
    name_input_name = Label(admin_panel, text="Введите имя")
    name_input_name.grid(column=3, row=4)
    input_name.grid(column=3, row=5)

    input_password = Entry(admin_panel, width=20)
    name_input_password = Label(admin_panel, text="Введите пароль")
    name_input_password.grid(column=3, row=6)
    input_password.grid(column=3, row=7)

    input_role = Entry(admin_panel, width=20)
    name_input_role = Label(admin_panel, text="Введите id должности")
    name_input_role.grid(column=3, row=8)
    input_role.grid(column=3, row=9)

    button_add_user = Button(admin_panel,text="Добавить пользователя",
                             height=2,
                             width=20,
                             background='green',
                             foreground='white',
                             command=lambda :add_user(input_login.get(),input_name.get(),
                                                      input_password.get(),input_role.get()))
    button_add_user.grid(column=3,row=10)
    #добавить смену
    input_date = Entry(admin_panel, width=20)
    number_shift = Label(admin_panel, text="Введите номер смены")
    number_shift.grid(column=12, row=2)
    input_date.grid(column=12, row=3)

    input_name_cook = Entry(admin_panel, width=20)
    name_cook = Label(admin_panel, text="Введите имя повара")
    name_cook.grid(column=12, row=4)
    input_name_cook.grid(column=12, row=5)

    input_oficiant1 = Entry(admin_panel, width=20)
    name_oficiant1 = Label(admin_panel, text="Введите оффицианта")
    name_oficiant1.grid(column=12, row=6)
    input_oficiant1.grid(column=12, row=7)

    input_oficiant2 = Entry(admin_panel, width=20)
    name_oficiant2 = Label(admin_panel, text="Введите оффицианта")
    name_oficiant2.grid(column=12, row=8)
    input_oficiant2.grid(column=12, row=9)

    button_add_shift = Button(admin_panel, text="Добавить смену",
                             height=2,
                             width=20,
                             background='green',
                             foreground='white',
                             command=lambda: add_shift(input_date.get(), input_name_cook.get(),
                                                      input_oficiant1.get(), input_oficiant2.get()))
    button_add_shift.grid(column=12, row=10)
    #вывод смен
    #добавить смену
    title_cook = Label(admin_panel,text="Выберите повара")
    title_cook.grid(column = 10, row = 2)
    #вывод поваров в виде списка
    list_cook = UserController.list_user(2)
    combobox_cook = ttk.Combobox(values=list_cook)
    combobox_cook.grid(column = 10,row=3)
    admin_panel.mainloop()

if __name__ == "__main__":
    admin()