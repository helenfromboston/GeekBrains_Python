import datetime
import re
import random
import telebot
import requests

bot = telebot.TeleBot('5703927521:AAG4acGXZHxvhlwpGO6FID7BSFhA2bNrUEw', parse_mode=None)

def log(message):
    with open('log.txt', 'a', encoding='utf-8') as data:
        data.writelines(message.text + ' ' + str(datetime.datetime.now()) + '\n')


def start_msg(message):
    bot.send_message(message.chat.id, f'Hi {message.from_user.first_name}! Welcome!\n'+
    'Choose your destiny by hitting / to see what commands you can use here')


def hello_msg(message):
    bot.send_message(message.chat.id, f'Hi {message.from_user.first_name}!')


def cat(message):
    bot.send_sticker(message.chat.id, random_cat())


def weather_msg(message):
    weather = requests.get("https://wttr.in/?0T")
    bot.send_message(message.chat.id, weather.text)


def random_cat():
    cat_ids = ['CAACAgIAAxkBAAEX9KhjHO5Z0vU1g4DvLHQCqFiHufv3OQAChwUAAiMFDQABE-Nhq6tbXOMpBA',
               'CAACAgIAAxkBAAEX9NdjHPOzfzF63cUVLB9So3NCjSH72wACQQUAAiMFDQABH6kfFQphJ-spBA',
               'CAACAgIAAxkBAAEX9N9jHPP2fbzHJidlFejedmEJhsiu1gACewUAAiMFDQABFvB5J76cyUcpBA',
               'CAACAgIAAxkBAAEX9ONjHPQbO959QfIbYnkjfeqV07dsWwACUAUAAiMFDQABSHMtZmr4rZ4pBA']
    return random.choice(cat_ids)


def math_msg(message):
    equation = message.text.replace('/math', '')
    eq_result = "".join(equation.split())
    if re.match('^([-+]?([(]?[0-9][)]?[+-/*]?))*$', eq_result):
        try:
            bot.send_message(message.chat.id,f"{equation} = {eval(eq_result)}")
        except:
            bot.send_message(message.chat.id,'Ooops error calculating')
    else:
            bot.send_message(message.chat.id,'Wrong pattern')


game_on = False
def guess_game(message):
    global my_number
    global game_on
    game_on = True
    my_number = random.randint(1, 1000)
    invite = bot.send_message(message.chat.id, "Let's play a guessing game! Guess the number I think about from 1 to 1000")


def guess_check(message, my_number):
    global game_on
    guess = int(message.text)
    if guess > 1000:
        bot.send_message(message.chat.id, "My number is lower than 1000")
    elif guess > my_number:
        bot.send_message(message.chat.id, "Lower!")
        game_on = True
    elif guess < my_number:
        bot.send_message(message.chat.id, "Higher!")
        game_on = True
    elif guess == my_number:
        bot.send_message(message.chat.id, "Yay, you got it, that was my number!")
        game_on = False
    else:
        bot.send_message(message.chat.id, "What even is this?")
        game_on = True


@bot.message_handler(content_types=["text", "sticker"])
def main_function(message):
    log(message)
    global game_on
    global my_number
    text = message.text
    if 'start' in text.lower():
        start_msg(message)
    elif 'hello' in text.lower():
        hello_msg(message)
    elif 'cat' in text.lower() :
        cat(message)
    elif 'math' in text.lower():
        invite = bot.send_message(message.chat.id, 'Alright, hit me up with your maths!')
        bot.register_next_step_handler(invite, math_msg)
    elif 'weather' in text.lower():
        weather_msg(message)
    elif text.isdigit() and game_on is True:
        guess_check(message, my_number)
    elif 'game' in text.lower() and game_on is False:
        guess_game(message)


print('server start')
bot.polling(none_stop=True, interval=0)