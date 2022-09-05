def new_entry(entry):
    with open('Phonebook.txt', 'a', encoding = 'UTF-8') as data:
        data.write(f"{entry}\n")