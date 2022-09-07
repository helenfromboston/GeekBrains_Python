# Задача 1. В каждой группе учится от 20 до 30 студентов.
# По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка.
# Определите группу с наилучшим средним баллом.

import random
from statistics import mean

rows = 3
class_array = [0] * rows

for i in range(len(class_array)):
    class_array[i] = list(random.randint(1, 5) for i in range(random.randint(20, 30)))

for i in class_array:
    print(i)

grade_list = []

for i in range(len(class_array)):
    grade_list.append(round(mean(class_array[i]), 2))

print(grade_list)

max_grade = max(grade_list)
best_group = grade_list.index(max_grade)

print(f"Группа с наилучшим средним баллом: группа {best_group + 1} ({max_grade})")