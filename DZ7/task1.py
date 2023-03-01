'''
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод:
пара-ра-рам рам-пам-папам па-ра-па-дам 

Вывод:
Парам пам-пам
'''
'''
# №1

def vinniу (poem):
    vowels = ['А','О','У','Ы','Э','Е','Ё','И','Ю','Я']
    poem = poem.upper().split()
    score = []
    for element in poem:
        count = 0
        for letter in element:
            if letter in vowels:
                count += 1
        score.append(count)        

    return "Парам пам-пам" if len(set(score)) == 1 else "Пам парам"

print(vinniу(input('Введите текст стиха: ')))

'''
# №2

vowels = 'АОУЫЭЕЁИЮЯ'
# poem = input('Введите текст стиха: ').upper().split()
# count = [sum(i in vowels for i in x) for x in poem]
# print(*count)
# print("Парам пам-пам" if len(set(count)) == 1 else "Пам парам")