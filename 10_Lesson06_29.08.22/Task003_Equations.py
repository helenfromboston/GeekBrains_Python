# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

user_input = input('Введите математическое выражение: ')
print(f"{user_input} = {eval(user_input)}")