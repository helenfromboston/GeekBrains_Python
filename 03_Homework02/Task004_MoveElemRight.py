# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def fill_list(x, y):
    list_to_fill = []
    for i in range(x, y):
        list_to_fill.append(i)
    return list_to_fill

def move_list(list_to_move, z):
    list_to_move = list_to_move[z:] + list_to_move[:z]
    return list_to_move

N = int(input("Введите число N: "))
M = -abs(N)
N = N + 1

list_one = fill_list(M, N)
print(list_one)

list_two = move_list(list_one, -2)
print(list_two)

