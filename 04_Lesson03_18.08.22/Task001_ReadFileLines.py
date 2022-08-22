# Задача 1. Дан файл, заполненный числами построчно. Считайте файл.
# Выведите все элементы, стоящие на чётных строках, а потом на нечётных.

with open('Task001.txt', 'r') as numbers:
    my_list = numbers.readlines()
    # print(my_list)

for index in range(0, len(my_list), 2):
    print(f"В строке {index} – {my_list[index]}", end="")
print()
for index in range(1, len(my_list), 2):
    print(f"В строке {index} – {my_list[index]}", end="")