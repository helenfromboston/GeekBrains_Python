# Задача 1. Даны два случайных пятизначных числа.
# Определить, состоят ли они из одних и тех же цифр

list1 = "72126"
list2 = "27624"
numbers_sq = True

for i in list1:
    if list1.count(i) != list2.count(i):
        numbers_sq = False

print("Да" if numbers_sq else "Нет" )