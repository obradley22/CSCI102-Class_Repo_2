# Paris Porter Bradley
# ​CSCI 102 – Section E
# Week 12 - Part A

def PrintOutput(string):
    return print("OUTPUT " + str(string))

def LoadFile(file):
    with open(file) as file_text:
        lines = file_text.readlines()
    return linesgit 

def UpdateString(my_string, letter, index):
    my_list = []
    for i in my_string:
        my_list.append(i)
    my_list[index]=letter
    new_string="".join(my_list)
    return print("OUTPUT",new_string)


def FindWordCount(list1,string):
    count=0
    for i in list1:
        if string in i:
            count+=1
    return count
