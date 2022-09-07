# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк
# превосходит сумму главной диагонали матрицы.

import random

rows = columns = 4
square_array = [0] * rows

for i in range(len(square_array)):
    square_array[i] = list(random.randint(10, 50) for i in range(columns))

for i in square_array:
    print(i)

diagonal = 0
for i in range(rows):
    for j in range(columns):
        if i == j:
            diagonal += square_array[i][j]

print(f"Сумма главной диагонали матрицы: {diagonal}")

sum_list = []
for i in square_array:
   sum_list.append(sum(i))

print(f"Сумма элементов строк: {sum_list}")

sum_num = []
for i in sum_list:
    if i > diagonal:
        sum_num.append(sum_list.index(i))

if len(sum_num) == 0:
    print("Нет строк с суммой элементов, превосходящей сумму главной диагонали матрицы")
else:
    print(f"Сумма элементов {sum_num} строк(и) превосходит сумму главной диагонали матрицы")