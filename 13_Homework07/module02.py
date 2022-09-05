from re import search

def search_name(user_input):
    name_list = []
    with open('Phonebook.txt', encoding = 'UTF-8') as data:
        for line in data.readlines():
            if search(user_input, line.lower()):
                name_list.append(line.removesuffix('\n'))
        if len(name_list) > 0:
            return name_list
        else:
            return "Нет совпадений"