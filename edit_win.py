from dataclasses import field
from readline import insert_text
import tkinter
from tkinter import *
from tkinter import ttk
import csv
import controller
my_list = []
path = "pb.csv"
def wind_edit(index):
    my_list = []
    with open (path,"r") as data:
        reader = csv.reader (data, delimiter=",")
        for item in reader:
            my_list.append(item)
    def add_data_to_list():
        s = (str(text_name.get())+","+str(text_surname.get())+","+str(comb_sex.get())+","+str(text_phone.get())+","+str(comb_course.get())+","+str(text_group.get())+","+str(comb_status.get())+"\n")
        temp_s = s[:-1].split(',')
        my_list[index] = temp_s
        controller.list_to_file(my_list, path)        
        edit_window.destroy()
    edit_window = Tk()
    edit_window.geometry("750x260")
    edit_window.title("Редактировать запись")
    labelName = tkinter.Label(edit_window, text = "Имя")
    text_name = tkinter.Entry(edit_window,exportselection="12",textvariable="123")
    text_name.insert(0,str(my_list[index][0]))
    labelPhone = tkinter.Label(edit_window, text = "Телефон")
    text_surname = tkinter.Entry(edit_window, text ="Фамилия")
    text_surname.insert(0,str(my_list[index][1]))
    label_surname = tkinter.Label(edit_window, text = "Фамилия")
    text_phone = tkinter.Entry(edit_window)
    comb_sex=ttk.Combobox(edit_window, text="пол", values = [
                                    "М", 
                                    "Ж"])
    comb_sex.configure(width=4)
    comb_sex.insert(0,str(my_list[index][2]))
    text_phone.insert(0,str(my_list[index][3]))
    label_sex = tkinter.Label(edit_window, text = "Пол")
    comb_course = ttk.Combobox(edit_window, text="курс", values = [
                                "1", 
                                "2",
                                "3",
                                "4",
                                "5"])
    comb_course.configure(width=4)
    comb_course.insert(0,str(my_list[index][4]))
    label_course = tkinter.Label(edit_window, text = "Курс")
    text_group = tkinter.Entry(edit_window, text ="Группа")
    label_group = tkinter.Label(edit_window, text = "Группа")
    text_group.insert(0,str(my_list[index][5]))
    comb_status = ttk.Combobox(edit_window, text="Успеваемость", values = [
                "отличник", 
                "хорошист",
                "троешник",
                "на отчисление"])
    comb_status.configure(width=18)
    comb_status.insert(0,str(my_list[index][6]))
    label_status = tkinter.Label(edit_window, text = "Успеваемость")
    button_ok = tkinter.Button(edit_window, text = "Редактировать", command = add_data_to_list)

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

    edit_window.mainloop()

 

