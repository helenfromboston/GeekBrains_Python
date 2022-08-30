# Задача 3. Имеется информация о том, телефонами каких компаний сейчас торгуют магазины.
# Определите те компании, чьи телефоны присутствуют в каждом магазине.

with open("Task002.txt", encoding='utf-8') as phone:
    data = phone.readlines()
print(data)
store = []
for i in range(1, len(data), 2):
    store.append((data[i][:-1]).split(", "))
print(store)
assortment = set(store[0])

for i in store:
    print(i)
    assortment = set(i).intersection(assortment)

print(assortment)
