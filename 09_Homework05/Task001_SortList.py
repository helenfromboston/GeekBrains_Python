# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# Комментарий: сделала возрастающую последовательность относительно первого элемента.
# Как сделать с рандомным выбором элементов пока не дошло :(

import random

def list_sort_ascend(user_list):
    new_list = []
    new_list.append(user_list[0])
    for j in range(len(user_list)):
        if user_list[j] in new_list:
            continue
        elif user_list[j] > user_list[0] and user_list[j] > new_list[len(new_list)-1]:
            new_list.append(user_list[j])
    return new_list

my_list = list(random.randint(1, 30) for i in range(10))
print(my_list)

result = list_sort_ascend(my_list)
print(result)