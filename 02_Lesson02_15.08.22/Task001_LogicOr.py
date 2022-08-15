# Задача 1. Выведите таблицу истинности для выражения ¬X ∨ Y.

def check():
    for x in range(2):
        for y in range(2):
            print(x, y, int(not x or y))

print("x", "y", "¬X ∨ Y")
check()