# Задача 1. Имеются данные о продаже компьютеров компаний «Ашечка»и «Бэшечка»за последние 6 лет.
# Спрогнозируйте, через сколько лет объёмы продаж этих компаний сравняются

import statistics as stat
import matplotlib.pyplot as m

A = [1743, 1648, 1650, 1622, 1581, 1490]
B = [743, 648, 711, 780, 805, 846]

A_avg_list = []
for i in range(len(A)-1):
    A_avg_list.append(A[i] - A[i+1])

B_avg_list = []
for i in range(len(B)-1):
    B_avg_list.append(B[i] - B[i+1])

A_avg = round(stat.mean(A_avg_list), 0)
B_avg = round(stat.mean(B_avg_list), 0)

A_last = A[5]
B_last = B[5]

for i in range(10):
    d = A_last - A_avg
    A.append(d)
    A_last = A[-1]

for i in range(10):
    d = B_last - B_avg
    B.append(d)
    B_last = B[-1]

m.plot(A, 'r-')
m.plot(B, 'r-')
m.show()
m.subplot(A,)