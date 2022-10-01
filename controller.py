import csv

def refresh_list(input_path):
    my_inputlist=[]
    with open (input_path,"r") as data:
    
        reader = csv.reader (data, delimiter=",")
        for item in reader:
            my_inputlist.append(item)
    return my_inputlist
def add_spaces(input_interval):
    s=""
    for i in range(input_interval):
        s += " "
    return s
def format_line(input_list, input_index, list_interval):
    temp_str = ""
    for i in range(len(input_list[input_index])-1):
        temp_str += input_list[input_index][i]+add_spaces(list_interval[i]-len(input_list[input_index][i]))
    temp_str += input_list[input_index][6]
    return(temp_str)
def list_to_file(input_list, input_path): 
    with open (input_path, "w") as data:
        for lin in input_list:
            temp_str=""
            result_str=""
            for wor in lin:
                temp_str+=wor+","
            result_str=temp_str[:-1]
            data.write(result_str+"\n")