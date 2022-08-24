# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из букв и чисел.
# Создайте скрипт для сохранения пароля в файл password.txt.

import random

dict = 'abcdefghijklmnopkrstuvwxyz0123456789!@#$%^&*()_+|'
length = len(dict) - 1

L = int(input())

cat = ""
for i in range(L):
    index_list = random.randint(0, length)
    cat += dict[index_list]

print(cat)