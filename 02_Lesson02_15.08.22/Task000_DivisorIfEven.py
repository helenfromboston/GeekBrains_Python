# Задача 0. Дано число N. Найти все его делители. Для каждого делителя укажите, четный он или нечетный

def check_even(x):
    if x % 2 == 0:
        return "– четное"
    else:
        return "– нечетное"


# def find_div(x):
    values = range(1, x+1)
    for i in values:
        if x % i == 0:
            print(i, check_even(i))

def find_div(x):
    values = range(1, x+1)
    result = []
    for i in values:
        if x % i == 0:
            result.append(i)

number = int(input("Введите число: "))
# find_div(number)

divisors = find_div(number)
for i in divisors:
    print(i, check_even(i))