# Задача 0. Создайте скрипт func и функцию чтения последней строки файла. Вызовите её из скрипта example.

def read_last_line(file):
    with open(file, encoding='UTF-8') as my_file:
        last_line = my_file.readlines()
        print(last_line[-1])