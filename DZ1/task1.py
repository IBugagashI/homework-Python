# Задача 2: Найдите сумму цифр трехзначного числа. 
number = input('Ведите число: ')
sum = 0
for i in range(len(number)):
    sum += int(number[i])
print(f"Сумма отдельных чисел введённого числа : {sum}")