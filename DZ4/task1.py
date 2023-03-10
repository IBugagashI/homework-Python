'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

6 12
'''
'''
# условие ввода 3

list_1 = list(map(int, input("Укажите числа для множества 1, через пробел: ").split())) # пользователь вводит сами элементы множеств 1.
list_2 = list(map(int, input("Укажите числа для множества 2, через пробел: ").split())) # пользователь вводит сами элементы множеств 2.
set_list_1 = set(list_1)
set_list_2 = set(list_2)
result = set_list_1.intersection(set_list_2)
print(f"Первый список из {len(list_1)} элементов: {list_1}\nВторой спиосок из {len(list_2)} элементов: {list_2}")
print(f'Их общие элементы: {sorted(result)}')

# условие ввода 2
'''
import random

list_1 = random.choices(range(0, 20), k = int(input("Введите рамер первого множества: ")))
list_2 = random.choices(range(0, 20), k = int(input("Введите рамер второго множества: ")))
set_list_1 = set(list_1)
set_list_2 = set(list_2)
result = set_list_1.intersection(set_list_2)
print(f"Первый список из {len(list_1)} элементов: {list_1}\nВторой спиосок из {len(list_2)} элементов: {list_2}")
print(f"Их общие элементы: {sorted(result)}")


'''
# условие ввода 1

n, m = int(input("Введите рамер первого множества: ")), int(input("Введите рамер второго множества: ")) # Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
list_1 = [0] * n
list_2 = [0] * m
for i in range(n):    
    list_1[i] = int(input(f'Введите {i + 1} элемент первого множемножества: ')) # пользователь вводит сами элементы множеств 1.
for i in range(m):
    list_2[i] = int(input(f'Введите {i + 1} элемент второго множемножества: ')) # пользователь вводит сами элементы множеств 2.
set_list_1 = set(list_1)
set_list_2 = set(list_2)
result = set_list_1.intersection(set_list_2)
print(f"Первый список из {len(list_1)} элементов: {list_1}\nВторой спиосок из {len(list_2)} элементов: {list_2}")
print(f'Их общие элементы: {sorted(result)}')

'''