'''
Задача 30: Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''

'''
start = int(input('Укажите первый элемент: '))
dif = int(input('Укажите разность: '))
length = int(input('Укажите колличество элементов: '))
prg = [0] * length
for i in range(len(prg)):
    prg[i] = start
    start += dif
print(*prg)
'''
start = int(input('Укажите первый элемент: '))
dif = int(input('Укажите разность: '))
col = int(input('Укажите колличество элементов: '))
prg = list(range(start, start + dif * col, dif))
print(*prg)