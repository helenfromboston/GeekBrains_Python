# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def check(string_one: str, string_two: str):
    count = 0
    for i in range(len(string_one)):
        for j in range(len(string_two)):
            if string_one[i] == string_two[j]:
                count += 1
        print(f"{string_one[i]} – {count}")
        count = 0

user_str_one = "one"
user_str_two = "onetwonine"
check(user_str_one, user_str_two)