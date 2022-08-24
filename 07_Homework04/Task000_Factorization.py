# Задача 1. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

def check_prime_factors(number):
    num = number + 1
    prime_list = []
    for n in range(2, num):
        while not number % n:
            number = int(number / n)
            prime_list.append(n)
    return prime_list

N = 60
print(check_prime_factors(N))