import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def boo(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)


