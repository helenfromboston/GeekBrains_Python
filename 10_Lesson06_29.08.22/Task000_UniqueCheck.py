# Задача 0. Дан список случайных элементов.
# Проверьте, что все его элементы уникальны.

number = [7, 2, 3, 4, 5, 7]
result = set(number)
print('Yes' if len(number) == len(result) else 'No')