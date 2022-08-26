# Задача 3. : Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов.
# Удалите из списка дубликаты уже имеющихся элементов.
# [1, 2, 9, 5, 2, 18, 3, 5, 13, 2] > [1, 2, 9, 5, 18, 3, 13]

import random

my_list = list(random.randint(1, 20) for i in range(10))
print(my_list)

new_set = set(my_list)
print(new_set)

new_list = list(new_set)
print(new_list)