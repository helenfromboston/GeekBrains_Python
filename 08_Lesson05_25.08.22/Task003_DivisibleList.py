# Задача 4. Задайте список из 15 случайных чисел.
# Выведите все пары кратных чисел из этого списка.

import random

my_list = list(random.randint(1, 100) for i in range(5))

print(my_list)

# for item in my_list:
#     for i in my_list:
#         if not i % item and item != i:
#             print(i, item)

my_list = list(filter(lambda x: not x % 2, my_list))

print(my_list)