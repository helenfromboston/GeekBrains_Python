# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 5x^2 + 3x
# 3x^2 + x + 8
# 8x^2 + 4x + 8

# Комментарий: у меня получилось придумать какой-то код для двучленов
# заданного формата. Лучше ничего в голову не пришло :(

with open('Task003_01.txt', 'r', encoding='UTF-8') as data:
    str1 = data.read()

with open('Task003_02.txt', 'r', encoding='UTF-8') as data:
    str2 = data.read()

list1 = []
list2 = []

for index in range(len(str1)):
    if str1[index] == 'x':
        if not str1[index-1].isdigit():
            list1.append('1')
        list1.append(str1[index-1])
if str1[-1].isdigit():
    list1[-1] = str1[-1]
elif not str1[-1].isdigit():
    list1.append('0')

for index in range(len(str2)):
    if str2[index] == 'x':
        if not str2[index-1].isdigit():
            list2.append('1')
        list2.append(str2[index-1])
if str2[-1].isdigit():
    list2[-1] = str2[-1]
elif not str2[-1].isdigit():
    list2.append('0')

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

print(str1)
print(str2)

print(
    f"Результат: {list1[0]+list2[0]}x^2 + {list1[1]+list2[1]}x + {list1[2]+list2[2]}")