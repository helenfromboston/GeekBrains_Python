def q_num():
    q_list = []
    with open('Questions.txt', encoding='UTF-8') as data:
        for i in data.readlines():
            q_list.append(i.removesuffix('\n'))
    return len(q_list)