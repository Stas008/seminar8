from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import font
from turtle import color
import csv
from webbrowser import get
from tkinter import messagebox as mb
from tkinter import filedialog
import add_win
import edit_win
import controller
import find_win

path = "pb.csv"
my_list = []


my_list = controller.refresh_list(path)

root = Tk()
root.title("Students Book")
root.geometry("750x400")

def open_click():
    path = filedialog.askopenfilename()
    refresh_click()
def refresh_click():
    my_list = controller.refresh_list(path)
    lbox.delete(0, END)
    for i in range(0,len(my_list)):
            lbox.insert(0,controller.format_line(my_list, i, [10,12,5,15,5,7]))
    lbox.select_set(0)
    show_btns()
def show_btns():
    show_btn['state'] = tkinter.NORMAL
    add_btn['state'] = tkinter.NORMAL
    edit_btn['state'] = tkinter.NORMAL
    del_btn['state'] = tkinter.NORMAL
    exp_btn['state'] = tkinter.NORMAL
def hide_btns():
    show_btn['state'] = tkinter.DISABLED
    add_btn['state'] = tkinter.DISABLED
    edit_btn['state'] = tkinter.DISABLED
    del_btn['state'] = tkinter.DISABLED
    exp_btn['state'] = tkinter.DISABLED
def show_click():
    find_win.find_wind()
def btn_edit_click():
    hide_btns()
    my_list = controller.refresh_list(path)
    edit_win.wind_edit(len(my_list) - 1 - lbox.curselection()[0])
def add_click():
    hide_btns()
    add_win.new_wind()
    refresh_btn()
def btn_del_click():
    print (len(my_list) - 1 - lbox.curselection()[0])
    check_del(my_list[len(my_list) - 1 - lbox.curselection()[0]][0])
def check_del(cont):
    answer = mb.askyesno(
    title="Вы уверены?", 
    message=f"Удалить {cont}?")
    if answer:
        my_list.remove(my_list[len(my_list) - 1 - lbox.curselection()[0]])
        controller.list_to_file(my_list, path)
def btn_exp_click():
    new_path = str(filedialog.asksaveasfilename())
    controller.list_to_file(my_list, new_path)
def btn_exit_click():
    root.destroy()
    
lbox = Listbox(width=69, height=22, bg="white", fg="blue", font=('Courier'))
lbox.place(x=10, y=50)
open_btn = ttk.Button(text="Открыть", width=12, command=open_click)
open_btn.place(x=580, y=50)
refresh_btn = ttk.Button(text="Обновить", width=12, command=refresh_click)
refresh_btn.place(x=580, y=90)
show_btn=ttk.Button(text="Найти",width=12, command=show_click)
show_btn['state'] = tkinter.DISABLED
show_btn.place(x=580, y=130)
add_btn = ttk.Button(text="Добавить",width=12, command=add_click)
add_btn['state'] = tkinter.DISABLED
add_btn.place(x=580, y=170)
edit_btn = ttk.Button(text="Редактировать",width=12, command=btn_edit_click)
edit_btn['state'] = tkinter.DISABLED
edit_btn.place(x=580, y=210)
del_btn = ttk.Button(text="Удалить",width=12, command=btn_del_click)
del_btn['state'] = tkinter.DISABLED
del_btn.place(x=580, y=250)
exp_btn = ttk.Button(text="Экспорт",width=12, command=btn_exp_click)
exp_btn['state'] = tkinter.DISABLED
exp_btn.place(x=580, y=290)
exit_btn = ttk.Button(text="Выход",width=12, command=btn_exit_click)
exit_btn.place(x=580, y=330)
lab1 = ttk.Label(text="Имя            Фамилия       Пол     Телефон           Курс    Группа    Статус", font='Helvetica 13 bold')
lab1.place(x=10, y=26)

root.mainloop()
