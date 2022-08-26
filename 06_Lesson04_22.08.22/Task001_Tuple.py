# Задача 1 . Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в кортеже по заданному индексу.

import random

my_tuple = tuple(random.randint(1, 10) for i in range(5))
print(my_tuple)
# my_tuple_1 = ([1, 2, 33], [3, 2, 1])
# my_tuple_1[2] = 64
# print(my_tuple_1[2])
# print(my_tuple_1)

el_index = 1

my_list = list(my_tuple)

my_list[el_index] = random.randint(1, 10)
my_tuple = tuple(my_list)
print(my_tuple)