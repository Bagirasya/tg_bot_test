import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def boo(message):
    bot.send_message(
        message.chat.id, "Hi, {0.first_name}.\nGive me your birth date, time and place, please".format(message.from_user), parse_mode='html')

@bot.message_handler(content_types=['text'])
def boo(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)


