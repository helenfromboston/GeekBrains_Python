# Задача 3. Найдите все простые несократимые дроби,
# лежащие между 0 и 1, знаменатель которых не превышает 11.

import math

fraction_list = []
for i in range(1, 12):
    for j in range(1, 12):
        if i/j >= 1:
            continue
        elif math.gcd(i, j) == 1:
            fraction_list.append(f"{i}/{j}")
            # print(f"{i}/{j}", end=", ")

print(fraction_list)
