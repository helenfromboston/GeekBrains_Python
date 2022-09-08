def q_extract(value):
    q_list = []
    with open('Questions.txt', encoding='UTF-8') as data:
        for i in data.readlines():
            q_list.append(i.removesuffix('\n'))
    q_tuples = []
    for i in q_list:
        q_tuples.append(tuple(i.split('? ')))
    return q_tuples[(value-1)][0]