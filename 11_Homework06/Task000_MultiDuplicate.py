# Задача 1. Дано натуральное число N.
# Найдите значение выражения: N + NN + NNN.
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

N = 132
N = str(N)
result = int(N) + int(N*2) + int(N*3)
print(f"N = {N}: {N} + {N*2} + {N*3} = {result}")