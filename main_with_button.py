import telebot
from telebot import types
import functional





@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Перейти к коммандам")
    markup.add(btn1)
    with open('start_msg.txt', 'r', encoding='utf8') as F:
        mess = f'Привет, <b>{message.from_user.first_name.capitalize()}' \
                f'</b>!\n {F.read()}'
        bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Перейти к коммандам':
        functional.start_mess(message, bot)
    elif message.text == '1':
        functional.com_1(message, bot)
    elif message.text == '2':
        functional.com_2(message, bot)
    elif message.text == '3':
        functional.com_3(message, bot)
    elif message.text == '4':
        functional.com_4(message, bot)
    elif message.text == '5':
        functional.com_5(message, bot)
    elif message.text == '6':
        functional.com_6(message, bot)
    elif message.text == '7':
        functional.com_7(message, bot)
    elif message.text == '8':
        functional.com_8(message, bot)
    else:
        if message.text == 'Зови':
            functional.call_admin(message, bot)
        else:
            functional.say_sorry_if_dont_understand(message, bot)


if __name__ == '__main__':
    bot.polling(none_stop=True)
