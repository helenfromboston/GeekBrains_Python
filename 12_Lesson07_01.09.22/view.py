def printMainMenu():
    print("Выберите пункт меню:\n \
    1 - сколько дней осталось до Нового Года\n \
    2 - сколько дней прошло в этом году")

def printResult(result, title):
    print(f'{result} {title}')

def getValues():
    user_input = input("Напишите ответ: ")
    return user_input

def errorMessage():
    print("Некорректный ввод")