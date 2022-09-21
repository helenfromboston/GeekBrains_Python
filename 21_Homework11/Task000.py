# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значениях x значение функции отрицательно.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = 5*(x**2) + 10*x - 30

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y, 'r')
plt.show()

# Ответ: при х от -3,6 до 1,6