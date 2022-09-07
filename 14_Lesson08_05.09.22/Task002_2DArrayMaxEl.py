# Задача 4. Дан двумерный массив.
# Определите номер строки и столбца,
# в котором находится максимальный элемент.

from operator import index
import random
rows = 5
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

print(new_list)
max = max(new_list)
max_index = new_list.index(max)
print(max_index)
print(max)

max_index_row = max_index // rows
max_index_column = max_index % columns

print(f"Максимальный элемент в строке {max_index_row + 1}, в столбце {max_index_column + 1}")