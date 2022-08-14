# Напишите программу, которая находит наибольшее и наименьшее число из списка значений

# высококлассное решение
my_list = [int(i) for i in input('Введите числа массива: ').split()]
print(f'Максимальное число из списка = {max(my_list)}, минимальное число из списка = {min(my_list)}')

list = [1, 4, -1, 0, 8, -5, 3]
min = list[0]
max = list[0]
for i in list:
    if i > max:
        max = i
    elif i < min:
        min = i
print(max)
print(min)
