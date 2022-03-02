import config
import telebot
import random
import random_word

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def boo(message):

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Agree")
    item2 = telebot.types.KeyboardButton("Disagree")

    markup.add(item1, item2)

    bot.send_message(
        message.chat.id,
        "Hi, {0.first_name}.\nTake a fortune cookie, buddy".format(message.from_user),
        parse_mode='html',
        reply_markup=markup,)


@bot.message_handler(content_types=['text'])
def boo_text(message):
    if message.chat.type == 'private':
        if message.text == "Agree":
            rand_nick = random_word.RandomWords().get_random_word()
            if rand_nick:
                bot.send_message(message.chat.id, rand_nick)
            else:
                bot.send_message(message.chat.id, "mirror")
        elif message.text == "Disagree":
            # inline keyboard
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton("Mew", callback_data='cat')
            item2 = telebot.types.InlineKeyboardButton("Rawr", callback_data='dog')
            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Okay", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Badabee")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.data == 'cat':
            cats = open('kittens.webp', 'rb')
            bot.send_photo(call.message.chat.id, cats, 'Kittens')
        elif call.data == 'dog':
            dogs = open('adoggo.webp', 'rb')
            bot.send_photo(call.message.chat.id, dogs, 'A doggo')

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)


