from optparse import Values
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import color
import csv
from numpy import size

new_cont = ("","")
path = "pb.csv"
def new_wind():
    def write_to_file():
        s = (str(text_name.get())+","+str(text_surname.get())+","+str(comb_sex.get())+","+str(text_phone.get())+","+str(comb_course.get())+","+str(text_group.get())+","+str(comb_status.get())+"\n")
        with open (path, "a") as data:
            data.write(s)
        
        add_window.destroy()

    add_window = Tk()
    add_window.geometry("750x260")
    add_window.title("Добавить запись")
    labelName = tkinter.Label(add_window, text = "Имя")
    text_name = tkinter.Entry(add_window, text ="Имя")
    labelPhone = tkinter.Label(add_window, text = "Телефон")
    text_surname = tkinter.Entry(add_window, text ="Фамилия")
    label_surname = tkinter.Label(add_window, text = "Фамилия")
    text_phone = tkinter.Entry(add_window)
    comb_sex=ttk.Combobox(add_window, text="пол", values = [
                                    "М", 
                                    "Ж"])
    comb_sex.configure(width=4)
    label_sex=tkinter.Label(add_window, text = "Пол")
    comb_course=ttk.Combobox(add_window, text="курс", values = [
                                "1", 
                                "2",
                                "3",
                                "4",
                                "5"])
    comb_course.configure(width=4)
    label_course=tkinter.Label(add_window, text = "Курс")
    text_group = tkinter.Entry(add_window, text ="Группа")
    label_group = tkinter.Label(add_window, text = "Группа")
    comb_status=ttk.Combobox(add_window, text="Успеваемость", values = [
                "отличник", 
                "хорошист",
                "троешник",
                "на отчисление"])
    comb_status.configure(width=18)
    label_status=tkinter.Label(add_window, text = "Успеваемость")

    button_ok = tkinter.Button(add_window, text = "Добавить контакт", command = write_to_file)
    
    labelName.place(x=10, y=10)
    text_name.place(x=10, y=40)
    label_surname.place(x=260,y=10)
    text_surname.place(x=260, y=40)
    labelPhone.place(x=510,y=10)
    text_phone.place(x=510, y=40)
    comb_sex.place(x=10,y=120)
    label_sex.place(x=10, y= 90)
    comb_course.place(x=140,y=120)
    label_course.place(x=140,y=90)
    text_group.place(x=260, y=120)
    label_group.place(x=260, y=90)
    button_ok.place(x=280, y=180)
    comb_status.place(x=510, y=120)
    label_status.place(x=510, y=90)

    add_window.mainloop()

 

