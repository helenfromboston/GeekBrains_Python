import telebot
import requests
import datetime

bot = telebot.TeleBot("5626384928:AAHWVNNKJBOkc4OX0SshT2HvGfR5PCDtHMg", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=["text", "sticker"])
def function_name(message):
	# bot.reply_to(message, "This is a message handler")
    text= message.text
    if "привет" in text.lower():
        bot.reply_to(message, f"Привет {message.from_user.first_name}!")
    elif "погода" in text.lower():
        weather = requests.get("https://wttr.in/?0T")
        bot.reply_to(message, weather.text)
    with open('log.txt', 'a', encoding='utf-8') as data:
        data.writelines(message.text + ' ' + str(datetime.datetime.now()) + '\n')