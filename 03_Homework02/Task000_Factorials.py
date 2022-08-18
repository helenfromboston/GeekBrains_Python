# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def fact_list(x):
    res = 1
    new_list = []
    for i in range(1, x):
        res = res*i
        new_list.append(res)
    return new_list

N = int(input("Введите число: "))
N = N + 1
print(fact_list(N))