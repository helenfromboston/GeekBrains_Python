# Задача 2. Актёров разделили на списки по трём качествам
# «умные», «красивые», «сильные». На главную роль нужен актёр
# обладающий всеми тремя качествами. Определите, сколько есть
# претендентов на главную роль. Списки актёров поместите в
# соответствующие файлы.

# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад


def find_actor():
    handsome = ['Илья', 'Федор', 'Семен', 'Олег', 'Лев', 'Антон', 'Артем', 'Боря', 'Стас', 'Марк', 'Ян', 'Влад']
    smart = ['Илья', 'Георгий', 'Лев', 'Демьян', 'Антон', 'Владислав', 'Боря', 'Стас', 'Марк', 'Влад']
    strong = ['Федор', 'Георгий', 'Олег', 'Демьян', 'Артем', 'Елисей', 'Боря', 'Стас', 'Влад']
    actors = []
    for h in handsome:
        for s in smart:
            for st in strong:
                if h in smart and h in strong and h not in actors:
                    actors.append(h)
    return actors


def write_file(list_actor):
    with open("actors.txt", 'a', encoding="utf-8") as file:
        file.write(str(list_actor))


actors_list = find_actor()
print(actors_list)
write_file(actors_list)


def create_set():
    handsome = {'Илья', 'Федор', 'Семен', 'Олег', 'Лев', 'Антон', 'Артем', 'Боря', 'Стас', 'Марк', 'Ян', 'Влад'}
    smart = {'Илья', 'Георгий', 'Лев', 'Демьян', 'Антон', 'Владислав', 'Боря', 'Стас', 'Марк', 'Влад'}
    strong = {'Федор', 'Георгий', 'Олег', 'Демьян', 'Артем', 'Елисей', 'Боря', 'Стас', 'Влад'}
    actors = handsome.intersection(smart).intersection(strong)
    return actors


actors_list = create_set()
print(create_set())
write_file(actors_list)