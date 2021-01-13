import telebot
from config import TOKEN, keys
from extensions import CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    text = 'Чтобы узнать интересующий курс введите команду в следующем формате:\n<имя валюты> ' \
           '<имя валюты в которой надо узнать цену первой валюты> ' \
           '<количество первой валюты>' \
           '\nНапример: евро рубль 1' \
           '\n' \
           '\nУвидеть список всех доступных валют: /value' \
           '\n' \
           '\nСправка: /help'
    if message.text == '/start':
        bot.send_message(message.chat.id, f'Здравствуйте {message.from_user.first_name}!\n\n{text}')
    elif message.text == '/help':
        bot.send_message(message.chat.id, f'{text}')


@bot.message_handler(commands=['value'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def send_message(message):
    text = CryptoConverter.get_price(message)
    bot.reply_to(message, text)


@bot.message_handler(content_types=['document', 'audio', 'voice', 'photo', 'video', 'contact'])
def handle_docs_audio(message):
    bot.send_message(message.chat.id, 'Сложновато, введите запрос текстом')


@bot.message_handler(content_types=['sticker'])
def cheak_sticker(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBpl_-xiT56G-rubPnJcRzfZYxGt9vAAI3AANOXNIpdbSyVJtgJt8eBA')


bot.polling(none_stop=True)
