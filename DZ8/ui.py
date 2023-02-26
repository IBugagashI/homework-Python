from logger import print_data, input_data, filter_data

def interface():
    print('''Выберите режим работы: 
            1 - запись данных
            2 - вывод данных
            3 - поиск данных 
            ''')
    command_namber = int(input('Введите номер режима: '))
    while command_namber < 1 or command_namber > 3:
        print('Введите корректный номер режима!')
        command_namber = int(input('Введите номер режима: '))

    if command_namber == 1:
        input_data()
    elif command_namber == 2:
        print_data()
    elif command_namber == 3:
        print('Введите параметры поиска через ";": ')
        filter_string = input()
        filter_data(filter_string)