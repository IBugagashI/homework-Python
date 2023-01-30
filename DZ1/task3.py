'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
'''

'''
Решение 1

number = int(input("Введите номер билета: "))
digit1 = number // 10**5
digit2 = (number % 10**5) // 10 ** 4
digit3 = (number % 10**4) // 10 ** 3
digit4 = (number % 10**3) // 10 ** 2
digit5 = (number % 10**2) // 10
digit6 = number % 10
print(f"Ваш билет {number}")
if (digit1 + digit2 + digit3) == (digit4 + digit5 + digit6):
    print("YES")
else:
    print("NO")
'''

# Решение 2
number = input("Введите номер билета: ")
half1 = int(number[0]) + int(number[1]) + int(number[2])
half2 = int(number[3]) + int(number[4]) + int(number[5])
print(f"Ваш билет {number}")
if half1 == half2:
    print("YES")
else:
    print("NO")


