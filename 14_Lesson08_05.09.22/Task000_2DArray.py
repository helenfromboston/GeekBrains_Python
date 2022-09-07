# Задача 1 . Задайте двумерный массив случайных чисел размером 4х5.
# Случайные числа не должны повторяться. Запишите массив в txt файл.

import random
rows = 4
columns = 5
a = [0] * rows
used = [0]

for i in range(len(a)):
    a[i] = list(0 for i in range(columns))

for i in range(rows):
    for j in range(columns):
        number = 0
        while number in used:
            number = random.randint(1, 100)
        a[i][j] = number
        used.append(number)

for i in a:
    print(i)