# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def check():
    print("x", "y", "z", "1", "2", "3")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(x, y, z, int(x and y), int(
                    not (x and y)), int(not (x and y) or z))


check()

# Для вывода печати:
# 1 - X ∧ Y
# 2 - ¬(X ∧ Y)
# 3 - ¬(X ∧ Y) ∨ Z