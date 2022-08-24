# Задача 0. Создайте файл random.txt. Запишите в него 10 случайных чисел.
import random

list = []

for i in range(10):
    list.append(random.randint(1, 10))

with open('random.txt', 'w', encoding = 'UTF-8') as data:
    data.writelines(str(list))