def show_phonebook():
    with open('Phonebook.txt', encoding = 'UTF-8') as data:
        phonebook = data.read()
    return phonebook