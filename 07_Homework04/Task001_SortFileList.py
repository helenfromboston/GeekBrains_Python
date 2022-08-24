# Задача 2. В первой строке файла находится информация об ассортименте мороженного,
# во второй - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

def strip_read_list(user_list):
    new_list = []
    for i in user_list:
        new_list.append(i.strip())
    user_list[:] = []
    user_list.extend(new_list)
    return user_list

icecream_list = []
stock_list = []

with open('Task001_File.txt', 'r', encoding='UTF-8') as data:
    for line in data.readlines(1):
        for word in line.split(', '):
            icecream_list.append(word)
    for line in data.readlines(2):
        for word in line.split(', '):
            stock_list.append(word)

strip_read_list(icecream_list)
icecream_set = set(icecream_list)
stock_set = set(stock_list)
print(f"1. {icecream_set}")
print(f"2. {stock_set}")

result = icecream_set.difference(stock_set)

if result == set():
    print("Всё в наличии")
else:
    print(f"Закончилось: {result}")