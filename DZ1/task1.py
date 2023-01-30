# Задача 2: Найдите сумму цифр трехзначного числа. 

# Решение 1

number = int(input('Ведите число: '))
x = number // 100
y = number % 10
z = (number % 100) // 10
print('Сумма отдельных чисел введённого числа = ', x + y + z)

'''
# Решение 2

number = input('Ведите число: ')
sum = 0
for i in range(len(number)):
    sum += int(number[i])
print(f"Сумма отдельных чисел введённого числа : {sum}")
'''