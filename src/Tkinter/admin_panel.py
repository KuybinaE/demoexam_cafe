#Окно-панель администратора
from tkinter import *
from src.Controllers.UserController import UserController


admin_panel = Tk()
admin_panel.geometry('1700x800')
admin_panel.title("Панель администратора")
#Заголовок
title_window = Label(admin_panel,text='Панель администратора',font=(24),
                     anchor='center',width=188)
# title_window.grid(column=0,row=0,padx=1,pady=10)
title_window.grid(column=0,row=0,columnspan=400,padx=0,pady=10)
# title_window.pack(expand = True,anchor = N)
#Сотрудники
title_employee = Label(admin_panel, text="Сотрудники",font=(24))
title_employee.grid(column=1,row=1,padx=1,pady=10)
#логин,должность и кнопка
user = UserController()
list_user = user.get()
count_row = 2
for row in list_user:
    login_title = Label(admin_panel,text=row.login)
    login_title.grid(column=0,row=count_row,padx=1,pady=1)
    login_role = Label(admin_panel,text=row.role_id.role)
    login_role.grid(column=1,row=count_row,padx=0,pady=1)
    button_login=Button(admin_panel,
                        text='Уволить',
                        height=2,
                        width=8,
                        background='red',
                        foreground='white',
                        command=user.update_status(row.id))
    button_login.grid(column=2,row=count_row,padx=0,pady=1)
    count_row+=1










admin_panel.mainloop()