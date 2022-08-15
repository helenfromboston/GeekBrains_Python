# Задача 2. Напишите программу, в которой пользователь будет задавать две строки,
# а программа определять количество вхождений одной строки в другой.
# « qwe » « qwertyqwe » > 2

def find_str(string: str, second_string: str):
    count = 0
    for i in range(len(second_string)):
        if second_string[i:3+i] == string:
            count += 1
    return count


user_string = 'qwe'
second_string = 'qwertyqwe'

print(find_str(user_string, second_string))