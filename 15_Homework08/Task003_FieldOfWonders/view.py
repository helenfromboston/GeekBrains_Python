def print_menu(n):
    print(f'Приветствую! Выберите номер вопроса от 1 до {n}')

def get_value():
    user_input = input("Ваш выбор: ").lower()
    return user_input

def error_message():
    print("Некорректный ввод")

def q_print(q):
    print(f'Итак, ваш вопрос: {q}')

def hidden_a(a, b):
    return (len(str(a)) * b)

def hidden_a_print(hidden_a):
    print(f'Слово: {hidden_a}')

def winner_print():
    print('ВЫ ВЫИГРАЛИ А-А-АВТОМОБИЛЬ!')