
from optparse import Values
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import color
import csv
from numpy import size
import controller
path = "pb.csv"
my_list = controller.refresh_list(path)
result_list = my_list
new_cont = ("","")
temp_index_list = [i for i in range(len(my_list))]
def find_wind():
    def find_string():
        index_list=[i for i in range (len(my_list))]
        result_list=controller.refresh_list(path)
        lbox.delete(0,END)
        if str(text_name.get()) != '':
            for i in range(len(result_list)):
                if (result_list[i][0] != str(text_name.get())) & (i in index_list):
                    index_list.remove(i)
                if index_list == []:
                    break
        if str(text_surname.get()) != '':
            for i in range(len(result_list)):
                if (result_list[i][1] != str(text_surname.get())) & (i in index_list):
                    index_list.remove(i)
                if index_list == []:
                    break
        if str(comb_sex.get()) != '':
            for i in range(len(result_list)):
                if (result_list[i][2] != str(comb_sex.get())) & (i in index_list):
                    index_list.remove(i)
                if index_list==[]:
                    break
        if str(text_phone.get()) != '':
            for i in range(len(result_list)):
                if (result_list[i][3] != str(text_phone.get())) :
                    index_list.remove(i)
                if index_list == []:
                    break             
        if str(comb_course.get()) != '':
            for i in range(len(result_list)):
                if (result_list[i][4] != str(comb_course.get())) & (i in index_list):
                    index_list.remove(i)
                if index_list == []:
                    break             
        if str(text_group.get()) != '':
            for i in range(len(result_list)):
                if (result_list[i][5] != str(text_group.get())) & (i in index_list):
                    index_list.remove(i)
                if index_list == []:
                    break             
        if str(comb_status.get()) != '':
            for i in range(len(result_list)):
                if (result_list[i][6] != str(comb_status.get())) & (i in index_list):
                    index_list.remove(i)
                if index_list == []:
                    break             
        if index_list != []:
            for i in index_list:
                lbox.insert(0, my_list[i])
        else:
            lbox.insert(0, "по Вашему запросу ничего не найдено")

    def close_btn():
        find_window.destroy()

    find_window = Tk()
    find_window.geometry("750x400")
    find_window.title("Поиск")
    labelName = tkinter.Label(find_window, text = "Имя")
    text_name = tkinter.Entry(find_window, text ="Имя")
    labelPhone = tkinter.Label(find_window, text = "Телефон")
    text_surname = tkinter.Entry(find_window, text ="Фамилия")
    label_surname = tkinter.Label(find_window, text = "Фамилия")
    text_phone = tkinter.Entry(find_window)
    comb_sex=ttk.Combobox(find_window, text="пол", values = [
                                    "",
                                    "М", 
                                    "Ж"])
    comb_sex.configure(width=4)
    label_sex=tkinter.Label(find_window, text = "Пол")
    comb_course=ttk.Combobox(find_window, text="курс", values = [
                                "",
                                "1", 
                                "2",
                                "3",
                                "4",
                                "5"])
    comb_course.configure(width=4)
    label_course=tkinter.Label(find_window, text = "Курс")
    text_group = tkinter.Entry(find_window, text ="Группа")
    label_group = tkinter.Label(find_window, text = "Группа")
    comb_status=ttk.Combobox(find_window, text="Успеваемость", values = [
                "",
                "отличник", 
                "хорошист",
                "троешник",
                "на отчисление"])
    comb_status.configure(width=18)
    label_status=tkinter.Label(find_window, text = "Успеваемость")
    button_find = tkinter.Button(find_window, text = "Найти контакт",width=12, command=find_string)
    button_close = tkinter.Button(find_window, text = "Закрыть",width=12, command=close_btn)
    lbox = Listbox(find_window, width=70, height=7, bg="white", fg="blue")
    
    lbox.place(x=50, y=250)
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
    button_find.place(x=200, y=180)
    button_close.place(x=390,y=180)
    comb_status.place(x=510, y=120)
    label_status.place(x=510, y=90)
    
    find_window.mainloop()

 

