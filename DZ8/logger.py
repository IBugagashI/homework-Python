import os

from data_create import name_data, surname_data, phone_data, adress_data

file_name = 'data.txt'
file_name2 = 'data2.txt'

def print_data():
    if os.path.exists(file_name):
        print('Вывод данных из файла: ')
        with open(file_name, 'r', encoding= 'utf-8') as file:
            list_data = file.readlines()
            for element in list_data:
                print(element)
    else:
        print('Файл отсутствует!')

def input_data():
    print('Введите данные для записи в фаил: ')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    with open(file_name, 'a', encoding= 'utf-8') as file:
        file.write(f'{name};{surname};{phone};{adress}\n')

def filter_data(filter_string):
    with open(file_name, 'r', encoding= 'utf-8') as file:
        list_data = file.readlines()
        if ';' in filter_string:
            list_filter = filter_string.split(';')
        else:
            list_filter = [filter_string]
        is_found = False
        for element in list_data:
            temp_record = element.split(';')
            count = 0
            for record in temp_record:
                for element_filter in list_filter:
                    if element_filter.lower() in record.lower() and len(element_filter.lower()) == len(record.lower()):
                        count += 1
            if count == len(list_filter):
                print(element)
                is_found = True
    if not is_found:
        print('Запись не найдена!')

def editing_data(meaning, new_sense):
    with open(file_name, 'r', encoding= 'utf-8') as file:
        old_str = file.readlines()

    with open(file_name, 'w', encoding= 'utf-8') as file:
        for element in old_str:
            if meaning in element:
                element = element.replace(meaning, new_sense, 1)
                file.write(element)
            else:
                file.write(element)

def delet_data():
    with open(file_name, 'r', encoding='utf-8') as file:
        old_str = file.readlines()        

    
    # with open(file_name, 'w', encoding= 'utf-8') as file:
    #     for element in old_data:
    #         file.write((element.replace(meaning, new_sense)).split(';') + '\n')