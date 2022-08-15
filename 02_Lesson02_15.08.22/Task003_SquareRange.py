# Задача 3. Дано число N. Заполните список длиной N элементами
# N = 5 > [ 1, -3, 9, -27, 81]

N = int(input("Введите N: "))
list = [0]*N
for i in range(N):
    list[i] = (-3)**i
print(list)