# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5.
# Заполните список случайным образом числами от 1 до 100.

import random

my_list = list(random.randint(1, 100) for i in range(15))
anonim = list(filter(lambda x: not x%5, my_list))
print(my_list)
print(anonim)