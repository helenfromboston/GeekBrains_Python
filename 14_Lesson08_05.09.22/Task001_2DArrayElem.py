# Задача 2. Считайте двумерный массив из файла.
# Найдите разницу между вторым максимальным и вторым минимальным элементами массива.

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

new_list = []

for row in range(rows):
    for column in range(columns):
        new_list.append(a[row][column])

new_set = list(set(new_list))
print(new_set)

result = new_set[-2] - new_set[1]
print(f"{new_set[-2]} - {new_set[1]} = {result}")