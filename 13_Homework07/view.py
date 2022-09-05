def print_menu():
    print("Выберите действие:\n \
           0 - выход\n \
           1 - новая запись\n \
           2 - поиск по имени\n \
           3 - вывод всего справочника\n \
           4 - экспорт справочника в формат html")

def get_value():
    user_input = input("Ваш выбор: ")
    return user_input

def get_new_entry():
    new_name = input("Введите новое ФИО: ")
    new_phone = input("Введите номер телефона: ")
    entry = (f"{new_name} - {new_phone}")
    return entry

def get_name_search():
    user_input = input("Введите искомое имя: ").lower()
    return user_input

def print_module(entry):
    print(entry)

def error_message():
    print("Некорректный ввод")

def done_message():
    print("Сделано!")