'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2**k
), не превосходящие числа N.

10 -> 1 2 4 8
'''
number = int(input('Введите число N: '))
k = 0
print(f"Целые степени двойки до {number}: ", end='')
while number > (2**k):
    print(2**k,  end=' ')
    k += 1