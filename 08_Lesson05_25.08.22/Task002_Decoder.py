# Задача 2. В зоопарк отправили отчёт о новом поступлении зверей с ошибкой,
# в результате которой некоторые данные не расшифровались.
# Расшифруйте данные. Определите, в какой клетке находится лев.
# Номер клетки совпадает с номером строки.

def strip_read_list(user_list):
    new_list = []
    for i in user_list:
        new_list.append(i.strip())
    user_list[:] = []
    user_list.extend(new_list)
    return user_list

def read_file():
    with open("Task002.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
    data = strip_read_list(data)
    return data

func = lambda a: int(a, 2)
animals = read_file()

def decoder(lett, datas):
    step = 6
    count = 1
    for item in datas:
        for i in range(len(item) // 6):
            if i == 0:
                print(count, end=" ")
                count += 1
            tmp = item[0:step]
            print(lett[func(tmp)], end="")
            item = item[step:]
        print()

animals = read_file()
letters = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
decoder(letters, animals)