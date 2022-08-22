# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

def Fibonacci_list(user_list):
    for i in range(len(user_list)):
        if i == 0:
            user_list[i] = 0
        elif i == 1:
            user_list[i] = 1
        else:
            user_list[i] = user_list[i-1]+user_list[i-2]
    return user_list

N = int(input("Введите число: "))
my_list = [0]*N

with open('Task000.txt', 'w') as data:
    data.write(f'{Fibonacci_list(my_list)}')