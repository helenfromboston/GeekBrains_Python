# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.

def strip_read_list(user_list):
    new_list = []
    for i in user_list:
        new_list.append(i.strip())
    user_list[:] = []
    user_list.extend(new_list)
    return user_list

def first_letter_search(user_list, letter: str):
    letter_list = []
    for i in range(len(user_list)):
        if user_list[i][0] == letter:
            letter_list.append(user_list[i])
    return letter_list

with open('Task001.txt', 'r', encoding = 'UTF-8', ) as data:
    read_list = data.readlines()

strip_read_list(read_list)
result = first_letter_search(read_list, "а")
print(result)