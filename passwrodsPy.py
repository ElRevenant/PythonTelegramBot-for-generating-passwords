import telebot
import random

bot = telebot.TeleBot('YOUR_TOKEN')

easy_password_symbols = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
]

mid_password_symbols = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '-', '_', '!', '?', '-',
]

hard_password_symbols = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|', '~', '`',
]

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет, это бот для создания паролей! Напиши /password для создания паролей")

@bot.message_handler(commands=['password'])
def num_of_symbols(message):
    msg = bot.send_message(message.chat.id, 'Ваше количество символов')
    bot.register_next_step_handler(msg, difficulty)

def difficulty(message):
    try:
        length = int(message.text)
        msg = bot.send_message(message.chat.id, "Укажите сложность пароля.\n\nНапример: easy, mid, hard")
        bot.register_next_step_handler(msg, lambda m: password(m, length))
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите число")

def password(message, length):
    diff = message.text.lower()
    if diff == "easy":
        password_symbols = easy_password_symbols
    elif diff == "mid":
        password_symbols = mid_password_symbols
    elif diff == "hard":
        password_symbols = hard_password_symbols
    try:
        bot.send_message(message.chat.id, f"Ваш пароль №1: {''.join(random.choices(password_symbols, k=length))}"
                                          f"\n\nВаш пароль №2: {''.join(random.choices(password_symbols, k=length))}"
                                          f"\n\nВаш пароль №3: {''.join(random.choices(password_symbols, k=length))}")
    except ValueError:
        bot.reply_to(message, "Введите допустимое значение символов")


@bot.message_handler(content_types=["text", "photo"])
def lol_messages(message):
    if message.photo:
        bot.reply_to(message, 'Прикольное фото')
    if message.text.lower() == 'Привет'.lower():
        bot.reply_to(message, 'Даров (/start)')
    else:
        bot.reply_to(message, 'чо')

bot.infinity_polling()
