import telebot
from telebot import types


def call_admin(message, bot):
    adm_id = '897514632'
    msg_id = message.message_id
    bot.send_message(adm_id, f'Дашуля, тебе тут вопросик от {message.from_user.first_name}. Помоги мне, я не могу на '
                             f'это ответить.')
    bot.forward_message(chat_id=adm_id, from_chat_id=message.chat.id, message_id=msg_id)


def start_mess(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1, 9):
        btn = types.KeyboardButton(str(i))
        markup.add(btn)
    stick_token = 'CAACAgIAAxkBAAEFS0hi0tHn-szAiBzvbA2nxgdQoHtkAQACAQMAAsxUSQkSK9r0GUh3qykE'
    bot.send_sticker(message.chat.id, stick_token)
    mess = f'<b>{message.from_user.first_name.capitalize()}</b>,' \
        f' что бы ты хотел узнать? Вот возможные комманды:'
    with open('commands.txt ', 'r', encoding='utf8') as F:
        com = F.read()
        bot.send_message(message.chat.id, f'{mess}\n{com}', reply_markup=markup, parse_mode='html')


def com_1(message, bot):
    with open('first_meet.txt', 'r', encoding='utf8') as F:
        bot.send_message(message.chat.id, F.read())


def com_2(message, bot):
    works = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg', 'photo5.jpg', 'photo6.jpg',
             'photo7.jpg', 'photo8.jpg', 'photo9.jpg', 'photo10.jpg']
    bot.send_media_group(message.chat.id,
                         [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in works])


def com_3(message, bot):
    with open('rewiews.jpg', 'rb') as ph:
        mess = f'Вот, держи. Надеюсь твой отзыв в дальнейшем пополнит этот коллаж!'
        bot.send_photo(message.chat.id, ph, caption=mess)


def com_4(message, bot):
    with open('price-list.jpg', 'rb') as ph:
        bot.send_photo(message.chat.id, ph, caption='Помни, что стоимость каждой татуировки сугубо индивидуальна'
                                                    ' и  зависит от многих фаткоров!')


def com_5(message, bot):
    with open('adresses.txt', 'r', encoding='utf8') as F:
        bot.send_message(message.chat.id, F.read())


def com_6(message, bot):
    mess = f'Ты можешь записаться ко мне через личные сообщения в социальных сетях:\n' \
           f'<a href="https://instagram.com/dda.tattoo?igshid=YmMyMTA2M2Y=">Мой инстаграмм</a>\n' \
           f'<a href="https://vk.com/pechyonkina75">Мой ВК</a>\n' \
           f'А еще ты можешь написать мне в Telegramm или в WhatsApp, лови мой номер:'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_contact(message.chat.id, '+79961890809', 'Дарья Артемовна')


def com_7(message, bot):
    with open('prepairing_for_tattoo.txt', 'r', encoding='utf8') as F:
        bot.send_message(message.chat.id, F.read())


def com_8(message, bot):
    with open('take_care_for_tattoo.txt', 'r', encoding='utf8') as F:
        mess = f'<b>Пошаговая инструкция по уходу за тату.</b>\n{F.read()}'
        bot.send_message(message.chat.id, mess, parse_mode='html')


def say_sorry_if_dont_understand(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Зови")
    btn2 = types.KeyboardButton("Перейти к коммандам")
    markup.add(btn1, btn2)
    mess = 'К сожалению я не могу тебя понять. Ты можешь перейти к коммандам.' \
           ' Если я ничем не могу тебе помочь, то мы можем позвать Дашу, и она точно не оставит тебя без ответа.'
    bot.send_message(message.chat.id, mess, reply_markup=markup)