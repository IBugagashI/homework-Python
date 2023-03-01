def name_data():
    name = input('Введите ваше имя: ')
    return name

def surname_data():
    surname = input('Введите ваше фамилию: ')
    return surname

def phone_data():
    phone = input('Введите ваш телефон: ')
    return phone

def adress_data():
    adress = input('Введите ваш адрес: ')
    return adress

def set_value():
    meaning = input('Введите искомый элемент: ')
    return meaning

# def read_data(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         old_str = file.readlines()        
#     with open(file_name, 'w', encoding= 'utf-8') as file:
#         for element in old_str:
#             return element