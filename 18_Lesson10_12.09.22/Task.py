import telebot
import requests
import datetime

bot = telebot.TeleBot("5626384928:AAHWVNNKJBOkc4OX0SshT2HvGfR5PCDtHMg", parse_mode=None)
# You can set parse_mode by default. HTML or MARKDOWN
def function_name(message):
    text = message.text
    print(f"{message.from_user.first_name} {message.from_user.last_name}: {text}")

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(content_types=["text", "sticker"])
# def function_name(message):
# 	# bot.reply_to(message, "This is a message handler")
#     text= message.text
#     if "привет" in text.lower():
#         bot.reply_to(message, f"Привет {message.from_user.first_name}!")
#     elif "погода" in text.lower():
#         weather = requests.get("https://wttr.in/?0T")
#         bot.reply_to(message, weather.text)
#     with open('log.txt', 'a', encoding='utf-8') as data:
#         data.writelines(message.text + ' ' + str(datetime.datetime.now()) + '\n')

@bot.message_handler(commands=['registration'])
def func(message):
    data = str(message.from_user.id) + '\n'
    with open("log_id.txt", "r+", encoding='utf-8') as file:
        text_id = file.readlines()
    # with open("log_id.txt", "a", encoding='utf-8') as file:
        if data not in text_id:
            file.writelines(data)
            bot.reply_to(message, "Регистрация прошла успешно!")
        else:
            bot.reply_to(message, "Ваша запись уже зарегистрирована!")

@bot.message_handler(commands=['notify'])
def notify(message):
    with open("log_id.txt", "r+", encoding='utf-8') as data:
        users = data.read().removesuffix('\n')
    for id in users:
        bot.send_message(int(id), '(づ￣ 3￣)づ')

bot.polling(none_stop=True, interval=0)