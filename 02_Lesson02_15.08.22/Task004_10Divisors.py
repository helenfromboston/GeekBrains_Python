# Задача 4. Найдите все числа до 10000, у которых количество делителей равно 10.

# def count_div(x):
#     count = 0
#     for i in range(1, x+1):
#         if x % i == 0:
#             count += 1
#     return count

# for i in range(1, 10001):
#     if count_div(i) == 10:
#         print(i)

def count_div(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count

def find_max_div():
    new_list = []
    for i in range(1, 10001):
        if count_div(i) == 10:
            new_list.append(i)
    return new_list

print(find_max_div())
