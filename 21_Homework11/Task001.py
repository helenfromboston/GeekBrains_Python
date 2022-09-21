# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома
# и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом.
# Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import random
import matplotlib.pyplot as plt
import numpy as np

house_sq = [random.randint(100, 300) for i in range(15)]
house_pr = [random.randint(3000000, 20000000) for i in range(15)]

# print(house_sq)

hourse_sq_pr = []
for i in range(len(house_sq)):
    hourse_sq_pr.append(round(house_pr[i]/house_sq[i], 2))

# print(hourse_sq_pr)

house_match_index = []
for i in range(len(hourse_sq_pr)):
    if hourse_sq_pr[i] < 50000:
        house_match_index.append(i)

# print(house_match_index)

house_match = []
for i in range(len(house_match_index)):
    house_match.append(house_sq[house_match_index[i]])

house_match.sort()

for i in range(len(house_match)):
    house_match[i] = str(f'Дом № {house_sq.index(house_match[i]) + 1}, ')\
         + str(f'площадь {house_match[i]} кв.м, ')\
         + str(f'стоимость кв.м {"{:,.2f}".format(hourse_sq_pr[house_match_index[i]])} руб.')

print(f"Подходящие дома: ")
for i in house_match:
    print(i)

x = np.linspace(0, 15, 17)
y = x + 50000
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.bar(range(1, 16), hourse_sq_pr)
plt.plot(y, 'r')
plt.show()