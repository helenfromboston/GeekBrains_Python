import telebot
import requests
import datetime

bot = telebot.TeleBot("5626384928:AAHWVNNKJBOkc4OX0SshT2HvGfR5PCDtHMg", parse_mode=None)

@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id, 'Напишите Ваш вопрос технической поддержке')


@bot.message_handler(content_types=["text", "sticker"])
def add_q(message):
    info = f"{message.from_user.id}: {message.text}\n"
    with open('log.txt', 'a', encoding='utf-8') as data:
        data.writelines(info)
    bot.send_message(message.chat.id, 'Обращение записано. Ожидайте ответа')

q_tuples = []

def q_extract_all():
    global q_tuples
    q_list = []
    with open('log.txt', encoding='UTF-8') as data:
        for i in data.readlines():
            q_list.append(i.removesuffix('\n'))
    for i in q_list:
        q_tuples.append(tuple(i.split(': ')))
    return q_tuples


def q_extract(value):
    qs = q_extract_all()
    return qs[(int(value)-1)]

qa_list = []

def reply():
    q_num = int(input("Выберите номер вопроса: "))
    if q_num in qa_list:
        print("На данный вопрос уже был отправлен ответ")
        ready()
    else:
        q = q_extract(q_num)
        user = q[0]
        q = q[1]
        print(f"Вопрос пользователя: {q}")
        reply = input('Введите ответ пользователю: ')
        bot.send_message(int(user), f'Ответ на Ваш вопрос\n"{q}":\n{reply}')
        qa_list.append(q_num)


def ready():
    r = input("Вывести список вопросов (0) или Хотите ответить на конкретный вопрос (1): ")
    if r == "0":
        qs = q_extract_all()
        num = 1
        for item in range(len(qs)):
            print(f"{num}. {qs[item][1]}")
            num += 1
        ready()
    elif r == "1":
        reply()
        ready()
    else:
        print("???")

ready()
bot.polling(none_stop=True, interval=0)