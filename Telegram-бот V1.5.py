import telebot
from telebot import types
import random
from random import choice
from test_Keplerians import *
from variables import *
import xml.etree.ElementTree as ET
token = ''
bot = telebot.TeleBot(token)

chat_global_file = open("chat.txt", "r")
chat_global = set()
for line in chat_global_file:
    chat_global.add(line.strip())
chat_global_file.close()

def staet():
    bot.send_message(chat, "Бот успешно запущен!")

if __name__ == "__main__":
    staet()

@bot.message_handler(commands=['start'])
def komand(message):
    black_list = open("black_list.txt", "r", encoding="UTF-8")
    black_l = black_list.read()
    if not str(message.chat.id) in black_l:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but5 = '/idea'
        but6 = '/test'
        but7 = '/beta_kmn'
        but8 = '/beta_randomaizer'
        but9 = '/info'
        markup.add(but5, but6, but7, but8, but9)
        bot.send_message(message.chat.id, """Привет! С тобой Саня, ты в моем боте! Выбери одну из команд ниже:\n/idea - Можно подкинуть мне идею для видео!(P.S. все идеи будут приходить мне, так что не надо писать всякую фигню!)\n/test - Можно пройти тест по играм Keplerians!\n/beta_kmn - игра "Камень, ножницы, бумага"! Можно играть как одному, так и с друзьями! (бета-версия)\n/beta_randomaizer - Рандомайзер! Доступен как и в одиночном режиме, так и в сетевом режиме! (бета-версия)\n/info - Информация о боте и его разработчике!""", reply_markup=markup)
        if not str(message.chat.id) in chat_global:
            chat_global_file = open("chat.txt", "a")
            chat_global_file.write(str(message.chat.id) + "\n")
            chat_global.add(message.chat.id)
    elif str(message.chat.id) in black_l:
        bot.send_message(message.chat.id, black_list_text)

@bot.message_handler(commands=['spec'])
def n(message):
    markup = types.ReplyKeyboardMarkup(True)
    but1 = types.KeyboardButton("Внутри бота!")
    but2 = types.KeyboardButton("В ТГ-канал")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardMarkup(True)
    but = '/start'
    markup1.add(but)
    if str(message.chat.id) == chat:
        send = bot.send_message(chat, "Выбери куда будет отправляться пост!", reply_markup=markup)
        bot.register_next_step_handler(send, start1)
    elif str(message.chat.id) != chat:
        bot.send_message(message.chat.id, "Извините, команда доступна только администраторам бота!", reply_markup=markup1)

def start1(message):
    markup = types.ReplyKeyboardMarkup(True)
    but1 = types.KeyboardButton("Фото")
    but2 = types.KeyboardButton("Текст")
    markup.add(but1, but2)
    if message.text in poluchat:
        if message.text == poluchat[0]:
            send = bot.send_message(chat, "Выбери начинку поста!", reply_markup=markup)
            bot.register_next_step_handler(send, start2)
        elif message.text == poluchat[1]:
            send = bot.send_message(chat, "Выбери начинку поста!", reply_markup=markup)
            bot.register_next_step_handler(send, start3)
    elif not message.text in poluchat:
        send = bot.send_message(chat, "Ой")
        bot.register_next_step_handler(send, start1)

def start2(message):
    markup = types.ReplyKeyboardMarkup(True)
    but = "/stop"
    markup.add(but)
    if message.text in ft:
        if message.text == ft[0]:
            send = bot.send_message(chat, "Приложи фото и напиши текст (при необходимости)!", reply_markup=markup)
            bot.register_next_step_handler(send, start_fb)
        elif message.text == ft[1]:
            send = bot.send_message(chat, "Напиши сообщение!", reply_markup=markup)
            bot.register_next_step_handler(send, start_tb)
    elif not message.text in ft:
        send = bot.send_message(chat, "Ой")
        bot.register_next_step_handler(send, start2)

def start3(message):
    markup = types.ReplyKeyboardMarkup(True)
    but = "/stop"
    markup.add(but)
    if message.text in ft:
        if message.text == ft[0]:
            send = bot.send_message(chat, "Приложи фото и напиши текст (при необходимости)!", reply_markup=markup)
            bot.register_next_step_handler(send, start_fk)
        elif message.text == ft[1]:
            send = bot.send_message(chat, "Напиши сообщение!", reply_markup=markup)
            bot.register_next_step_handler(send, start_tk)
    elif not message.text in ft:
        send = bot.send_message(chat, "Ой")
        bot.register_next_step_handler(send, start3)

def start_tk(message):
    if message.content_type == "text" and message.text != stop:
        bot.send_message(kanal, message.text, parse_mode="Markdown", timeout=0)
        bot.send_message(chat, "Сообщение отправлено!", timeout=0)
    elif message.text == stop:
        bot.send_message(chat, "Вы отказались от публикаций в канал!")

def start_fk(message):
    if message.content_type == "photo":
        bot.send_photo(chat_id=kanal, photo=message.photo[0].file_id, caption=message.caption, parse_mode="Markdown", timeout=0)
        bot.send_message(chat, "Сообщения успешно отправлены!")
    elif message.content_type != "photo" and message.text == stop:
        bot.send_message(message.chat.id, "Вы отказались от публикаций в канал!")
    elif message.content_type != "photo" and message.text != stop:
        send = bot.send_message(chat, "Это не фото! Добавь фото!")
        bot.register_next_step_handler(send, start_fk)

def start_tb(message):
    if message.content_type == "text" and message.text != stop:
        kluch = int(baza.find("posled_mes").text) + 1
        baza.find("posled_mes").text = str(int(baza.find("posled_mes").text) + 1)
        r = ET.Element(f"post_mes{kluch}")
        for user in chat_global:
            try:
                send = bot.send_message(user, message.text, parse_mode="Markdown", timeout=0)
                post = ET.Element(f"message{user}")
                post.attrib['mesid'] = str(send.id)
                post.attrib["chatid"] = user
                post.text = "text"
                r.append(post)
                root.append(r)
            except:
                print(user)
        bot.send_message(chat, f"Сообщения №```{kluch}``` успешно отправлены\!", parse_mode="MarkdownV2")
    elif message.text == stop:
        bot.send_message(message.chat.id, "Вы не стали добавлять текст в бот!")
    baza.write("baza.xml", encoding="UTF-8")

def start_fb(message):
    if message.content_type == "photo":
        kluch = int(baza.find("posled_mes").text) + 1
        baza.find("posled_mes").text = str(int(baza.find("posled_mes").text) + 1)
        r = ET.Element(f"post_mes{kluch}")
        for user in chat_global:
            try:
                send = bot.send_photo(chat_id=user, photo=message.photo[0].file_id, caption=message.caption, parse_mode="Markdown", timeout=0)
                post = ET.Element(f"message{user}")
                post.attrib['mesid'] = str(send.id)
                post.attrib["chatid"] = user
                post.text = "photo"
                r.append(post)
                root.append(r)
            except:
                print(user)
        bot.send_message(chat, f"Сообщения №```{kluch}``` успешно отправлены\!", parse_mode="MarkdownV2")
    elif message.content_type != "photo" and message.text == stop:
        bot.send_message(message.chat.id, "Вы не стали добавлять текст в бот!")
    elif message.content_type != "photo" and message.text != stop:
        send = bot.send_message(chat, "Это не фото! Добавь фото!")
        bot.register_next_step_handler(send, start_fb)
    baza.write("baza.xml", encoding="UTF-8")

@bot.message_handler(commands=["admin"])
def adminka(message):
    markup = types.ReplyKeyboardMarkup(True)
    but = types.KeyboardButton("/start")
    markup.add(but)
    markup1 = types.ReplyKeyboardRemove()
    if str(message.chat.id) == chat:
        send = bot.send_message(chat, "Введите номер сообщения!", reply_markup=markup1)
        bot.register_next_step_handler(send, sta)
    elif str(message.chat.id) != chat:
        bot.send_message(message.chat.id, "Извините, команда доступна только администратору бота!", reply_markup=markup)

def sta(message):
    markup = types.ReplyKeyboardMarkup(True)
    but1 = types.KeyboardButton("Изменить его")
    but2 = types.KeyboardButton("Удалить")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardMarkup(True)
    but = types.KeyboardButton("/start")
    markup1.add(but)
    if message.text.isdigit():
        kluch = str(message.text)
        if baza.find(f"post_mes{kluch}") != None:
            o = baza.find(f"mes{chat}")
            o.text = str(message.text)
            send = bot.send_message(chat, "Выберите действие с сообщением!", reply_markup=markup)
            bot.register_next_step_handler(send, sa)
        elif baza.find(f"post_mes{kluch}") == None:
            send = bot.send_message(chat, "Сообщение не найдено! Введите другой номер!")
            bot.register_next_step_handler(send, sta)
    elif not message.text.isdigit() and message.text != stop:
        send = bot.send_message(chat, "Ой")
        bot.register_next_step_handler(send, sta)
    elif not message.text.isdigit() and message.text == stop:
        bot.send_message(chat, "Вы отказались от публикаций!", reply_markup=markup1)
    baza.write("baza.xml", encoding="utf-8")

def sa(message):
    markup = types.ReplyKeyboardMarkup(True)
    but = types.KeyboardButton(stop)
    markup.add(but)
    markup1= types.ReplyKeyboardMarkup(True)
    but1 = types.KeyboardButton(slova[0])
    but2 = types.KeyboardButton(slova[1])
    markup1.add(but1, but2)
    if message.text in deis_mes:
        if message.text == deis_mes[0]:
            send = bot.send_message(chat, "Введите новый текст!", reply_markup=markup)
            bot.register_next_step_handler(send, sa1)
        elif message.text == deis_mes[1]:
            send = bot.send_message(chat, "Вы точно хотите удалить сообщение? (восстановить его уже не получится!)", reply_markup=markup1)
            bot.register_next_step_handler(send, sa2)
    elif not message.text in deis_mes:
        send = bot.send_message(chat, "Ой")
        bot.register_next_step_handler(send, sa)

def sa1(message):
    markup = types.ReplyKeyboardMarkup(True)
    but = types.KeyboardButton("/start")
    markup.add(but)
    if message.content_type == "text" and message.text != stop:
        kluch = baza.find(f"mes{chat}").text
        for user in chat_global:
            try:
                mesid = baza.find(f"post_mes{kluch}").find(f"message{user}").attrib['mesid']
                if baza.find(f"post_mes{kluch}").find(f"message{user}").text == "text":
                    bot.edit_message_text(chat_id=user, text=message.text, message_id=mesid, parse_mode="Markdown")
                elif baza.find(f"post_mes{kluch}").find(f"message{user}").text == "photo":
                    bot.edit_message_caption(chat_id=user, caption=message.text, message_id=mesid)
            except:
                print(user)
        bot.send_message(chat, "Сообщение изменено!", timeout=0)
    elif message.text == stop:
        bot.send_message(chat, "Вы отказались от изменений сообщения!", reply_markup=markup)

def sa2(message):
    markup = types.ReplyKeyboardMarkup(True)
    but = types.KeyboardButton("/start")
    markup.add(but)
    if message.text.title() in slova:
        if message.text.title() == slova[0]:
            kluch = baza.find(f"mes{chat}").text
            for user in chat_global:
                try:
                    mesid = baza.find(f"post_mes{kluch}").find(f"message{user}").attrib['mesid']
                    bot.delete_message(chat_id=user, message_id=mesid, timeout=0)
                except:
                    print(user)
            bot.send_message(chat, "Сообщение удалено!", timeout=0, reply_markup=markup)
        elif message.text.title() == slova[1]:
            bot.send_message(chat, "Сообщение не было удалено!", reply_markup=markup)
    elif not message.text.title() in slova:
        send = bot.send_message(chat, "Ой")
        bot.register_next_step_handler(send, sa2)

@bot.message_handler(commands=['test'])
def nachalo(message):
    black_list = open("black_list.txt", "r", encoding="UTF-8")
    black_l = black_list.read()
    if not str(message.chat.id) in black_l:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = "Да!"
        markup.add(but1)
        send = bot.send_message(message.chat.id, "Привет! Давай проведим, насколько ты хорошо знаешь игры Keplerians! Начнем?", reply_markup=markup)
        bot.register_next_step_handler(send, vp_1)
    elif str(message.chat.id) in black_l:
        bot.send_message(message.chat.id, black_list_text)

def vp_1(message):
    global markup1, but1, but2, but3, but4
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = answer1
    but2 = answer2
    but3 = answer3
    but4 = answer4
    markup1.add(but1, but2, but3, but4)
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    if message.text == "Да!":
        send = bot.send_message(message.chat.id, f"{question1}\n{variants1}\n{variants2}\n{variants3}\n{variants4}", reply_markup=markup1)
        bot.register_next_step_handler(send, vp_2)
    else:
        bot.send_message(message.chat.id, "Эм, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

def vp_2(message):
    global ball1
    ball1 = 0
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    if message.text == answer2:
        ball1 += 1
        bot.send_message(message.chat.id, f"{answer5}\n{answer7} Первой игрой Кеплерианцев была игра The Nun. Но ее удалили из Google Play за нарушение авторских прав.")
    elif message.text == answer1 or answer3 or answer4:
        bot.send_message(message.chat.id, f"{answer6}\n{answer7} Первой игрой Кеплерианцев была игра The Nun. Но ее удалили из Google Play за нарушение авторских прав.")
    else:
        bot.send_message(message.chat.id, "Эм, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

    send = bot.send_message(message.chat.id, f"{question2}\n{variants5}\n{variants6}\n{variants7}\n{variants8}")
    bot.register_next_step_handler(send, vp_3)

def vp_3(message):
    global ball2
    ball2 = 0
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    if message.text == answer3:
        ball2 += 1
        bot.send_message(message.chat.id, f"{answer5}\n{answer7} Мистер Мит на первый взгляд кажется обычным мясником, но на самом деле он превращал людей в свиней и сдавал их на мясо (по данным из игры Mr Meat 2)")
    elif message.text == answer1 or answer2 or answer4:
        bot.send_message(message.chat.id, f"{answer6}\n{answer7} Мистер Мит на первый взгляд кажется обычным мясником, но на самом деле он превращал людей в свиней и сдавал их на мясо (по данным из игры Mr Meat 2)")
    else:
        bot.send_message(message.chat.id, "Эм, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

    send = bot.send_message(message.chat.id, f"{question3}\n{variants9}\n{variants10}\n{variants11}\n{variants12}")
    bot.register_next_step_handler(send, vp_4)

def vp_4(message):
    global ball3
    ball3 = 0
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    if message.text == answer4:
        bot.send_message(message.chat.id, f"{answer5}\n{answer7} Ребекка является дочкой Мистера Мита. В первой части Доктор Уайт помог Ребекке превратится ей назад в человека, но Ребекка не является дочкой Доктора Уайта")
        ball3 += 1
    elif message.text == answer1 or answer2 or answer3:
        bot.send_message(message.chat.id, f"{answer6}\n{answer7} Ребекка является дочкой Мистера Мита. В первой части Доктор Уайт помог Ребекке превратится ей назад в человека, но Ребекка не является дочкой Доктора Уайта")
    else:
        bot.send_message(message.chat.id, "Эм, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

    send = bot.send_message(message.chat.id, f"{question4}\n{variants13}\n{variants14}\n{variants15}\n{variants16}")
    bot.register_next_step_handler(send, vp_5)

def vp_5(message):
    global ball4
    ball4 = 0
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    if message.text == answer3:
        bot.send_message(message.chat.id, f"{answer5}\n{answer7} Возможно я вас удивлю, но Мишель является сестрой Ребекки. В доме Мистера Мита можно было увидеть фотографии семьи, где зачеркнутым ребенком как раз была Мишель, а не Ребекка")
        ball4 += 1
    elif message.text == answer1 or answer2 or answer4:
        bot.send_message(message.chat.id, f"{answer6}\n{answer7} Возможно я вас удивлю, но Мишель является сестрой Ребекки. В доме Мистера Мита можно было увидеть фотографии семьи, где зачеркнутым ребенком как раз была Мишель, а не Ребекка")
    else:
        bot.send_message(message.chat.id, "Эм, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

    send = bot.send_message(message.chat.id, f"{question5}\n{variants17}\n{variants18}\n{variants19}\n{variants20}")
    bot.register_next_step_handler(send, vp_6)

def vp_6(message):
    global ball5
    ball5 = 0
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup2.add(but1, but2, but3)
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    if message.text == answer2:
        bot.send_message(message.chat.id, f"{answer5}\n{answer7} Джей - простой мальчик из небольшого городка, который имел дело с Мороженщиком, спасал друзей от него и сам попал на фабрику Мороженщика")
        ball5 += 1
    elif message.text == answer1 or answer3 or answer4:
        bot.send_message(message.chat.id, f"{answer6}\n{answer7} Джей - простой мальчик из небольшого городка, который имел дело с Мороженщиком, спасал друзей от него и сам попал на фабрику Мороженщика")
    else:
        bot.send_message(message.chat.id, "Эм, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

    send = bot.send_message(message.chat.id, f"{question6}\n{variants21}\n{variants22}\n{variants23}", reply_markup=markup2)
    bot.register_next_step_handler(send, vp_7)

def vp_7(message):
    global ball6
    ball6 = 0
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    if message.text == answer1:
        bot.send_message(message.chat.id, f"""{answer5}\n{answer7} в прачечной находятся дети монахини, которых сама ловила с помощью приглашений в "лагерь" """)
        ball6 += 1
    elif message.text == answer2 or answer3 or answer4:
        bot.send_message(message.chat.id, f"""{answer6}\n{answer7} в прачечной находятся дети монахини, которых сама ловила с помощью приглашений в "лагерь" """)
    else:
        bot.send_message(message.chat.id, "Эм, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

    send = bot.send_message(message.chat.id, f"{question7}\n{variants24}\n{variants25}\n{variants26}")
    bot.register_next_step_handler(send, vp_8)

def vp_8(message):
    global ball7
    ball7 = 0
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    if message.text == answer2:
        bot.send_message(message.chat.id, f"{answer5}\n{answer7} крокодил был в третьей части Ice Scream, с помощью него можно получить револьеры, и первой части монахини, при побеге через водосток")
        ball7 += 1
    elif message.text == answer1 or answer3 or answer4:
        bot.send_message(message.chat.id, f"{answer6}\n{answer7} крокодил был в третьей части Ice Scream, с помощью него можно получить револьеры, и первой части монахини, при побеге через водосток")
    else:
        bot.send_message(message.chat.id, "Эм, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

    send = bot.send_message(message.chat.id, f"{question8}\n{variants27}\n{variants28}\n{variants29}")
    bot.register_next_step_handler(send, vp_9)

def vp_9(message):
    global ball8
    ball8 = 0
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    if message.text == answer3:
        bot.send_message(message.chat.id, f"""{answer5}\n{answer7} 31 октября вышла первая игра Кеплерианцев под названием "Evil Nun: The Broken Mask". Она доступна в магазине Steam и Epic Games! #НеРеклама""")
        ball8 += 1
    elif message.text == answer1 or answer2 or answer4:
        bot.send_message(message.chat.id, f"""{answer6}\n{answer7} 31 октября вышла первая игра Кеплерианцев под названием "Evil Nun: The Broken Mask". Она доступна в магазине Steam и Epic Games! #НеРеклама""")
    else:
        bot.send_message(message.chat.id, "Эм, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

    send = bot.send_message(message.chat.id, f"{question9}\n{variants30}\n{variants31}\n{variants32}")
    bot.register_next_step_handler(send, vp_10)

def vp_10(message):
    global ball9
    ball9 = 0
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    if message.text == answer1:
        bot.send_message(message.chat.id, f"{answer5}\n{answer7} Granny была полностью разработана DVLoper, Keplerians не принимали никакого участия в разработке")
        ball9 += 1
    elif message.text == answer2 or answer3 or answer4:
        bot.send_message(message.chat.id, f"{answer6}\n{answer7} Granny была полностью разработана DVLoper, Keplerians не принимали никакого участия в разработке")
    else:
        bot.send_message(message.chat.id, "Эм, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

    send = bot.send_message(message.chat.id, f"{question10}\n{variants33}\n{variants34}\n{variants35}")
    bot.register_next_step_handler(send, itog)

def itog(message):
    global ball10
    ball10 = 0
    if message.text == answer2:
        ball10 += 1
        bot.send_message(message.chat.id, f"{answer5}\n{answer7} 16 декабря вышла 7 часть Ise Scream, поэтому на данный момент частей Ise Scream 7, а не 6")
    elif message.text == answer1 or answer3 or answer4:
        bot.send_message(message.chat.id, f"{answer6}\n{answer7} 16 декабря вышла 7 часть Ise Scream, поэтому на данный момент частей Ise Scream 7, а не 6")
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    ball = ball1 + ball2 + ball3 + ball4 + ball5 + ball6 + ball7 + ball8 + ball9 + ball10
    bot.send_message(message.chat.id, "Спасибо за прохождение теста!")
    if ball < 3:
        print(f"{message.from_user.first_name}: {ball} баллов")
        bot.send_message(message.chat.id, f"Твой балл: {ball}\nВидно ты плохо в этом разбираешься, советую подтянуть знания по играм Keplerians!", reply_markup=markup3)
    elif ball >= 3 and ball < 6:
        print(f"{message.from_user.first_name}: {ball} баллов")
        bot.send_message(message.chat.id, f"Твой балл: {ball}\nНеплохо, неплохо! Вижу ± ты игры знаешь!", reply_markup=markup3)
    elif ball >= 6 and ball < 9:
        print(f"{message.from_user.first_name}: {ball} баллов")
        bot.send_message(message.chat.id, f"Твой балл: {ball}\nВижу, игры знаешь вообще замечательно!", reply_markup=markup3)
    elif ball >= 9:
        print(f"{message.from_user.first_name}: {ball} баллов")
        bot.send_message(message.chat.id, f"Твой балл: {ball}\nДа ты вообще бог!", reply_markup=markup3)
    bot.send_message(message.chat.id, "Нажми кнопку ниже!")

@bot.message_handler(commands=['idea'])
def vibor(message):
    black_list = open("black_list.txt", "r", encoding="UTF-8")
    black_l = black_list.read()
    if not str(message.chat.id) in black_l:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton(blogers[0])
        but2 = types.KeyboardButton(blogers[1])
        markup.add(but1, but2)
        send = bot.send_message(message.chat.id, f"Выбери, кому будешь подавать идею:", parse_mode="Markdown", reply_markup=markup)
        bot.register_next_step_handler(send, idea1)
    elif str(message.chat.id) in black_l:
        bot.send_message(message.chat.id, black_list_text)

def idea1(message):
    if message.text in blogers:
        idea[str(message.chat.id)] = str(message.text)
        i4(message)
    elif not message.text in blogers:
        send = bot.send_message(message.chat.id, "Ой, не совсем тебя понял! Нажми кнопку ниже!")
        bot.register_next_step_handler(send, idea1)

def i4(message):
    markup = types.ReplyKeyboardMarkup(True)
    but = types.KeyboardButton(stop)
    markup.add(but)
    if idea[str(message.chat.id)] == blogers[0]:
        send = bot.send_message(chat_id=message.chat.id,  text=f"Напиши сообщение, я прочитаю и отвечу\!\n\n||Или нажми {stop} если передумал подавать идею\!||", parse_mode='MarkdownV2', reply_markup=markup)
        bot.register_next_step_handler(send, sanya)
    elif idea[str(message.chat.id)] == blogers[1]:
        send = bot.send_message(chat_id=message.chat.id,  text=f"Напиши сообщение, Илья прочитает и возможно ответит\!\n\n||Или нажми {stop} если передумал подавать идею\!||", parse_mode='MarkdownV2', reply_markup=markup)
        bot.register_next_step_handler(send, sanya)

def sanya(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/start")
    markup.add(but)
    text = str(message.text)
    print(str(message.text))
    if idea[str(message.chat.id)] == blogers[0]:
        if message.content_type == "text" and message.text != "/stop":
            bot.send_message(message.chat.id, "Твое сообщение успешно отправлено!", reply_markup=markup)
            bot.send_message(chat_id=chat, text=f"Поступило новое предложение от {message.chat.id}! Читай: {message.text}")
        elif message.text == "/stop":
            bot.send_message(message.chat.id, "Вы отказались от предоставления идеи!", reply_markup=markup)
    if idea[str(message.chat.id)] == blogers[1]:
        if message.content_type == "text" and message.text != "/stop":
            bot.send_message(message.chat.id, "Твое сообщение успешно отправлено!", reply_markup=markup)
            bot.send_message(chat_id=chat1, text=f"Поступило новое предложение от {message.chat.id}! Читай: {message.text}")
        elif message.text == "/stop":
            bot.send_message(message.chat.id, "Вы отказались от предоставления идеи!", reply_markup=markup)


@bot.message_handler(commands=['proverka'])
def admin(message):
    ne_chat_id = str(message.chat.id)
    markup = types.ReplyKeyboardRemove()
    if ne_chat_id in admin_chat:
        if ne_chat_id == chat:
            send = bot.send_message(chat_id=chat, text="Введи Chat Id кому надо ответить", reply_markup=markup)
            bot.register_next_step_handler(send, admin1)
        elif ne_chat_id == chat1:
            send = bot.send_message(chat_id=chat1, text="Введи Chat Id кому надо ответить", reply_markup=markup)
            bot.register_next_step_handler(send, admin3)
    elif ne_chat_id != chat1:
        bot.send_message(ne_chat_id, "Извините, команда доступна только администраторам бота!")

def admin1(message):
    global chat_id2
    chat_id2 = str(message.text)
    markup = types.ReplyKeyboardRemove()
    send = bot.send_message(chat_id=chat, text="Введи ответ!", reply_markup=markup)
    bot.register_next_step_handler(send, admin2)

def admin2(message):
    bot.send_message(chat_id=chat, text="Сообщение отправлено!")
    bot.send_message(chat_id=chat_id2, text=f"Саня KONTROL CHEK ответ на твою идею! вот его текст:\n{message.text}")

def admin3(message):
    global chat_id3
    chat_id3 = str(message.text)
    send = bot.send_message(chat_id=chat1, text="Введи ответ!")
    bot.register_next_step_handler(send, admin5)

def admin5(message):
    bot.send_message(chat_id=chat1, text="Сообщение отправлено!")
    bot.send_message(chat_id=chat_id3, text=f"Илья IluyhichPLAY ответил на твою идею! Быстрее читай: {message.text}")

@bot.message_handler(commands=['beta_kmn'])
def kmn_nach(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Одиночный")
    but2 = types.KeyboardButton("Сетевой")
    markup.add(but1, but2)
    send = bot.send_message(message.chat.id, "Привет! Добро пожаловать в игру Камень-ножницы-бумага! Выбери нужный тебе режим!", reply_markup=markup)
    bot.register_next_step_handler(send, kmn_vib)

def kmn_vib(message):
    print(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton(kamen)
    but2 = types.KeyboardButton(noshik)
    but3 = types.KeyboardButton(bumaga)
    but4 = types.KeyboardButton(stop)
    markup.add(but1, but2, but3).add(but4)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but9 = types.KeyboardButton(kmn_kolvo[0])
    but10 = types.KeyboardButton(kmn_kolvo[1])
    markup1.add(but9, but10)
    markup2= types.ReplyKeyboardRemove()
    if message.text.title() in kmn_reshim:
        if message.text.title() == "Одиночный":
            shet[f"{message.chat.id}kmnna1_ig"] = int(0)
            shet[f"{message.chat.id}kmnna1_bot"] = int(0)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            but5 = types.KeyboardButton(kamen)
            but6 = types.KeyboardButton(noshik)
            but7 = types.KeyboardButton(bumaga)
            but8 = types.KeyboardButton(stop)
            markup.add(but5, but6, but7, but8)
            send = bot.send_message(message.chat.id, "Текущий счёт:\nВы *" + str(shet[f"{message.chat.id}kmnna1_ig"]) + ":" + str(shet[f"{message.chat.id}kmnna1_bot"]) + "* Бот", parse_mode="Markdown")
            send1 = bot.send_message(message.chat.id, "Выбери Камень, ножницы или бумагу", reply_markup=markup)
            bot.register_next_step_handler(send1, kmn_odin)
            shet[f"{message.chat.id}kmnna1_mes"] = send.message_id
            shet[f"{message.chat.id}kmnna1_mesdel"] = send1.message_id
        elif message.text.title() == "Сетевой":
            send = bot.send_message(message.chat.id, "Выберите количество игроков ниже!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_rasvetvlenie)
    elif not message.text.title() in kmn_reshim:
        send = bot.send_message(message.chat.id, "Ой, не совсем тебя понял! Нажми кнопку ниже!")
        bot.register_next_step_handler(send, kmn_vib)
    kmn3.write("bazakmn3.xml", encoding="UTF-8")

def kmn_rasvetvlenie(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("/stop")
    markup.add(but1)
    markup1 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton(sposob_prig[0])
    but3 = types.KeyboardButton(sposob_prig[1])
    markup1.add(but2, but3)
    if message.text in kmn_kolvo:
        if message.text == kmn_kolvo[0]:
            if kmn2.find(f"user{message.chat.id}") == None:
                igrok1 = ET.Element(f"user{message.chat.id}")
                igrok1.attrib["id"] = str(message.chat.id)
                kmn2r.append(igrok1)
                if message.from_user.last_name != None:
                    user1 = ET.Element("nameig")
                    user1.text = f"{message.from_user.first_name} {message.from_user.last_name}"
                    igrok1.append(user1)
                elif message.from_user.last_name == None:
                    user1 = ET.Element("nameig")
                    user1.text = str(message.from_user.first_name)
                    igrok1.append(user1)
            elif kmn2.find(f"user{message.chat.id}") != None:
                igrok1 = kmn2.find(f"user{message.chat.id}")
                user1 = kmn2.find(f"user{message.chat.id}").find("nameig")
                if message.from_user.last_name != None:
                    user1.text = f"{message.from_user.first_name} {message.from_user.last_name}"
                elif message.from_user.last_name == None:
                    user1.text = str(message.from_user.first_name)
            send = bot.send_message(message.chat.id, "Пожалуйста, выберите способ приглашения друга ниже!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_rasvetvlenie_mp2)
        elif message.text == kmn_kolvo[1]:
            if kmn3.find(f"user{message.chat.id}") == None:
                igrok1 = ET.Element(f"user{message.chat.id}")
                igrok1.attrib["id"] = str(message.chat.id)
                kmn3r.append(igrok1)
                if message.from_user.last_name != None:
                    user1 = ET.Element("nameig")
                    user1.text = f"{message.from_user.first_name} {message.from_user.last_name}"
                    igrok1.append(user1)
                elif message.from_user.last_name == None:
                    user1 = ET.Element("nameig")
                    user1.text = str(message.from_user.first_name)
                    igrok1.append(user1)
            elif kmn3.find(f"user{message.chat.id}") != None:
                igrok1 = kmn3.find(f"user{message.chat.id}")
                user1 = kmn3.find(f"user{message.chat.id}").find("nameig")
                if message.from_user.last_name != None:
                    user1.text = f"{message.from_user.first_name} {message.from_user.last_name}"
                elif message.from_user.last_name == None:
                    user1.text = str(message.from_user.first_name)
            send = bot.send_message(message.chat.id, "Пожалуйста, выберите способ приглашения друга ниже!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_rasvetvlenie_mp3)
    elif not message.text in kmn_kolvo:
        send = bot.send_message(message.chat.id, "Ой, не совсем тебя понял, нажми кнопку ниже!")
        bot.register_next_step_handler(send, kmn_rasvetvlenie)

def kmn_rasvetvlenie_mp2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("/stop")
    markup.add(but1)
    markup1 = types.ReplyKeyboardRemove()
    markup2 = types.ReplyKeyboardMarkup(True)
    but = types.KeyboardButton("/start")
    markup2.add(but)
    if message.text.title() in sposob_prig:
        if message.text.title() == sposob_prig[0]:
            send = bot.send_message(message.chat.id, "Отлично! Отправьте мне сообщение от друга!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_mp_2_priglas_message)
        elif message.text.title() == sposob_prig[1]:
            p = open("Важное фото.png", "rb")
            send = bot.send_photo(message.chat.id, photo=p, caption="Отлично! Введи Chat Id одного из нужных пользователя!\n*Важно! Что такое Chat Id и как его получить?*\nChat Id - это уникальный идентификатор, который используется в ботах для отправки сообщений пользователям (надеюсь объяснил понятно).\nДля того чтобы получить Chat Id вашего друга нужно найти сообщение друга и отправить его боту @userinfobot и скопировать набор цифр из *ВТОРОЙ СТРОКИ* и отправить его в ответ на это сообщение!\n_P.S. кнопка /stop это для того чтобы отменить выбор!_", reply_markup=markup, parse_mode="Markdown")
            bot.register_next_step_handler(send, kmn_mp)
    elif not message.text.title() in sposob_prig and message.text != stop:
        send = bot.send_message(message.chat.id, "Ой, не совсем тебя понял, нажми кнопку ниже!")
        bot.register_next_step_handler(send, kmn_rasvetvlenie_mp2)
    elif not message.text.title() in sposob_prig and message.text == stop:
        bot.send_message(message.chat.id, "Вы остановили выбор!", reply_markup=markup2)

def kmn_mp_2_priglas_message(message):
    bot.delete_message(message.chat.id, message.message_id)
    try:
        igrok1 = kmn2.find(f"user{message.chat.id}").attrib["id"]
        user1 = kmn2.find(f"user{message.chat.id}").find("nameig").text
        markup = types.ReplyKeyboardMarkup(True)
        but1 = types.KeyboardButton(slova[0])
        but2 = types.KeyboardButton(slova[1])
        markup.add(but1, but2)
        chat_global_file = open("chat.txt", "r")
        text2 = f"Попросите вашего друга зайти в бот и нажать кнопку /start, а потом повторите попытку, либо нажмите {stop} для прекращения приглашений друга!!\nОшибка повторяется? Ответ ищите [здесь](https://t.me/kontrol_chek185/1131)"
        allText = chat_global_file.read()
        spis_chat_id = list(map(str, allText.split()))
        if kmn2.find(f"user{message.chat.id}").find("igrok2") == None:
            igrok = ET.Element("igrok2")
            igrok.attrib["id"] = str(message.forward_from.id)
            igrok.text = None
            kmn2.find(f"user{message.chat.id}").append(igrok)
        elif kmn2.find(f"user{message.chat.id}").find("igrok2") != None:
            igrok = kmn2.find(f"user{message.chat.id}").find("igrok2")
            igrok.attrib["id"] = str(message.forward_from.id)
            igrok.text = None
        if kmn2.find(f"user{message.forward_from.id}") == None:
            igrok2 = ET.Element(f"user{message.forward_from.id}")
            igrok2.attrib["id"] = str(message.forward_from.id)
            kmn2r.append(igrok2)
            igrok2 = kmn2.find(f"user{message.forward_from.id}")
            igrok = ET.Element("nameig")
            igrok.text = None
            igrok2.append(igrok)
            igrok_ = ET.Element("igrok2")
            igrok_.attrib["id"] = str(message.chat.id)
            igrok_.text = user1
            igrok2.append(igrok_)
            igrok2 = kmn2.find(f"user{message.forward_from.id}").attrib["id"]
        elif kmn2.find(f"user{message.forward_from.id}") != None:
            igrok2 = kmn2.find(f"user{message.forward_from.id}").attrib["id"]
            igrok = kmn2.find(f"user{message.forward_from.id}").find("igrok2")
            igrok.attrib["id"] = str(message.chat.id)
            igrok.text = user1
        text = "[здесь](https://t.me/kontrol_chek185/1131)"
        if igrok1 != igrok2:
            if igrok2 in spis_chat_id:
                bot.send_message(igrok1, "Отправил приглашение! Ожидай ответа!")
                send = bot.send_message(igrok2, f"Игрок {user1} прислал вам приглашение, хотите играть?", reply_markup=markup)
                bot.register_next_step_handler(send, kmn_mp_vib_ig1)
            elif not igrok2 in spis_chat_id:
                send = bot.send_message(message.chat.id, f"Пользователь не найден в базе данных бота! {text2}", parse_mode="Markdown")
                bot.register_next_step_handler(send, kmn_mp)
        elif igrok2 == igrok1:
            send = bot.send_message(message.chat.id, f"Извините с самим собой играть нельзя! Попробуйте еще раз!\nЧто делать если возникает такая ошибка? Ищите {text}", parse_mode="Markdown")
            bot.register_next_step_handler(send, kmn_mp)
    except AttributeError:
        markup1 = types.ReplyKeyboardMarkup(True)
        but1 = types.KeyboardButton(sposob_prig[0])
        but2 = types.KeyboardButton(sposob_prig[1])
        but3 = types.KeyboardButton(stop)
        markup1.add(but1, but2).add(but3)
        send = bot.send_message(message.chat.id, f"Похоже ваш друг скрыл свой аккаунт и мы не можем распознать его Chat Id. {text_AttributeError}", reply_markup=markup1)
        bot.register_next_step_handler(send, kmn_rasvetvlenie_mp2)
    kmn2.write("bazakmn2.xml", encoding="UTF-8")

def kmn_odin(message):
    bot.delete_message(message.chat.id, message.id, timeout=0)
    bot.delete_message(message.chat.id, shet[f"{message.chat.id}kmnna1_mesdel"], timeout=0)
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    shet[f"{message.chat.id}kmnna1_bothod"] = random.choice(["Камень", "Ножницы", "Бумага"])
    if message.text.title() in bot_knb and message.text != "/stop":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton(kamen)
        but2 = types.KeyboardButton(noshik)
        but3 = types.KeyboardButton(bumaga)
        but4 = types.KeyboardButton(stop)
        markup.add(but1, but2, but3).add(but4)
        shet[f"{message.chat.id}kmnna1_ighod"] = message.text.title()
        if shet[f"{message.chat.id}kmnna1_ighod"] == shet[f"{message.chat.id}kmnna1_bothod"]:
            shet[f"{message.chat.id}kmnna1_ig"] += int(1)
            shet[f"{message.chat.id}kmnna1_bot"] += int(1)
            bot.edit_message_text(chat_id=message.chat.id, text=f"Ты выбрал: *" + str(shet[f"{message.chat.id}kmnna1_ighod"]) + "*\nБот выбрал: *" + str(shet[f"{message.chat.id}kmnna1_bothod"]) + "*\n\nНичья!\nСчет:\nВы *" + str(shet[f"{message.chat.id}kmnna1_ig"]) + "*:*" + str(shet[f"{message.chat.id}kmnna1_bot"]) +"* Бот", message_id=shet[f"{message.chat.id}kmnna1_mes"], parse_mode="Markdown")
            send = bot.send_message(message.chat.id, "Выберите Камень, Ножницы или Бумагу!", reply_markup=markup)
            bot.register_next_step_handler(send, kmn_odin)
            shet[f"{message.chat.id}kmnna1_mesdel"] = send.message_id
            print(f"{message.chat.id} " + str(shet[f"{message.chat.id}kmnna1_ig"]) + ":" + str(shet[f"{message.chat.id}kmnna1_bot"]) + " бот")
        elif (shet[f"{message.chat.id}kmnna1_ighod"] == kamen and shet[f"{message.chat.id}kmnna1_bothod"] == noshik) or (shet[f"{message.chat.id}kmnna1_ighod"] == noshik and shet[f"{message.chat.id}kmnna1_bothod"] == bumaga) or (shet[f"{message.chat.id}kmnna1_ighod"] == bumaga and shet[f"{message.chat.id}kmnna1_bothod"] == kamen):
            shet[f"{message.chat.id}kmnna1_ig"] += int(1)
            bot.edit_message_text(chat_id=message.chat.id, text=f"Ты выбрал: *" + str(shet[f"{message.chat.id}kmnna1_ighod"]) + "*\nБот выбрал: *" + str(shet[f"{message.chat.id}kmnna1_bothod"]) + "*\n\nТы победил!\nСчет:\nВы *" + str(shet[f"{message.chat.id}kmnna1_ig"]) + "*:*" + str(shet[f"{message.chat.id}kmnna1_bot"]) +"* Бот", message_id=shet[f"{message.chat.id}kmnna1_mes"], parse_mode="Markdown")
            send = bot.send_message(message.chat.id, "Выберите Камень, Ножницы или Бумагу!", reply_markup=markup)
            bot.register_next_step_handler(send, kmn_odin)
            shet[f"{message.chat.id}kmnna1_mesdel"] = send.message_id
            print(f"{message.chat.id} " + str(shet[f"{message.chat.id}kmnna1_ig"]) + ":" + str(shet[f"{message.chat.id}kmnna1_bot"]) + " бот")
        elif (shet[f"{message.chat.id}kmnna1_bothod"] == kamen and shet[f"{message.chat.id}kmnna1_ighod"] == noshik) or (shet[f"{message.chat.id}kmnna1_bothod"] == noshik and shet[f"{message.chat.id}kmnna1_ighod"] == bumaga) or (shet[f"{message.chat.id}kmnna1_bothod"] == bumaga and shet[f"{message.chat.id}kmnna1_ighod"] == kamen):
            shet[f"{message.chat.id}kmnna1_bot"] += int(1)
            bot.edit_message_text(chat_id=message.chat.id, text=f"Ты выбрал: *" + str(shet[f"{message.chat.id}kmnna1_ighod"]) + "*\nБот выбрал: *" + str(shet[f"{message.chat.id}kmnna1_bothod"]) + "*\n\nБот победил!\nСчет:\nВы *" + str(shet[f"{message.chat.id}kmnna1_ig"]) + "*:*" + str(shet[f"{message.chat.id}kmnna1_bot"]) +"* Бот", message_id=shet[f"{message.chat.id}kmnna1_mes"], parse_mode="Markdown")
            send = bot.send_message(message.chat.id, "Выберите Камень, Ножницы или Бумагу!", reply_markup=markup)
            bot.register_next_step_handler(send, kmn_odin)
            shet[f"{message.chat.id}kmnna1_mesdel"] = send.message_id
            print(f"{message.chat.id} " + str(shet[f"{message.chat.id}kmnna1_ig"]) + ":" + str(shet[f"{message.chat.id}kmnna1_bot"]) + " бот")
    elif not message.text.title() in bot_knb and message.text == "/stop":
        bot.edit_message_text(chat_id=message.chat.id, text=f"Вы завершили игру!\nСчет:\nВы *" + str(shet[f"{message.chat.id}kmnna1_ig"]) + "*:*" + str(shet[f"{message.chat.id}kmnna1_bot"]) +"* Бот", message_id=shet[f"{message.chat.id}kmnna1_mes"], parse_mode="Markdown")
        bot.send_message(message.chat.id, "Нажмите кнопку ниже для выхода в меню бота!", reply_markup=markup3)
    elif not message.text.title() in bot_knb and message.text != "/stop":
        send = bot.send_message(message.chat.id, "Ой, не совсем тебя понял, нажми кнопку ниже!", reply_markup=markup)
        bot.register_next_step_handler(send, kmn_odin)
        shet[f"{message.chat.id}kmnna1_mesdel"] = send.message_id

def kmn_mp(message):
    markup4 = types.ReplyKeyboardRemove()
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    markup1 = types.ReplyKeyboardMarkup(True)
    but1 = types.KeyboardButton(sposob_prig[0])
    but2 = types.KeyboardButton(sposob_prig[1])
    but3 = types.KeyboardButton(stop)
    markup1.add(but1, but2).add(but3)
    if message.text.isdigit():
        igrok1 = kmn2.find(f"user{message.chat.id}").attrib["id"]
        user1 = kmn2.find(f"user{message.chat.id}").find("nameig").text
        chat_global_file = open("chat.txt", "r")
        allText = chat_global_file.read()
        spis_chat_id = list(map(str, allText.split()))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Да!')
        but2 = types.KeyboardButton("Нет!")
        markup.add(but1, but2)
        if kmn2.find(f"user{message.chat.id}").find("igrok2") == None:
            igrok = ET.Element("igrok2")
            igrok.attrib["id"] = str(message.text)
            igrok.text = None
            kmn2.find(f"user{message.chat.id}").append(igrok)
        elif kmn2.find(f"user{message.chat.id}").find("igrok2") != None:
            igrok = kmn2.find(f"user{message.chat.id}").find("igrok2")
            igrok.attrib["id"] = str(message.text)
            igrok.text = None
        if kmn2.find(f"user{message.text}") == None:
            igrok2 = ET.Element(f"user{message.text}")
            igrok2.attrib["id"] = str(message.text)
            kmn2r.append(igrok2)
            igrok2 = kmn2.find(f"user{message.text}")
            igrok = ET.Element("nameig")
            igrok.text = None
            igrok2.append(igrok)
            igrok_ = ET.Element("igrok2")
            igrok_.attrib["id"] = str(message.chat.id)
            igrok_.text = user1
            igrok2.append(igrok_)
            igrok2 = kmn2.find(f"user{message.text}").attrib["id"]
        elif kmn2.find(f"user{message.text}") != None:
            igrok2 = kmn2.find(f"user{message.text}").attrib["id"]
            igrok = kmn2.find(f"user{message.text}").find("igrok2")
            igrok.attrib["id"] = str(message.chat.id)
            igrok.text = user1
        if igrok1 != igrok2:
            if igrok2 in spis_chat_id:
                bot.send_message(igrok1, "Отправил приглашение! Ожидай ответа!", reply_markup=markup4)
                send = bot.send_message(igrok2, f"Игрок {user1} прислал вам приглашение, хотите играть?", reply_markup=markup)
                bot.register_next_step_handler(send, kmn_mp_vib_ig1)
            elif not igrok2 in spis_chat_id:
                send = bot.send_message(igrok1, f"Пользователь не найден в базе данных бота! {text2}", parse_mode="Markdown", reply_markup=markup1)
                bot.register_next_step_handler(send, kmn_rasvetvlenie_mp2)
        elif igrok2 == igrok1:
            send = bot.send_message(message.chat.id, f"Извините с самим собой играть нельзя! Выберите заново способ приглашения друга и повторите попытку!\nЧто делать если возникает такая ошибка? Ищите {text}", parse_mode="Markdown", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_rasvetvlenie_mp2)
        chat_global_file.close()
    elif not message.text.isdigit() and message.text != "/stop":
        send = bot.send_message(message.chat.id, "Вводите только цифры!")
        bot.register_next_step_handler(send, kmn_mp)
    elif not message.text.isdigit() and message.text == "/stop":
        bot.send_message(message.chat.id, "Вы остановили выбор, нажмите кнопку ниже!", reply_markup=markup3)
    kmn2.write("bazakmn2.xml", encoding="UTF-8")

def kmn_mp_vib_ig1(message):
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = types.KeyboardButton("/start")
    markup3.add(but5)
    if message.text.title() in slova:
        igrok1 = kmn2.find(f"user{message.chat.id}").find("igrok2").attrib["id"]
        user1 = kmn2.find(f"user{message.chat.id}").find("igrok2").text
        igrok2 = kmn2.find(f"user{message.chat.id}").attrib["id"]
        user2 = kmn2.find(f"user{message.chat.id}").find("nameig")
        user = kmn2.find(f"user{igrok1}").find("igrok2")
        if message.from_user.last_name != None:
            user.text = f"{message.from_user.first_name} {message.from_user.last_name}"
            user2.text = f"{message.from_user.first_name} {message.from_user.last_name}"
        elif message.from_user.last_name == None:
            user.text = str(message.from_user.first_name)
            user2.text = str(message.from_user.first_name)
        user2 = kmn2.find(f"user{message.chat.id}").find("nameig").text
        if message.text.title() == "Да!":
            shet[f"{igrok1}vs{igrok2}_hod{igrok1}"] = 0
            shet[f"{igrok1}vs{igrok2}_hod{igrok2}"] = 0
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            but1 = types.KeyboardButton(kamen)
            but2 = types.KeyboardButton(noshik)
            but3 = types.KeyboardButton(bumaga)
            but4 = types.KeyboardButton(stop)
            markup1.add(but1, but2, but3).add(but4)
            markup2 = types.ReplyKeyboardRemove()
            send1 = bot.send_message(igrok1, "Текущий счёт:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + ":" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + f"* {user2}", parse_mode="Markdown")
            send2 = bot.send_message(igrok2, "Текущий счёт:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + ":" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + f"* {user1}", parse_mode="Markdown")
            send = bot.send_message(igrok1, "Игрок принял приглашение! Выбери Камень, ножницы или бумага!", reply_markup=markup1)
            senddel = bot.send_message(igrok2, f"Вы приняли приглашение от {user1}! Подождите его выбор!", reply_markup=markup2)
            bot.register_next_step_handler(send, kmn_mp_vib_ig2)
            shet[f"{igrok1}vs{igrok2}_ms{igrok1}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}_ms{igrok2}"] = send2.message_id
            shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"] = send.message_id
            shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"] = senddel.message_id
        elif message.text.title() == "Нет!":
            bot.send_message(igrok1, text="Пользователь отклонил приглашение!", reply_markup=markup3)
            bot.send_message(igrok2, text="Вы отклонили приглашение!", reply_markup=markup3)
    elif not message.text.title() in slova:
        send = bot.send_message(message.chat.id, "Ой, не совсем тебя понял, нажми кнопку ниже!")
        bot.register_next_step_handler(send, kmn_mp_vib_ig1)
    kmn2.write("bazakmn2.xml", encoding="utf-8")

def kmn_mp_vib_ig2(message):
    bot.delete_message(message.chat.id, message.message_id, timeout=0)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton(kamen)
    but2 = types.KeyboardButton(noshik)
    but3 = types.KeyboardButton(bumaga)
    but4 = types.KeyboardButton(stop)
    markup1.add(but1, but2, but3).add(but4)
    markup2 = types.ReplyKeyboardRemove()
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = types.KeyboardButton("/start")
    markup3.add(but5)
    igrok1 = kmn2.find(f"user{message.chat.id}").attrib["id"]
    user1 = kmn2.find(f"user{message.chat.id}").find("nameig").text
    igrok2 = kmn2.find(f"user{message.chat.id}").find("igrok2").attrib["id"]
    user2 = kmn2.find(f"user{message.chat.id}").find("igrok2").text
    if message.text.title() in bot_knb and message.text != stop:
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"], timeout=0)
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"], timeout=0)
        shet[f"{igrok1}vs{igrok2}_zn{igrok1}"] = message.text.title()
        senddel = bot.send_message(igrok1, "Передали пользователю шанс выбора!", reply_markup=markup2)
        send = bot.send_message(igrok2, "Игрок выбрал! Выбери Камень, ножницы или бумагу!", reply_markup=markup1)
        bot.register_next_step_handler(send, kmn_mp_itog)
        shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"] = senddel.message_id
        shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"] = send.message_id
    elif not message.text.title() in bot_knb and message.text == "/stop":
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"], timeout=0)
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"], timeout=0)
        bot.edit_message_text(chat_id=igrok1, text=f"Вы завершили игру!\nОбщий счет:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + "*:*" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + f"* {user2}", message_id=shet[f"{igrok1}vs{igrok2}_ms{igrok1}"], parse_mode="Markdown")
        bot.edit_message_text(chat_id=igrok2, text=f"{user1} завершил игру!\nОбщий счет:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + "*:*" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + f"* {user1}", message_id=shet[f"{igrok1}vs{igrok2}_ms{igrok2}"], parse_mode="Markdown")
        bot.send_message(igrok1, "Для выхода в меню бота нажмите кнопку ниже!", reply_markup=markup3)
        bot.send_message(igrok2, "Для выхода в меню бота нажмите кнопку ниже!", reply_markup=markup3)
    elif not message.text.title() in bot_knb and message.text != "/stop":
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"], timeout=0)
        send = bot.send_message(chat_id=igrok1, text="Ой, не совсем тебя понял, нажми кнопку ниже!", reply_markup=markup1)
        bot.register_next_step_handler(send, kmn_mp_vib_ig2)
        shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"] = send.message_id

def kmn_mp_itog(message):
    bot.delete_message(message.chat.id, message.message_id, timeout=0)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton(kamen)
    but2 = types.KeyboardButton(noshik)
    but3 = types.KeyboardButton(bumaga)
    but4 = types.KeyboardButton(stop)
    markup1.add(but1, but2, but3).add(but4)
    markup2 = types.ReplyKeyboardRemove()
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    igrok2 = kmn2.find(f"user{message.chat.id}").attrib["id"]
    user2 = kmn2.find(f"user{message.chat.id}").find("nameig").text
    igrok1 = kmn2.find(f"user{message.chat.id}").find("igrok2").attrib["id"]
    user1 = kmn2.find(f"user{message.chat.id}").find("igrok2").text
    if message.text.title() in bot_knb and message.text != stop:
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"], timeout=0)
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"], timeout=0)
        shet[f"{igrok1}vs{igrok2}_zn{igrok2}"] = message.text.title()
        if shet[f"{igrok1}vs{igrok2}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}_zn{igrok2}"]:
            shet[f"{igrok1}vs{igrok2}_hod{igrok1}"] += 1
            shet[f"{igrok1}vs{igrok2}_hod{igrok2}"] += 1
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok2}"]) + "*\n\nНичья!\nТекущий счет:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + "*:*" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + f"* {user2}", message_id=shet[f"{igrok1}vs{igrok2}_ms{igrok1}"], parse_mode="Markdown")
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok1}"]) + "*\n\nНичья!\nТекущий счет:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + "*:*" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + f"* {user1}", message_id=shet[f"{igrok1}vs{igrok2}_ms{igrok2}"], parse_mode="Markdown")
            send1 = bot.send_message(chat_id=igrok1, text="Выберите Камень, ножницы или бумагу!", reply_markup=markup1)
            senddel = bot.send_message(chat_id=igrok2, text="Подожди выбор первого пользователя!", reply_markup=markup2)
            bot.register_next_step_handler(send1, kmn_mp_vib_ig2)
            shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"] = senddel.message_id
        elif (shet[f"{igrok1}vs{igrok2}_zn{igrok1}"] == kamen and shet[f"{igrok1}vs{igrok2}_zn{igrok2}"] == noshik) or (shet[f"{igrok1}vs{igrok2}_zn{igrok1}"] == noshik and shet[f"{igrok1}vs{igrok2}_zn{igrok2}"] == bumaga) or (shet[f"{igrok1}vs{igrok2}_zn{igrok1}"] == bumaga and shet[f"{igrok1}vs{igrok2}_zn{igrok2}"] == kamen):
            shet[f"{igrok1}vs{igrok2}_hod{igrok1}"] += 1
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok2}"]) + "*\n\nТы победил!\nТекущий счет:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + "*:*" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + f"* {user2}", message_id=shet[f"{igrok1}vs{igrok2}_ms{igrok1}"], parse_mode="Markdown")
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok1}"]) + f"*\n\n{user1} победил!\nТекущий счет:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + "*:*" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + f"* {user1}", message_id=shet[f"{igrok1}vs{igrok2}_ms{igrok2}"], parse_mode="Markdown")
            send1 = bot.send_message(chat_id=igrok1, text="Выберите Камень, ножницы или бумагу первыми!", reply_markup=markup1)
            senddel = bot.send_message(chat_id=igrok2, text="Подожди выбор первого пользователя!", reply_markup=markup2)
            bot.register_next_step_handler(send1, kmn_mp_vib_ig2)
            shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"] = senddel.message_id
        elif (shet[f"{igrok1}vs{igrok2}_zn{igrok1}"] == kamen and shet[f"{igrok1}vs{igrok2}_zn{igrok2}"] == bumaga) or (shet[f"{igrok1}vs{igrok2}_zn{igrok1}"] == noshik and shet[f"{igrok1}vs{igrok2}_zn{igrok2}"] == kamen) or (shet[f"{igrok1}vs{igrok2}_zn{igrok1}"] == bumaga and shet[f"{igrok1}vs{igrok2}_zn{igrok2}"] == noshik):
            shet[f"{igrok1}vs{igrok2}_hod{igrok2}"] += 1
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok1}"]) + "*\n\nТы победил!\nТекущий счет:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + "*:*" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + f"* {user1}", message_id=shet[f"{igrok1}vs{igrok2}_ms{igrok2}"], parse_mode="Markdown")
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}_zn{igrok2}"]) + f"*\n\n{user2} победил!\nТекущий счет:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + "*:*" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + f"* {user2}", message_id=shet[f"{igrok1}vs{igrok2}_ms{igrok1}"], parse_mode="Markdown")
            send1 = bot.send_message(chat_id=igrok1, text="Выберите Камень, ножницы или бумагу первыми!", reply_markup=markup1)
            senddel = bot.send_message(chat_id=igrok2, text="Подожди выбор первого пользователя!", reply_markup=markup2)
            bot.register_next_step_handler(send1, kmn_mp_vib_ig2)
            shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"] = senddel.message_id
        print(f"Текущий счет:\n{user1} " + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + ":" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + f" {user2}")
    elif not message.text.title() in bot_knb and message.text == stop:
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"], timeout=0)
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"], timeout=0)
        bot.edit_message_text(chat_id=igrok2, text=f"Вы завершили игру!\nОбщий счет:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + "*:*" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + f"* {user1}", message_id=shet[f"{igrok1}vs{igrok2}_ms{igrok2}"], parse_mode="Markdown")
        bot.edit_message_text(chat_id=igrok1, text=f"{user2} завершил игру!\nОбщий счет:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + "*:*" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + f"* {user2}", message_id=shet[f"{igrok1}vs{igrok2}_ms{igrok1}"], parse_mode="Markdown")
        bot.send_message(igrok1, "Для выхода в меню бота нажмите кнопку ниже!", reply_markup=markup3)
        bot.send_message(igrok2, "Для выхода в меню бота нажмите кнопку ниже!", reply_markup=markup3)
    elif not message.text.title() in bot_knb and message.text != stop:
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"], timeout=0)
        send = bot.send_message(chat_id=igrok2, text="Ой, не совсем тебя понял, нажми кнопку ниже!", reply_markup=markup1)
        bot.register_next_step_handler(send, kmn_mp_itog)
        shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"] = send.message_id
def kmn_rasvetvlenie_mp3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("/stop")
    markup.add(but1)
    markup1 = types.ReplyKeyboardRemove()
    markup2 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton("/start")
    markup2.add(but2)
    if message.text.title() in sposob_prig:
        if message.text.title() == sposob_prig[0]:
            send = bot.send_message(message.chat.id, "Отлично! Отправьте мне сообщение от друга!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_mp_3_priglas_ig2_message)
        elif message.text.title() == sposob_prig[1]:
            p = open("Важное фото.png", "rb")
            send = bot.send_photo(message.chat.id, photo=p, caption=text_photo, reply_markup=markup, parse_mode="Markdown")
            bot.register_next_step_handler(send, kmn_mp_3_priglas_ig2)
    elif not message.text.title() in sposob_prig and message.text != stop:
        send = bot.send_message(message.chat.id, "Ой, не совсем тебя понял, нажми кнопку ниже!")
        bot.register_next_step_handler(send, kmn_rasvetvlenie_mp3)
    elif not message.text.title() in sposob_prig and message.text == stop:
        bot.send_message(message.chat.id, "Вы остановили процесс приглашение пользователя!", reply_markup=markup2)

def kmn_mp_3_priglas_ig2_message(message):
    bot.delete_message(message.chat.id, message.message_id, timeout=0)
    markup1 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton("Через сообщения от друга")
    but3 = types.KeyboardButton("Через Chat Id")
    but4 = types.KeyboardButton("/stop")
    markup1.add(but2, but3).add(but4)
    igrok1 = kmn3.find(f"user{message.chat.id}").attrib["id"]
    user1 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    try:
        markup = types.ReplyKeyboardMarkup(True)
        but1 = types.KeyboardButton(slova[0])
        but2 = types.KeyboardButton(slova[1])
        markup.add(but1, but2)
        chat_global_file = open("chat.txt", "r")
        allText = chat_global_file.read()
        spis_chat_id = list(map(str, allText.split()))
        if kmn3.find(f"user{message.chat.id}").find("igroki") == None:
            igrok = ET.Element("igroki")
            igroki = ET.Element("igrok2")
            igroki.attrib["id"] = str(message.forward_from.id)
            igroki.text = None
            igrok.append(igroki)
            kmn3.find(f"user{message.chat.id}").append(igrok)
        elif kmn3.find(f"user{message.chat.id}").find("igroki") != None:
            igrok = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2")
            igrok.attrib["id"] = str(message.forward_from.id)
            igrok.text = None
        if kmn3.find(f"user{message.forward_from.id}") == None:
            igrok2 = ET.Element(f"user{message.forward_from.id}")
            igrok2.attrib["id"] = str(message.forward_from.id)
            kmn3r.append(igrok2)
            igrok2 = kmn3.find(f"user{message.forward_from.id}")
            igrok = ET.Element("nameig")
            igrok.text = None
            igrok2.append(igrok)
            igrok__ = ET.Element("igroki")
            igrok_ = ET.Element("igrok2")
            igrok_.attrib["id"] = str(message.chat.id)
            igrok_.text = user1
            igrok__.append(igrok_)
            igrok2.append(igrok__)
            igrok2 = kmn3.find(f"user{message.forward_from.id}").attrib["id"]
        elif kmn3.find(f"user{message.forward_from.id}") != None:
            igrok2 = kmn3.find(f"user{message.forward_from.id}").attrib["id"]
            igrok = kmn3.find(f"user{message.forward_from.id}").find("igroki").find("igrok2")
            igrok.attrib["id"] = str(message.chat.id)
            igrok.text = user1
        if igrok1 != igrok2:
            if igrok2 in spis_chat_id:
                bot.send_message(chat_id=igrok1, text="Отправил приглашение! Ожидай ответа!")
                send = bot.send_message(chat_id=igrok2, text=f"Игрок {user1} прислал вам приглашение, хотите играть?", reply_markup=markup)
                bot.register_next_step_handler(send, kmn_mp_3)
            elif not igrok2 in spis_chat_id:
                send = bot.send_message(igrok1, f"Пользователь не найден в базе данных бота! {text2}", parse_mode="Markdown")
                bot.register_next_step_handler(send, kmn_rasvetvlenie_mp3)
        elif igrok2 == igrok1:
            send = bot.send_message(message.chat.id, f"Извините с самим собой играть нельзя! Выберите способ приглашения друга снова и попробуйте еще раз!\nЧто делать если возникает такая ошибка? Ищите {text}", parse_mode="Markdown", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_rasvetvlenie_mp3)
    except AttributeError:
        send = bot.send_message(igrok1, f"Похоже ваш друг скрыл свой аккаунт и мы не можем распознать его Chat Id. {text_AttributeError}", reply_markup=markup1)
        bot.register_next_step_handler(send, kmn_rasvetvlenie_mp3)
    kmn3.write("bazakmn3.xml", encoding="UTF-8")

def kmn_mp_3_priglas_ig2(message):
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    markup1 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton(sposob_prig[0])
    but3 = types.KeyboardButton(sposob_prig[1])
    but4 = types.KeyboardButton(stop)
    markup1.add(but2, but3).add(but4)
    igrok1 = kmn3.find(f"user{message.chat.id}").attrib["id"]
    user1 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    if message.text.isdigit():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("Да!")
        but2 = types.KeyboardButton("Нет!")
        markup.add(but1, but2)
        chat_global_file = open("chat.txt", "r")
        allText = chat_global_file.read()
        spis_chat_id = list(map(str, allText.split()))
        if kmn3.find(f"user{message.chat.id}").find("igroki") == None:
            igrok = ET.Element("igroki")
            igroki = ET.Element("igrok2")
            igroki.attrib["id"] = str(message.text)
            igroki.text = None
            igrok.append(igroki)
            kmn3.find(f"user{message.chat.id}").append(igrok)
        elif kmn3.find(f"user{message.chat.id}").find("igroki") != None:
            igrok = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2")
            igrok.attrib["id"] = str(message.text)
            igrok.text = None
        if kmn3.find(f"user{message.text}") == None:
            igrok2 = ET.Element(f"user{message.text}")
            igrok2.attrib["id"] = str(message.text)
            kmn3r.append(igrok2)
            igrok2 = kmn3.find(f"user{message.text}")
            igrok = ET.Element("nameig")
            igrok.text = None
            igrok2.append(igrok)
            igrok__ = ET.Element("igroki")
            igrok_ = ET.Element("igrok2")
            igrok_.attrib["id"] = str(message.chat.id)
            igrok_.text = user1
            igrok__.append(igrok_)
            igrok2.append(igrok__)
            igrok2 = kmn3.find(f"user{message.text}").attrib["id"]
        elif kmn3.find(f"user{message.text}") != None:
            igrok2 = kmn3.find(f"user{message.text}").attrib["id"]
            igrok = kmn3.find(f"user{message.text}").find("igroki").find("igrok2")
            igrok.attrib["id"] = str(message.chat.id)
            igrok.text = user1
        if igrok1 != igrok2:
            if igrok2 in spis_chat_id:
                bot.send_message(igrok1, "Отправил приглашение! Ожидайте ответа!")
                send = bot.send_message(igrok2, f"Пользователь {user1} прислал вам приглашение! Хотите ли вы с ним поиграть?", reply_markup=markup)
                bot.register_next_step_handler(send, kmn_mp_3)
            elif not igrok2 in spis_chat_id:
                send = bot.send_message(igrok1, f"Пользователь не найден в базе данных бота! {text2}", parse_mode="Markdown", reply_markup=markup1)
                bot.register_next_step_handler(send, kmn_rasvetvlenie_mp3)
        elif igrok2 == igrok1:
            send = bot.send_message(message.chat.id, f"Извините с самим собой играть нельзя! {text3}\nЧто делать если возникает такая ошибка? Ищите {text}", parse_mode="Markdown", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_rasvetvlenie_mp3)
        chat_global_file.close()
    elif not message.text.isdigit() and message.text != "/stop":
        send = bot.send_message(chat_id=igrok1, text="Вводите только цифры!")
        bot.register_next_step_handler(send, kmn_mp_3_priglas_ig2)
    elif not message.text.isdigit() and message.text == "/stop":
        bot.send_message(message.chat.id, "Вы остановили выбор, нажмите кнопку ниже!", reply_markup=markup3)
    kmn3.write("bazakmn3.xml", encoding="UTF-8")

def kmn_mp_3(message):
    igrok1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib["id"]
    user1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
    igrok2 = kmn3.find(f"user{message.chat.id}").attrib["id"]
    user2 = kmn3.find(f"user{message.chat.id}").find("nameig")
    user = kmn3.find(f"user{igrok1}").find("igroki").find("igrok2")
    if message.from_user.last_name == None:
        user.text = str(message.from_user.first_name)
        user2.text = str(message.from_user.first_name)
    elif message.from_user.last_name != None:
        user.text = f"{message.from_user.first_name} {message.from_user.last_name}"
        user2.text = f"{message.from_user.first_name} {message.from_user.last_name}"
    user2 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    markup = types.ReplyKeyboardRemove()
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = types.KeyboardButton("/start")
    markup2.add(but5)
    markup1 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton("Я")
    but3 = types.KeyboardButton("Игрок 2")
    markup1.add(but2, but3)
    if message.text.title() in vib:
        if message.text.title() == "Да!":
            send = bot.send_message(igrok1, f"{user2} принял приглашение! Выберите кто будет приглашать игрока 3 (это очень важно!)!", reply_markup=markup1)
            bot.send_message(igrok2, "Окей! Ждем решения первого игрока!", reply_markup=markup)
            bot.register_next_step_handler(send, kmn_peredacha_vib)
        elif message.text.title() == "Нет!":
            bot.send_message(igrok1, f"Пользователь {user2} отклонил приглашение!", reply_markup=markup2)
            bot.send_message(igrok2, "Вы отклонили приглашение!", reply_markup=markup2)
    elif not message.text.title() in vib:
        send = bot.send_message(igrok2, "Вы кажется не то ввели. Нажмите кнопку ниже!")
        bot.register_next_step_handler(send, kmn_mp_3)
    kmn3.write("bazakmn3.xml", encoding="UTF-8")

def kmn_peredacha_vib(message):
    markup1 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton(sposob_prig[0])
    but3 = types.KeyboardButton(sposob_prig[1])
    markup1.add(but2, but3)
    igrok1 = kmn3.find(f"user{message.chat.id}").attrib["id"]
    user1 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    igrok2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib["id"]
    user2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
    if message.text.title() in kto_priglasit:
        if message.text.title() == "Я":
            send = bot.send_message(igrok1, "Окей, приняли! Пожалуйста, выберите способ приглашения друга ниже!", reply_markup=markup1)
            bot.send_message(igrok2, f"Подождите! {user1} сейчас кого-то пригласит!")
            bot.register_next_step_handler(send, kmn_peredacha_vib0)
        elif message.text.title() == "Игрок 2":
            bot.send_message(igrok1, f"Окей, передали возможность {user2}! Подождите пока он пригласит кого-нибудь.", reply_markup=types.ReplyKeyboardRemove())
            send = bot.send_message(igrok2, f"{user1} передал вам возможность приглашения друга! Пожалуйста выберите способ приглашения друга ниже!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_peredacha_vib1)
    elif not message.text.title() in kto_priglasit:
        send = bot.send_message(igrok1, "Вы кажется не то ввели. Нажмите кнопку ниже!")
        bot.register_next_step_handler(send, kmn_peredacha_vib)

def kmn_peredacha_vib1(message):
    igrok2 = kmn3.find(f"user{message.chat.id}").attrib["id"]
    user2 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    igrok1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
    user1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
    markup1 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton(sposob_prig[0])
    but3 = types.KeyboardButton(sposob_prig[1])
    markup1.add(but2, but3)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("/stop")
    markup.add(but1)
    markup2 = types.ReplyKeyboardRemove()
    markup3 = types.ReplyKeyboardMarkup(True)
    but4 = types.KeyboardButton("/start")
    markup3.add(but4)
    if message.text.title() in sposob_prig:
        if message.text.title() == sposob_prig[0]:
            send = bot.send_message(igrok2, "Отлично! Отправьте мне сообщение от друга!", reply_markup=markup2)
            bot.register_next_step_handler(send, kmn_mp_3_priglas_ig3_ig2_message)
        elif message.text.title() == sposob_prig[1]:
            p = open("Важное фото.png", "rb")
            send = bot.send_photo(igrok2, photo=p, caption=text_photo, reply_markup=markup2, parse_mode="Markdown")
            bot.register_next_step_handler(send, kmn_peredacha)
    elif not message.text.title() in sposob_prig and message.text != stop:
        send = bot.send_message(igrok2, "Ой, не совсем тебя понял, нажми кнопку ниже!")
        bot.register_next_step_handler(send, kmn_peredacha_vib1)
    elif not message.text.title() in sposob_prig and message.text == stop:
        bot.send_message(igrok2, "Вы приняли решение завершить игру!", reply_markup=markup3)
        bot.send_message(igrok1, f"{user2} принял решение завершить игру!", reply_markup=markup3)

def kmn_peredacha_vib0(message):
    igrok1 = kmn3.find(f"user{message.chat.id}").attrib["id"]
    user1 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    igrok2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
    user2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
    markup1 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton(sposob_prig[0])
    but3 = types.KeyboardButton(sposob_prig[1])
    markup1.add(but2, but3)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("/stop")
    markup.add(but1)
    markup2 = types.ReplyKeyboardRemove()
    markup3 = types.ReplyKeyboardMarkup(True)
    but4 = types.KeyboardButton("/start")
    markup3.add(but4)
    if message.text.title() in sposob_prig:
        if message.text.title() == sposob_prig[0]:
            send = bot.send_message(igrok1, "Отлично! Отправьте мне сообщение от друга!", reply_markup=markup2)
            bot.register_next_step_handler(send, kmn_mp_3_priglas_ig3_message)
        elif message.text.title() == sposob_prig[1]:
            p = open("Важное фото.png", "rb")
            send = bot.send_photo(igrok1, photo=p, caption=text_photo, reply_markup=markup2, parse_mode="Markdown")
            bot.register_next_step_handler(send, kmn_mp_3_1)
    elif not message.text.title() in sposob_prig and message.text != stop:
        send = bot.send_message(igrok1, "Ой, не совсем тебя понял, нажми кнопку ниже!")
        bot.register_next_step_handler(send, kmn_peredacha_vib0)
    elif not message.text.title() in sposob_prig and message.text == stop:
        bot.send_message(igrok1, "Вы приняли решение завершить игру!", reply_markup=markup3)
        bot.send_message(igrok2, f"{user1} принял решение завершить игру!", reply_markup=markup3)

def kmn_peredacha(message):
    markup4 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton(sposob_prig[0])
    but3 = types.KeyboardButton(sposob_prig[1])
    but5 = types.KeyboardButton(stop)
    markup4.add(but2, but3).add(but5)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да!")
    but2 = types.KeyboardButton("Нет!")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("Передать возможность первому игроку")
    markup1.add(but)
    markup2 = types.ReplyKeyboardRemove()
    markup3 = types.ReplyKeyboardMarkup(True)
    but4 = types.KeyboardButton("/start")
    markup3.add(but4)
    igrok1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib["id"]
    user1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
    igrok2 = kmn3.find(f"user{message.chat.id}").attrib['id']
    user2 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    if message.text.isdigit():
        chat_global_file = open("chat.txt", "r")
        allText = chat_global_file.read()
        spis_chat_id = list(map(str, allText.split()))
        if kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3") == None:
            igrok = ET.Element("igrok3")
            igrok.attrib['id'] = str(message.text)
            igrok.text = None
            kmn3.find(f"user{message.chat.id}").find("igroki").append(igrok)
        elif kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3") != None:
            igrok = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3")
            igrok.attrib['id'] = str(message.text)
            igrok.text = None
        if kmn3.find(f"user{igrok1}").find("igroki").find("igrok3") == None:
            igrok = ET.Element("igrok3")
            igrok.attrib['id'] = str(message.text)
            igrok.text = None
            kmn3.find(f"user{igrok1}").find("igroki").append(igrok)
        elif kmn3.find(f"user{igrok1}").find("igroki").find("igrok3") != None:
            igrok = kmn3.find(f"user{igrok1}").find("igroki").find("igrok3")
            igrok.attrib['id'] = str(message.text)
            igrok.text = None
        if kmn3.find(f"user{message.text}") == None:
            igrok = ET.Element(f"user{message.text}")
            igrok.attrib['id'] = str(message.text)
            ig = ET.Element("nameig")
            ig.text = None
            igrok.append(ig)
            ig3 = ET.Element("igroki")
            ig1 = ET.Element("igrok2")
            ig1.attrib['id'] = igrok1
            ig1.text = user1
            ig3.append(ig1)
            ig2 = ET.Element("igrok3")
            ig2.attrib['id'] = igrok2
            ig2.text = user2
            ig3.append(ig2)
            igrok.append(ig3)
            kmn3r.append(igrok)
            igrok3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
        elif kmn3.find(f"user{message.text}") != None:
            igrok = kmn3.find(f"user{message.text}")
            if igrok.find("igroki") == None:
                ig = ET.Element("igroki")
                ig1 = ET.Element("igrok2")
                ig1.attrib['id'] = igrok1
                ig1.text = user1
                ig.append(ig1)
                ig2 = ET.Element("igrok3")
                ig2.attrib['id'] = igrok2
                ig2.text = user2
                ig.append(ig2)
                igrok.append(ig)
            elif igrok.find("igroki") != None:
                igroki = igrok.find("igroki")
                if igroki.find("igrok2") == None:
                    ig = ET.Element("igrok2")
                    ig.attrib['id'] = igrok1
                    ig.text = user1
                    igroki.append(ig)
                elif igroki.find("igrok2") != None:
                    ig = igroki.find("igrok2")
                    ig.attrib['id'] = igrok1
                    ig.text = user1
                if igroki.find("igrok3") == None:
                    ig = ET.Element("igrok3")
                    ig.attrib['id'] = igrok2
                    ig.text = user2
                    igroki.append(ig)
                elif igroki.find("igrok3") != None:
                    ig = igroki.find("igrok3")
                    ig.attrib['id'] = igrok2
                    ig.text = user2
            igrok3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
        if igrok1 != igrok3 and igrok2 != igrok3:
            if igrok3 in spis_chat_id:
                bot.send_message(igrok1, "Подождите еще! Отправили приглашение третьему другу!", reply_markup=markup2)
                bot.send_message(igrok2, "Приняли! Ожидайте ответа!", reply_markup=markup2)
                send = bot.send_message(igrok3, f"{user1} и {user2} отправили вам приглашение сыграть вместе в игру Камень-ножницы-бумага! Вы согласны?", reply_markup=markup)
                bot.register_next_step_handler(send, kmn_vib_ig1_3)
            elif not igrok3 in spis_chat_id:
                send = bot.send_message(igrok2, f"Пользователь не найден в базе данных бота! {text2}", parse_mode="Markdown", reply_markup=markup4)
                bot.register_next_step_handler(send, kmn_peredacha_vib1)
        elif igrok1 == igrok3 or igrok2 == igrok3:
            send = bot.send_message(igrok2, f"Извините с самим собой играть нельзя! {text3}\nЧто делать если возникает такая ошибка? Ищите {text}", parse_mode="Markdown", reply_markup=markup4)
            bot.register_next_step_handler(send, kmn_peredacha_vib1)
        chat_global_file.close()
    elif not message.text.isdigit():
        send = bot.send_message(igrok2, "Ой, мы кажется вас не поняли! Отправьте мне сюда только цифры!")
        bot.register_next_step_handler(send, kmn_peredacha)
    kmn3.write("bazakmn3.xml", encoding="UTF-8")

def kmn_mp_3_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да!")
    but2 = types.KeyboardButton("Нет!")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("Передать возможность второму игроку")
    markup1.add(but)
    markup3 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton(sposob_prig[0])
    but3 = types.KeyboardButton(sposob_prig[1])
    but5 = types.KeyboardButton(stop)
    markup3.add(but2, but3).add(but5)
    markup2 = types.ReplyKeyboardRemove()
    igrok1 = kmn3.find(f"user{message.chat.id}").attrib['id']
    user1 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    igrok2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
    user2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
    if message.text.isdigit():
        chat_global_file = open("chat.txt", "r")
        allText = chat_global_file.read()
        spis_chat_id = list(map(str, allText.split()))
        if kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3") == None:
            igrok = ET.Element("igrok3")
            igrok.attrib['id'] = str(message.text)
            igrok.text = None
            kmn3.find(f"user{message.chat.id}").find("igroki").append(igrok)
        elif kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3") != None:
            igrok = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3")
            igrok.attrib['id'] = str(message.text)
            igrok.text = None
        if kmn3.find(f"user{igrok2}").find("igroki").find("igrok3") == None:
            igrok = ET.Element("igrok3")
            igrok.attrib['id'] = str(message.text)
            igrok.text = None
            kmn3.find(f"user{igrok2}").find("igroki").append(igrok)
        elif kmn3.find(f"user{igrok2}").find("igroki").find("igrok3") != None:
            igrok = kmn3.find(f"user{igrok2}").find("igroki").find("igrok3")
            igrok.attrib['id'] = str(message.text)
            igrok.text = None
        if kmn3.find(f"user{message.text}") == None:
            igrok = ET.Element(f"user{message.text}")
            igrok.attrib['id'] = str(message.text)
            ig = ET.Element("nameig")
            ig.text = None
            igrok.append(ig)
            ig3 = ET.Element("igroki")
            ig1 = ET.Element("igrok2")
            ig1.attrib['id'] = igrok1
            ig1.text = user1
            ig3.append(ig1)
            ig2 = ET.Element("igrok3")
            ig2.attrib['id'] = igrok2
            ig2.text = user2
            ig3.append(ig2)
            igrok.append(ig3)
            kmn3r.append(igrok)
            igrok3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
        elif kmn3.find(f"user{message.text}") != None:
            igrok = kmn3.find(f"user{message.text}")
            if igrok.find("igroki") == None:
                ig = ET.Element("igroki")
                ig1 = ET.Element("igrok2")
                ig1.attrib['id'] = igrok1
                ig1.text = user1
                ig.append(ig1)
                ig2 = ET.Element("igrok3")
                ig2.attrib['id'] = igrok2
                ig2.text = user2
                ig.append(ig2)
                igrok.append(ig)
            elif igrok.find("igroki") != None:
                igroki = igrok.find("igroki")
                if igroki.find("igrok2") == None:
                    ig = ET.Element("igrok2")
                    ig.attrib['id'] = igrok1
                    ig.text = user1
                    igroki.append(ig)
                elif igroki.find("igrok2") != None:
                    ig = igroki.find("igrok2")
                    ig.attrib['id'] = igrok1
                    ig.text = user1
                if igroki.find("igrok3") == None:
                    ig = ET.Element("igrok3")
                    ig.attrib['id'] = igrok2
                    ig.text = user2
                    igroki.append(ig)
                elif igroki.find("igrok3") != None:
                    ig = igroki.find("igrok3")
                    ig.attrib['id'] = igrok2
                    ig.text = user2
            igrok3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
        if igrok1 != igrok3 and igrok2 != igrok3:
            if igrok3 in spis_chat_id:
                bot.send_message(igrok1, "Приняли! Ожидайте ответа!", reply_markup=markup2)
                bot.send_message(igrok2, "Подождите еще! Отправили приглашение третьему другу!", reply_markup=markup2)
                send = bot.send_message(igrok3, f"{user1} и {user2} отправили вам приглашение сыграть вместе в игру Камень-ножницы-бумага! Вы согласны?", reply_markup=markup)
                bot.register_next_step_handler(send, kmn_vib_ig1_3)
            elif not igrok3 in spis_chat_id:
                send = bot.send_message(igrok1, f"Пользователь не найден в базе данных бота! {text2}", parse_mode="Markdown", reply_markup=markup3)
                bot.register_next_step_handler(send, kmn_peredacha_vib0)
        elif igrok1 == igrok3 or igrok2 == igrok3:
            send = bot.send_message(message.chat.id, f"Извините с самим собой играть нельзя! Выберите способ приглашения друга снова и попробуйте еще раз!\nЧто делать если возникает такая ошибка? Ищите {text}", parse_mode="Markdown", reply_markup=markup3)
            bot.register_next_step_handler(send, kmn_peredacha_vib0)
        chat_global_file.close()
    elif not message.text.isdigit():
        send = bot.send_message(igrok1, "Ой, мы кажется вас не поняли! Отправьте мне сюда только цифры")
        bot.register_next_step_handler(send, kmn_mp_3_1)
    kmn3.write("bazakmn3.xml", encoding="UTF-8")

def kmn_mp_3_priglas_ig3_message(message):
    bot.delete_message(message.chat.id, message.message_id, timeout=0)
    markup1 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton(sposob_prig[0])
    but3 = types.KeyboardButton(sposob_prig[1])
    but5 = types.KeyboardButton(stop)
    markup1.add(but2, but3).add(but5)
    try:
        igrok1 = kmn3.find(f"user{message.chat.id}").attrib['id']
        user1 = kmn3.find(f"user{message.chat.id}").find("nameig").text
        igrok2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
        user2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
        markup = types.ReplyKeyboardMarkup(True)
        but1 = types.KeyboardButton(slova[0])
        but2 = types.KeyboardButton(slova[1])
        markup.add(but1, but2)
        chat_global_file = open("chat.txt", "r")
        text2 = f"Попросите вашего друга зайти в бот и нажать кнопку /start, а потом заново выберите способ приглашения друга и повторите попытку, либо нажмите {stop} для прекращения приглашений друга!!\nОшибка повторяется? Ответ ищите [здесь](https://t.me/kontrol_chek185/1131)"
        allText = chat_global_file.read()
        spis_chat_id = list(map(str, allText.split()))
        text = "[здесь](https://t.me/kontrol_chek185/1131)"
        markup2 = types.ReplyKeyboardRemove()
        if kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3") == None:
            igrok = ET.Element("igrok3")
            igrok.attrib['id'] = str(message.forward_from.id)
            igrok.text = None
            kmn3.find(f"user{message.chat.id}").find("igroki").append(igrok)
        elif kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3") != None:
            igrok = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3")
            igrok.attrib['id'] = str(message.forward_from.id)
            igrok.text = None
        if kmn3.find(f"user{igrok2}").find("igroki").find("igrok3") == None:
            igrok = ET.Element("igrok3")
            igrok.attrib['id'] = str(message.forward_from.id)
            igrok.text = None
            kmn3.find(f"user{igrok2}").find("igroki").append(igrok)
        elif kmn3.find(f"user{igrok2}").find("igroki").find("igrok3") != None:
            igrok = kmn3.find(f"user{igrok2}").find("igroki").find("igrok3")
            igrok.attrib['id'] = str(message.forward_from.id)
            igrok.text = None
        if kmn3.find(f"user{message.forward_from.id}") == None:
            igrok = ET.Element(f"user{message.forward_from.id}")
            igrok.attrib['id'] = str(message.forward_from.id)
            ig = ET.Element("nameig")
            ig.text = None
            igrok.append(ig)
            ig3 = ET.Element("igroki")
            ig1 = ET.Element("igrok2")
            ig1.attrib['id'] = igrok1
            ig1.text = user1
            ig3.append(ig1)
            ig2 = ET.Element("igrok3")
            ig2.attrib['id'] = igrok2
            ig2.text = user2
            ig3.append(ig2)
            igrok.append(ig3)
            kmn3r.append(igrok)
            igrok3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
        elif kmn3.find(f"user{message.forward_from.id}") != None:
            igrok = kmn3.find(f"user{message.forward_from.id}")
            if igrok.find("igroki") == None:
                ig = ET.Element("igroki")
                ig1 = ET.Element("igrok2")
                ig1.attrib['id'] = igrok1
                ig1.text = user1
                ig.append(ig1)
                ig2 = ET.Element("igrok3")
                ig2.attrib['id'] = igrok2
                ig2.text = user2
                ig.append(ig2)
                igrok.append(ig)
            elif igrok.find("igroki") != None:
                igroki = igrok.find("igroki")
                if igroki.find("igrok2") == None:
                    ig = ET.Element("igrok2")
                    ig.attrib['id'] = igrok1
                    ig.text = user1
                    igroki.append(ig)
                elif igroki.find("igrok2") != None:
                    ig = igroki.find("igrok2")
                    ig.attrib['id'] = igrok1
                    ig.text = user1
                if igroki.find("igrok3") == None:
                    ig = ET.Element("igrok3")
                    ig.attrib['id'] = igrok2
                    ig.text = user2
                    igroki.append(ig)
                elif igroki.find("igrok3") != None:
                    ig = igroki.find("igrok3")
                    ig.attrib['id'] = igrok2
                    ig.text = user2
            igrok3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
        if igrok1 != igrok3 and igrok2 != igrok3:
            if igrok3 in spis_chat_id:
                bot.send_message(igrok1, "Приняли! Ожидайте ответа!", reply_markup=markup2)
                bot.send_message(igrok2, "Подождите еще! Отправили приглашение третьему другу!", reply_markup=markup2)
                send = bot.send_message(igrok3, f"{user1} и {user2} отправили вам приглашение сыграть вместе в игру Камень-ножницы-бумага! Вы согласны?", reply_markup=markup)
                bot.register_next_step_handler(send, kmn_vib_ig1_3)
            elif not igrok3 in spis_chat_id:
                send = bot.send_message(igrok1, f"Пользователь не найден в базе данных бота! {text2}", parse_mode="Markdown", reply_markup=markup1)
                bot.register_next_step_handler(send, kmn_peredacha_vib0)
        elif igrok1 == igrok3 or igrok2 == igrok3:
            send = bot.send_message(message.chat.id, f"Извините с самим собой играть нельзя! Выберите способ приглашения друга снова и попробуйте еще раз!\nЧто делать если возникает такая ошибка? Ищите {text}", parse_mode="Markdown", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_peredacha_vib0)
    except AttributeError:
        send = bot.send_message(igrok1, f"Похоже ваш друг скрыл свой аккаунт и мы не можем распознать его Chat Id. {text_AttributeError}", reply_markup=markup1)
        bot.register_next_step_handler(send, kmn_peredacha_vib0)
    kmn3.write("bazakmn3.xml", encoding="UTF-8")

def kmn_mp_3_priglas_ig3_ig2_message(message):
    bot.delete_message(message.chat.id, message.message_id, timeout=0)
    markup1 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton(sposob_prig[0])
    but3 = types.KeyboardButton(sposob_prig[1])
    but5 = types.KeyboardButton(stop)
    markup1.add(but2, but3).add(but5)
    try:
        igrok1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib["id"]
        user1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
        igrok2 = kmn3.find(f"user{message.chat.id}").attrib['id']
        user2 = kmn3.find(f"user{message.chat.id}").find("nameig").text
        markup = types.ReplyKeyboardMarkup(True)
        but1 = types.KeyboardButton(slova[0])
        but2 = types.KeyboardButton(slova[1])
        markup.add(but1, but2)
        chat_global_file = open("chat.txt", "r")
        text2 = f"Попросите вашего друга зайти в бот и нажать кнопку /start, а потом повторите попытку, либо нажмите {stop} для прекращения приглашений друга!!\nОшибка повторяется? Ответ ищите [здесь](https://t.me/kontrol_chek185/1131)"
        allText = chat_global_file.read()
        spis_chat_id = list(map(str, allText.split()))
        markup2 = types.ReplyKeyboardRemove()
        if kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3") == None:
            igrok = ET.Element("igrok3")
            igrok.attrib['id'] = str(message.forward_from.id)
            igrok.text = None
            kmn3.find(f"user{message.chat.id}").find("igroki").append(igrok)
        elif kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3") != None:
            igrok = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3")
            igrok.attrib['id'] = str(message.forward_from.id)
            igrok.text = None
        if kmn3.find(f"user{igrok1}").find("igroki").find("igrok3") == None:
            igrok = ET.Element("igrok3")
            igrok.attrib['id'] = str(message.forward_from.id)
            igrok.text = None
            kmn3.find(f"user{igrok1}").find("igroki").append(igrok)
        elif kmn3.find(f"user{igrok1}").find("igroki").find("igrok3") != None:
            igrok = kmn3.find(f"user{igrok1}").find("igroki").find("igrok3")
            igrok.attrib['id'] = str(message.forward_from.id)
            igrok.text = None
        if kmn3.find(f"user{message.forward_from.id}") == None:
            igrok = ET.Element(f"user{message.forward_from.id}")
            igrok.attrib['id'] = str(message.forward_from.id)
            ig = ET.Element("nameig")
            ig.text = None
            igrok.append(ig)
            ig3 = ET.Element("igroki")
            ig1 = ET.Element("igrok2")
            ig1.attrib['id'] = igrok1
            ig1.text = user1
            ig3.append(ig1)
            ig2 = ET.Element("igrok3")
            ig2.attrib['id'] = igrok2
            ig2.text = user2
            ig3.append(ig2)
            igrok.append(ig3)
            kmn3r.append(igrok)
            igrok3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
        elif kmn3.find(f"user{message.forward_from.id}") != None:
            igrok = kmn3.find(f"user{message.forward_from.id}")
            if igrok.find("igroki") == None:
                ig = ET.Element("igroki")
                ig1 = ET.Element("igrok2")
                ig1.attrib['id'] = igrok1
                ig1.text = user1
                ig.append(ig1)
                ig2 = ET.Element("igrok3")
                ig2.attrib['id'] = igrok2
                ig2.text = user2
                ig.append(ig2)
                igrok.append(ig)
            elif igrok.find("igroki") != None:
                igroki = igrok.find("igroki")
                if igroki.find("igrok2") == None:
                    ig = ET.Element("igrok2")
                    ig.attrib['id'] = igrok1
                    ig.text = user1
                    igroki.append(ig)
                elif igroki.find("igrok2") != None:
                    ig = igroki.find("igrok2")
                    ig.attrib['id'] = igrok1
                    ig.text = user1
                if igroki.find("igrok3") == None:
                    ig = ET.Element("igrok3")
                    ig.attrib['id'] = igrok2
                    ig.text = user2
                    igroki.append(ig)
                elif igroki.find("igrok3") != None:
                    ig = igroki.find("igrok3")
                    ig.attrib['id'] = igrok2
                    ig.text = user2
            igrok3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
        if igrok3 in spis_chat_id:
            bot.send_message(igrok1, "Подождите еще! Отправили приглашение третьему другу!", reply_markup=markup2)
            bot.send_message(igrok2, "Приняли! Ожидайте ответа!", reply_markup=markup2)
            send = bot.send_message(igrok3, f"{user1} и {user2} отправили вам приглашение сыграть вместе в игру Камень-ножницы-бумага! Вы согласны?", reply_markup=markup)
            bot.register_next_step_handler(send, kmn_vib_ig1_3)
        elif not igrok3 in spis_chat_id:
            send = bot.send_message(igrok2, f"Пользователь не найден в базе данных бота! {text2}", parse_mode="Markdown", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_peredacha_vib1)
    except AttributeError:
        send = bot.send_message(igrok2, f"Похоже ваш друг скрыл свой аккаунт и мы не можем распознать его Chat Id. {text_AttributeError}", parse_mode="Markdown", reply_markup=markup1)
        bot.register_next_step_handler(send, kmn_peredacha_vib1)
    kmn3.write("bazakmn3.xml", encoding="UTF-8")

def kmn_vib_ig1_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton(kamen)
    but2 = types.KeyboardButton(noshik)
    but3 = types.KeyboardButton(bumaga)
    but4 = types.KeyboardButton(stop)
    markup.add(but1, but2, but3).add(but4)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = types.KeyboardButton("Отменить игру")
    but6 = types.KeyboardButton("Пригласить другого пользователя")
    but7 = types.KeyboardButton("Играть в двоем")
    markup1.add(but5, but6, but7)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but8 = types.KeyboardButton("/start")
    markup2.add(but8)
    markup3 = types.ReplyKeyboardRemove()
    igrok1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
    user1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
    igrok2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
    user2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").text
    igrok3 = kmn3.find(f"user{message.chat.id}").attrib['id']
    user3_1 = kmn3.find(f"user{igrok1}").find("igroki").find("igrok3")
    user3_2 = kmn3.find(f"user{igrok2}").find("igroki").find("igrok3")
    user3 = kmn3.find(f"user{message.chat.id}").find("nameig")
    if message.from_user.last_name == None:
        user3_1.text = str(message.from_user.first_name)
        user3_2.text = str(message.from_user.first_name)
        user3.text = str(message.from_user.first_name)
    elif message.from_user.last_name != None:
        user3_1.text = f"{message.from_user.first_name} {message.from_user.last_name}"
        user3_2.text = f"{message.from_user.first_name} {message.from_user.last_name}"
        user3.text = f"{message.from_user.first_name} {message.from_user.last_name}"
    user3 = kmn3.find(f"user{igrok3}").find("nameig").text
    if message.text.title() in vib:
        if message.text.title() == "Да!":
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"] = 0
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"] = 0
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"] = 0
            send4 = bot.send_message(igrok1, f"Текущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown")
            send5 = bot.send_message(igrok2, f"Текущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown")
            send3 = bot.send_message(igrok3, f"Текущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown")
            send = bot.send_message(igrok1, f"Ура! {user3} принял приглашение! Выберите Камень, ножницы или бумагу!", reply_markup=markup)
            send1 = bot.send_message(igrok2, f"Ура! {user3} принял приглашения! Подожди выбор {user1}", reply_markup=markup3)
            send2 = bot.send_message(igrok3, f"Вы приняли приглашение! Подожди выбор {user1}", reply_markup=markup3)
            bot.register_next_step_handler(send, kmn_vib_ig2_3)
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"] = send4.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"] = send5.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"] = send3.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"]= send1.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send2.id
        elif message.text.title() == "Нет!":
            send = bot.send_message(igrok1, f"{user3} отклонил приглашение! Выберите одно из действий ниже!", reply_markup=markup1)
            bot.send_message(igrok2, f"{user3} отклонил приглашение! Ждем решение первого игрока!", reply_markup=markup3)
            bot.send_message(igrok3, "Вы отклонили приглашение!", reply_markup=markup2)
            bot.register_next_step_handler(send, kmn_konflikt)
    elif not message.text.title() in vib:
        send = bot.send_message(igrok3, "Я вас не понял! Нажми кнопку ниже!")
        bot.register_next_step_handler(send, kmn_vib_ig1_3)

def kmn_vib_ig2_3(message):
    bot.delete_message(message.chat.id, message.id, timeout=0)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton(kamen)
    but2 = types.KeyboardButton(noshik)
    but3 = types.KeyboardButton(bumaga)
    but4 = types.KeyboardButton(stop)
    markup.add(but1, but2, but3).add(but4)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but8 = types.KeyboardButton("/start")
    markup2.add(but8)
    markup3 = types.ReplyKeyboardRemove()
    igrok1 = kmn3.find(f"user{message.chat.id}").attrib['id']
    user1 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    igrok2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
    user2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
    igrok3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
    user3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").text
    if message.text.title() in bot_knb:
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"], timeout=0)
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"], timeout=0)
        bot.delete_message(igrok3, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"], timeout=0)
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] = message.text.title()
        send1 = bot.send_message(igrok1, f"Окей, принял! Жду решения {user2}.", reply_markup=markup3)
        send = bot.send_message(igrok2, f"{user1} выбрал! Настал ваш выбор: выберите камень, ножницы или бумагу!", reply_markup=markup)
        send2 = bot.send_message(igrok3, f"{user1} сделал выбор! Ждем выбора второго игрока!", reply_markup=markup3)
        bot.register_next_step_handler(send, kmn_vib_ig3_3)
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send1.id
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send.id
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send2.id
    elif not message.text.title() in bot_knb and message.text == "/stop":
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"], timeout=0)
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"], timeout=0)
        bot.delete_message(igrok3, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"], timeout=0)
        bot.edit_message_text(chat_id=igrok1, text=f"Вы завершили игру!\nОбщий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
        bot.edit_message_text(chat_id=igrok2, text=f"{user1} завершил игру!\nОбщий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
        bot.edit_message_text(chat_id=igrok3, text=f"{user1} завершил игру!\nОбщий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
        bot.send_message(igrok1, "Нажмите кнопку ниже для выхода в меню бота", reply_markup=markup2)
        bot.send_message(igrok2, "Нажмите кнопку ниже для выхода в меню бота", reply_markup=markup2)
        bot.send_message(igrok3, "Нажмите кнопку ниже для выхода в меню бота", reply_markup=markup2)
    elif not message.text.title() in bot_knb and message.text != "/stop":
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"], timeout=0)
        send = bot.send_message(igrok1, "Ой, не совсем тебя поняли! Нажми любую кнопку ниже!", reply_markup=markup)
        bot.register_next_step_handler(send, kmn_vib_ig2_3)
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send.id

def kmn_vib_ig3_3(message):
    bot.delete_message(message.chat.id, message.id, timeout=0)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton(kamen)
    but2 = types.KeyboardButton(noshik)
    but3 = types.KeyboardButton(bumaga)
    but4 = types.KeyboardButton(stop)
    markup.add(but1, but2, but3).add(but4)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = types.KeyboardButton("/start")
    markup2.add(but5)
    markup3 = types.ReplyKeyboardRemove()
    igrok1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
    user1 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
    igrok2 = kmn3.find(f"user{message.chat.id}").attrib['id']
    user2 = kmn3.find(f'user{message.chat.id}').find("nameig").text
    igrok3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").attrib['id']
    user3 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok3").text
    if message.text.title() in bot_knb:
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"], timeout=0)
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"], timeout=0)
        bot.delete_message(igrok3, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"], timeout=0)
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] = message.text.title()
        send1 = bot.send_message(igrok1, f"{user2} сделал выбор! Ждем выбор {user3}!", reply_markup=markup3)
        send2 = bot.send_message(igrok2, f"Окей, принял! Жду решения {user3}.", reply_markup=markup3)
        send = bot.send_message(igrok3, f"{user2} выбрал! Настал ваш выбор: выберите камень, ножницы или бумагу!", reply_markup=markup)
        bot.register_next_step_handler(send, kmn_vib_itog_3)
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send1.id
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send2.id
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send.id
    elif not message.text.title() in bot_knb and message.text == "/stop":
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"], timeout=0)
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"], timeout=0)
        bot.delete_message(igrok3, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"], timeout=0)
        bot.edit_message_text(chat_id=igrok2, text=f"Вы завершили игру!\nОбщий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
        bot.edit_message_text(chat_id=igrok1, text=f"{user2} завершил игру!\nОбщий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
        bot.edit_message_text(chat_id=igrok3, text=f"{user2} завершил игру!\nОбщий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
        bot.send_message(igrok1, "Нажмите кнопку ниже для выхода в меню бота", reply_markup=markup2)
        bot.send_message(igrok2, "Нажмите кнопку ниже для выхода в меню бота", reply_markup=markup2)
        bot.send_message(igrok3, "Нажмите кнопку ниже для выхода в меню бота", reply_markup=markup2)
    elif not message.text.title() in bot_knb and message.text != "/stop":
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"], timeout=0)
        send = bot.send_message(igrok2, "Ой, не совсем тебя поняли! Нажми любую кнопку ниже!", reply_markup=markup)
        bot.register_next_step_handler(send, kmn_vib_ig3_3)
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send.id

def kmn_vib_itog_3(message):
    bot.delete_message(message.chat.id, message.id, timeout=0)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton(kamen)
    but2 = types.KeyboardButton(noshik)
    but3 = types.KeyboardButton(bumaga)
    but4 = types.KeyboardButton(stop)
    markup.add(but1, but2, but3).add(but4)
    markup1 = types.ReplyKeyboardRemove()
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = types.KeyboardButton("/start")
    markup2.add(but5)
    igrok1 = kmn3.find(f"user{message.chat.id}").find("igroki").find('igrok2').attrib['id']
    user1 = kmn3.find(f"user{message.chat.id}").find("igroki").find('igrok2').text
    igrok2 = kmn3.find(f"user{message.chat.id}").find("igroki").find('igrok3').attrib['id']
    user2 = kmn3.find(f"user{message.chat.id}").find("igroki").find('igrok3').text
    igrok3 = kmn3.find(f"user{message.chat.id}").attrib['id']
    user3 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    if message.text.title() in bot_knb:
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"], timeout=0)
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"], timeout=0)
        bot.delete_message(igrok3, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"], timeout=0)
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] = message.text.title()
        if shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]:
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"] += 1
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"] += 1
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"] += 1
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\nНичья!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\nНичья!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
            bot.edit_message_text(chat_id=igrok3, text="Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n\nНичья!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
            send = bot.send_message(igrok1, "Выберите Камень, ножницы или бумагу!", reply_markup=markup)
            send1 = bot.send_message(igrok2, "Подожди выбор первого пользователя!", reply_markup=markup1)
            send2 = bot.send_message(igrok3, "Подожди выбор первого пользователя!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_vib_ig2_3)
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send2.message_id
        elif (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]):
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"] += 1
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\nТы победил!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\n{user1} победил!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
            bot.edit_message_text(chat_id=igrok3, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n\n{user1} победил!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
            send = bot.send_message(igrok1, "Выберите Камень, ножницы или бумагу!", reply_markup=markup)
            send1 = bot.send_message(igrok2, "Подожди выбор первого пользователя!", reply_markup=markup1)
            send2 = bot.send_message(igrok3, "Подожди выбор первого пользователя!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_vib_ig2_3)
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send2.message_id
        elif (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]):
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"] += 1
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\nТы победил!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\n{user2} победил!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
            bot.edit_message_text(chat_id=igrok3, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n\n{user2} победил!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
            send = bot.send_message(igrok1, "Выберите Камень, ножницы или бумагу!", reply_markup=markup)
            send1 = bot.send_message(igrok2, "Подожди выбор первого пользователя!", reply_markup=markup1)
            send2 = bot.send_message(igrok3, "Подожди выбор первого пользователя!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_vib_ig2_3)
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send2.message_id
        elif (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]):
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"] += 1
            bot.edit_message_text(chat_id=igrok3, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n\nТы победил!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\n{user3} победил!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\n{user3} победил!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
            send = bot.send_message(igrok1, "Выберите Камень, ножницы или бумагу!", reply_markup=markup)
            send1 = bot.send_message(igrok2, "Подожди выбор первого пользователя!", reply_markup=markup1)
            send2 = bot.send_message(igrok3, "Подожди выбор первого пользователя!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_vib_ig2_3)
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send2.message_id
        elif (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]):
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"] += 1
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"] += 1
            bot.edit_message_text(chat_id=igrok3, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n\nТы и {user1} победили!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\nТы и {user3} победили!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\n{user1} и {user3} победили!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
            send = bot.send_message(igrok1, "Выберите Камень, ножницы или бумагу!", reply_markup=markup)
            send1 = bot.send_message(igrok2, "Подожди выбор первого пользователя!", reply_markup=markup1)
            send2 = bot.send_message(igrok3, "Подожди выбор первого пользователя!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_vib_ig2_3)
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send2.message_id
        elif (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]):
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"] += 1
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"] += 1
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\nТы и {user3} победили!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\n{user2} и {user3}  победили!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
            bot.edit_message_text(chat_id=igrok3, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n\nТы и {user2}победили!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
            send = bot.send_message(igrok1, "Выберите Камень, ножницы или бумагу!", reply_markup=markup)
            send1 = bot.send_message(igrok2, "Подожди выбор первого пользователя!", reply_markup=markup1)
            send2 = bot.send_message(igrok3, "Подожди выбор первого пользователя!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_vib_ig2_3)
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send2.message_id
        elif (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]):
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"] += 1
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"] += 1
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\nТы и {user1} победили!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\nТы и {user2} победили!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
            bot.edit_message_text(chat_id=igrok3, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n\n{user1} и {user2} победили!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
            send = bot.send_message(igrok1, "Выберите Камень, ножницы или бумагу!", reply_markup=markup)
            send1 = bot.send_message(igrok2, "Подожди выбор первого пользователя!", reply_markup=markup1)
            send2 = bot.send_message(igrok3, "Подожди выбор первого пользователя!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_vib_ig2_3)
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send2.message_id
        elif (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == noshik) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == bumaga) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == bumaga) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == kamen) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == kamen and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == noshik) or (shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"] == bumaga and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"] == noshik and shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"] == kamen):
            bot.edit_message_text(chat_id=igrok1, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\nРазный выбор!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
            bot.edit_message_text(chat_id=igrok2, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user3} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n\nРазный выбор!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
            bot.edit_message_text(chat_id=igrok3, text=f"Ты выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok3}"]) + f"*\n{user1} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok1}"]) + f"*\n{user2} выбрал: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_zn{igrok2}"]) + f"*\n\nРазный выбор!\nТекущий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
            send = bot.send_message(igrok1, "Выберите Камень, ножницы или бумагу!", reply_markup=markup)
            send1 = bot.send_message(igrok2, "Подожди выбор первого пользователя!", reply_markup=markup1)
            send2 = bot.send_message(igrok3, "Подожди выбор первого пользователя!", reply_markup=markup1)
            bot.register_next_step_handler(send, kmn_vib_ig2_3)
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"] = send.id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"] = send1.message_id
            shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send2.message_id
    elif not message.text.title() in bot_knb and message.text == "/stop":
        bot.delete_message(igrok1, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok1}"], timeout=0)
        bot.delete_message(igrok2, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok2}"], timeout=0)
        bot.delete_message(igrok3, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"], timeout=0)
        bot.edit_message_text(chat_id=igrok3, text=f"Вы завершили игру!\nОбщий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok3}"])
        bot.edit_message_text(chat_id=igrok1, text=f"{user3} завершил игру!\nОбщий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok1}"])
        bot.edit_message_text(chat_id=igrok2, text=f"{user3} завершил игру!\nОбщий счёт:\n{user1}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok1}"]) + f"*\n{user2}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok2}"]) + f"*\n{user3}: *" + str(shet[f"{igrok1}vs{igrok2}vs{igrok3}_hod{igrok3}"]) + "*", parse_mode="Markdown", message_id=shet[f"{igrok1}vs{igrok2}vs{igrok3}_mes{igrok2}"])
        bot.send_message(igrok1, "Нажмите кнопку ниже для выхода в меню бота", reply_markup=markup2)
        bot.send_message(igrok2, "Нажмите кнопку ниже для выхода в меню бота", reply_markup=markup2)
        bot.send_message(igrok3, "Нажмите кнопку ниже для выхода в меню бота", reply_markup=markup2)
    elif not message.text.title() in bot_knb and message.text != "/stop":
        bot.delete_message(igrok3, shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"], timeout=0)
        send = bot.send_message(igrok3, "Ой, не совсем тебя поняли! Нажми любую кнопку ниже!", reply_markup=markup)
        bot.register_next_step_handler(send, kmn_vib_itog_3)
        shet[f"{igrok1}vs{igrok2}vs{igrok3}_mesdel{igrok3}"] = send.id
def kmn_konflikt(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/start")
    markup.add(but)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = types.KeyboardButton("Передать возможность второму игроку")
    markup1.add(but5)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton(kamen)
    but2 = types.KeyboardButton(noshik)
    but3 = types.KeyboardButton(bumaga)
    but4 = types.KeyboardButton(stop)
    markup2.add(but1, but2, but3).add(but4)
    markup3 = types.ReplyKeyboardMarkup(True)
    but2 = types.KeyboardButton("Я")
    but3 = types.KeyboardButton("Игрок 2")
    markup3.add(but2, but3)
    igrok1 = kmn3.find(f"user{message.chat.id}").attrib['id']
    user1 = kmn3.find(f"user{message.chat.id}").find("nameig").text
    igrok2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
    user2 = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
    if message.text in vib1:
        if message.text == "Отменить игру":
            bot.send_message(igrok1, "Я вас понял! Спасибо за использование игры!", reply_markup=markup)
            bot.send_message(igrok2, f"{user1} принял решение завершить игру! Спасибо за использование игры!", reply_markup=markup)
        elif message.text == "Пригласить другого пользователя":
            send = bot.send_message(igrok1, f"Выберите кто будет приглашать другого пользователя!", reply_markup=markup3)
            bot.send_message(igrok2, f"{user1} принял решение пригласить другого игрока! Подождите его решения!")
            bot.register_next_step_handler(send, kmn_peredacha_vib)
        elif message.text == "Играть в двоем":
            if kmn2.find(f"user{message.chat.id}") == None:
                igrok = ET.Element(f"user{message.chat.id}")
                igrok.attrib['id'] = kmn3.find(f"user{message.chat.id}").attrib['id']
                r = ET.Element("nameig")
                r.text = kmn3.find(f"user{message.chat.id}").find("nameig").text
                igrok.append(r)
                ig = ET.Element("igrok2")
                ig.attrib['id'] = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
                ig.text = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
                igrok.append(ig)
                kmn2r.append(igrok)
            elif kmn2.find(f"user{message.chat.id}") != None:
                igrok = kmn2.find(f"user{message.chat.id}")
                name = igrok.find("nameig")
                name.text = kmn3.find(f"user{message.chat.id}").find("nameig").text
                if igrok.find("igrok2") == None:
                    ig = ET.Element("igrok2")
                    ig.attrib['id'] = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
                    ig.text = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
                    igrok.append(ig)
                elif igrok.find("igrok2") != None:
                    ig = igrok.find("igrok2")
                    ig.attrib['id'] = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").attrib['id']
                    ig.text = kmn3.find(f"user{message.chat.id}").find("igroki").find("igrok2").text
            if kmn2.find(f"user{igrok2}") == None:
                igrok = ET.Element(f"user{igrok2}")
                igrok.attrib['id'] = kmn3.find(f"user{igrok2}").attrib['id']
                r = ET.Element("nameig")
                r.text = kmn3.find(f"user{igrok2}").find("nameig").text
                igrok.append(r)
                ig = ET.Element("igrok2")
                ig.attrib['id'] = kmn3.find(f"user{igrok2}").find("igroki").find("igrok2").attrib['id']
                ig.text = kmn3.find(f"user{igrok2}").find("igroki").find("igrok2").text
                igrok.append(ig)
                kmn2r.append(igrok)
            elif kmn2.find(f"user{igrok2}") != None:
                igrok = kmn2.find(f"user{igrok2}")
                name = igrok.find("nameig")
                name.text = kmn3.find(f"user{igrok2}").find("nameig").text
                if igrok.find("igrok2") == None:
                    ig = ET.Element("igrok2")
                    ig.attrib['id'] = kmn3.find(f"user{igrok2}").find("igroki").find("igrok2").attrib['id']
                    ig.text = kmn3.find(f"user{igrok2}").find("igroki").find("igrok2").text
                    igrok.append(ig)
                elif igrok.find("igrok2") != None:
                    ig = igrok.find("igrok2")
                    ig.attrib['id'] = kmn3.find(f"user{igrok2}").find("igroki").find("igrok2").attrib['id']
                    ig.text = kmn3.find(f"user{igrok2}").find("igroki").find("igrok2").text
            shet[f"{igrok1}vs{igrok2}_hod{igrok1}"] = int(0)
            shet[f"{igrok1}vs{igrok2}_hod{igrok2}"] = int(0)
            send1 = bot.send_message(igrok1, "Текущий счёт:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + ":" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + f"* {user2}", parse_mode="Markdown")
            send2 = bot.send_message(igrok2, "Текущий счёт:\nВы *" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok2}"]) + ":" + str(shet[f"{igrok1}vs{igrok2}_hod{igrok1}"]) + f"* {user1}", parse_mode="Markdown")
            send = bot.send_message(igrok1, "Окей! Выберите Камень, ножницы или бумагу!", reply_markup=markup2)
            send3 = bot.send_message(igrok2, f"{user1} принял решение сыграть только с вами! Подождите его выбор!")
            bot.register_next_step_handler(send, kmn_mp_vib_ig2)
            shet[f"{igrok1}vs{igrok2}_msdel{igrok1}"] = send.id
            shet[f"{igrok1}vs{igrok2}_msdel{igrok2}"] = send3.id
            shet[f"{igrok1}vs{igrok2}_ms{igrok1}"] = send1.id
            shet[f"{igrok1}vs{igrok2}_ms{igrok2}"] = send2.id
    elif not message.text in vib1:
        send = bot.send_message(igrok1, "Ой, не совсем тебя поняли! Нажми любую кнопку ниже!")
        bot.register_next_step_handler(send, kmn_konflikt)
    kmn2.write("bazakmn2.xml", "UTF-8")

@bot.message_handler(commands=["beta_randomaizer"])
def randomaizer_vib(message):
    black_list = open("black_list.txt", "r", encoding="UTF-8")
    black_l = black_list.read()
    if not str(message.chat.id) in black_l:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton(kmn_reshim[0])
        but2 = types.KeyboardButton(kmn_reshim[1])
        markup.add(but1, but2)
        send = bot.send_message(message.chat.id, "Привет, ты в Рандомайзере! Выбери режим работы!", reply_markup=markup)
        bot.register_next_step_handler(send, randomaizer)
    elif str(message.chat.id) in black_l:
        bot.send_message(message.chat.id, black_list_text)

def randomaizer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/stop")
    markup.add(but)
    markup1 = types.ReplyKeyboardMarkup(True)
    but1 = types.KeyboardButton(sposob_prig[0])
    but2 = types.KeyboardButton(sposob_prig[1])
    markup1.add(but1, but2)
    if message.text in kmn_reshim:
        if message.text == "Одиночный":
            random_dict[f"{message.chat.id}randomaizer_na_1"] = []
            send = bot.send_message(message.chat.id, "Введите предметы, а когда вы все напишите нажмите кнопку ниже!", reply_markup=markup)
            bot.register_next_step_handler(send, randomaizer1)
        elif message.text == "Сетевой":
            if baza_random.find(f'user{message.chat.id}') == None:
                r = ET.Element(f"user{message.chat.id}")
                r.attrib['id'] = str(message.chat.id)
                name = ET.Element("namepolsov")
                if message.from_user.last_name == None:
                    name.text = str(message.from_user.first_name)
                elif message.from_user.last_name != None:
                    name.text = f"{message.from_user.first_name} {message.from_user.last_name}"
                r.append(name)
                baza_random_r.append(r)
                polsovatel1 = baza_random.find(f"user{message.chat.id}").attrib['id']
            elif baza_random.find(f"user{message.chat.id}") != None:
                r = baza_random.find(f"user{message.chat.id}")
                name = r.find("namepolsov")
                if message.from_user.last_name == None:
                    name.text = str(message.from_user.first_name)
                elif message.from_user.last_name != None:
                    name.text = f"{message.from_user.first_name} {message.from_user.last_name}"
                polsovatel1 = baza_random.find(f"user{message.chat.id}").attrib['id']
            p = open("Важное фото.png", "rb")
            send = bot.send_message(polsovatel1, "Выберите способ приглашения друга!", reply_markup=markup1, parse_mode="Markdown")
            bot.register_next_step_handler(send, randomaizer_mp_vib)
    baza_random.write("bazarandomaizer.xml", encoding="UTF-8")

def randomaizer1(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да!")
    but2 = types.KeyboardButton("Нет!")
    markup1.add(but1, but2)
    if message.content_type == "text" and message.text != "/stop":
        random_dict[f"{message.chat.id}randomaizer_na_1"].append(str(message.text))
        send = bot.send_message(message.chat.id, "Отлично! Можно ввести еще!")
        bot.register_next_step_handler(send, randomaizer1)
    elif message.text == "/stop":
        if len(random_dict[f"{message.chat.id}randomaizer_na_1"]) > 1:
            random_dict[f"{message.chat.id}randomaizer_na_1_bs"] = ", ".join(random_dict[f"{message.chat.id}randomaizer_na_1"])
            send = bot.send_message(message.chat.id, f"Окей! Проверь все ли верно:\n*" + str(random_dict[f"{message.chat.id}randomaizer_na_1_bs"]) + "*", reply_markup=markup1, parse_mode="Markdown")
            bot.register_next_step_handler(send, randomaizer_vp)
        elif len(random_dict[f"{message.chat.id}randomaizer_na_1"]) <= 1:
            send = bot.send_message(message.chat.id, "Извините, но в вашем списке очень мало объектов, из-за этого работа рандомайзера невозможна! Пожалуйста, добавьте еще элементов в список!")
            bot.register_next_step_handler(send, randomaizer1)

def randomaizer_vp(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("Крутить")
    markup.add(but)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("/stop")
    markup1.add(but1)
    if message.text in slova:
        if message.text == "Да!":
            send = bot.send_message(message.chat.id, "Хорошо! Тогда нажми кнопку ниже!", reply_markup=markup)
            bot.register_next_step_handler(send, randomaizer2)
        elif message.text == "Нет!":
            random_dict[f"{message.chat.id}randomaizer_na_1"].clear()
            send = bot.send_message(message.chat.id, "Введи другие значения!", reply_markup=markup1)
            bot.register_next_step_handler(send, randomaizer1)
    elif not message.text in slova:
        send = bot.send_message(message.chat.id, "Ой!")
        bot.register_next_step_handler(send, randomaizer_vp)

def randomaizer2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Крутить")
    but2 = types.KeyboardButton("Удалить")
    but3 = types.KeyboardButton("Завершить")
    markup.add(but1, but2).add(but3)
    if message.text == "Крутить":
        shifron = []
        while True:
            kluchi = choice(kluchi_shifron)
            shifron.append(kluchi)
            if len(shifron) == len(random_dict[f"{message.chat.id}randomaizer_na_1"]):
                kluchi_bez_skobok = ", ".join(shifron)
                print(f"Получен новый список от {message.chat.id}: {kluchi_bez_skobok}")
                break
        random_dict[f"{message.chat.id}randomaizer_itog"] = choice(random_dict[f"{message.chat.id}randomaizer_na_1"])
        send = bot.send_message(message.chat.id, f"Итог: *" + str(random_dict[f"{message.chat.id}randomaizer_itog"]) + "*\n\nВыберите действие с этим списком ниже!", parse_mode="Markdown", reply_markup=markup)
        bot.register_next_step_handler(send, randomaizer3)
        shifron.clear()
    elif message.text != "Крутить":
        send = bot.send_message(message.chat.id, "Ой")
        bot.register_next_step_handler(send, randomaizer2)

def randomaizer3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Крутить")
    but2 = types.KeyboardButton("Удалить")
    but3 = types.KeyboardButton("Завершить")
    markup.add(but1, but2).add(but3)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup1.add(but1, but3)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/start")
    markup2.add(but)
    if message.text in slo1:
        if message.text == "Удалить":
            random_dict[f"{message.chat.id}randomaizer_na_1"].remove(random_dict[f"{message.chat.id}randomaizer_itog"])
            if len(random_dict[f"{message.chat.id}randomaizer_na_1"]) != 0:
                send = bot.send_message(message.chat.id, "Элемент удален! Нажмите кнопку ниже!", reply_markup=markup1)
                bot.register_next_step_handler(send, randomaizer3)
            elif len(random_dict[f"{message.chat.id}randomaizer_na_1"]) == 0:
                bot.send_message(message.chat.id, "Элемент удален! На этом список закончился! Спасибо за использование!", reply_markup=markup2)
        elif message.text == "Крутить":
            random_dict[f"{message.chat.id}randomaizer_itog"] = choice(random_dict[f"{message.chat.id}randomaizer_na_1"])
            send = bot.send_message(message.chat.id, f"Итог: *" + str(random_dict[f"{message.chat.id}randomaizer_itog"]) + "*\n\nВыберите действие с этим списком ниже!", parse_mode="Markdown", reply_markup=markup)
            bot.register_next_step_handler(send, randomaizer3)
        elif message.text == "Завершить":
            random_dict[f"{message.chat.id}randomaizer_na_1"].clear()
            bot.send_message(message.chat.id, "Окей, завершаем использование! Спасибо за использование!", reply_markup=markup2)
    elif not message.text in slo1:
        send = bot.send_message(message.chat.id, "Ой")
        bot.register_next_step_handler(send, randomaizer3)

def randomaizer_mp_vib(message):
    markup = types.ReplyKeyboardMarkup(True)
    but = types.KeyboardButton("/stop")
    markup.add(but)
    markup1 = types.ReplyKeyboardRemove()
    polsovatel1 = baza_random.find(f"user{message.chat.id}").attrib['id']
    if message.text in sposob_prig:
        if message.text == sposob_prig[0]:
            send = bot.send_message(polsovatel1, "Отправьте мне сообщение от вашего друга!", reply_markup=markup1)
            bot.register_next_step_handler(send, randomaizer_mp_message)
        elif message.text == sposob_prig[1]:
            p = open("Важное фото.png", "rb")
            send = bot.send_photo(chat_id=polsovatel1, photo=p, caption=f"Введите Chat Id вашего друга!\n{text_photo}", reply_markup=markup, parse_mode="Markdown")
            bot.register_next_step_handler(send, randomaizer_mp)
    elif not message.text in sposob_prig:
        send = bot.send_message(polsovatel1, "Ой, не совсем тебя понял! Нажми кнопку ниже!")
        bot.register_next_step_handler(send, randomaizer_mp_vib)

def randomaizer_mp_message(message):
    bot.delete_message(message.chat.id, message.message_id, timeout=0)
    text2 = f"Попросите вашего друга зайти в бот и нажать кнопку /start, а потом выберите заново способ приглашения друга ниже, либо нажмите {stop} для прекращения приглашений друга!!\nОшибка повторяется? Ответ ищите [здесь](https://t.me/kontrol_chek185/1131)"
    text = "[здесь](https://t.me/kontrol_chek185/1131)"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да!")
    but2 = types.KeyboardButton("Нет!")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardRemove()
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/stop")
    markup2.add(but)
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but3 = types.KeyboardButton("/start")
    markup3.add(but3)
    markup4 = types.ReplyKeyboardMarkup(True)
    but4 = types.KeyboardButton(sposob_prig[0])
    but5 = types.KeyboardButton(sposob_prig[1])
    markup4.add(but4, but5)
    chat_global_file = open("chat.txt", "r")
    allText = chat_global_file.read()
    spis_chat_id = list(map(str, allText.split()))
    try:
        polsovatel1 = baza_random.find(f"user{message.chat.id}").attrib['id']
        user1 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
        if baza_random.find(f"user{message.chat.id}").find("polsovatel2") == None:
            polsov2 = ET.Element("polsovatel2")
            polsov2.attrib['id'] = str(message.forward_from.id)
            polsov2.text = None
            baza_random.find(f"user{message.chat.id}").append(polsov2)
            polsovatel2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
        elif baza_random.find(f"user{message.chat.id}").find("polsovatel2") != None:
            polsov2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2")
            polsov2.attrib['id'] = str(message.forward_from.id)
            polsov2.text = None
            polsovatel2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
        if baza_random.find(f"user{message.forward_from.id}") == None:
            polsov = ET.Element(f"user{message.forward_from.id}")
            polsov.attrib['id'] = str(message.forward_from.id)
            name = ET.Element("namepolsov")
            name.text = None
            polsov.append(name)
            polsov2 = ET.Element("polsovatel2")
            polsov2.attrib['id'] = str(message.chat.id)
            polsov2.text = user1
            polsov.append(polsov2)
            baza_random_r.append(polsov)
        elif baza_random.find(f"user{message.forward_from.id}") != None:
            polsov = baza_random.find(f"user{message.forward_from.id}")
            name = polsov.find("namepolsov")
            name.text = None
            if polsov.find("polsovatel2") == None:
                polsov2 = ET.Element("polsovatel2")
                polsov2.attrib['id'] = str(message.chat.id)
                polsov2.text = user1
                polsov.append(polsov2)
            elif polsov.find("polsovatel2") != None:
                polsov2 = polsov.find("polsovatel2")
                polsov2.attrib['id'] = str(message.chat.id)
                polsov2.text = user1
        if polsovatel1 != polsovatel2:
            if polsovatel2 in spis_chat_id:
                bot.send_message(polsovatel1, "Отправили твое приглашение! Ожидай ответа!", reply_markup=markup1)
                send = bot.send_message(polsovatel2, f"Вам пришло приглашение от пользователя {user1}! Вы принимаете его приглашение?", reply_markup=markup)
                bot.register_next_step_handler(send, randomaizer_mp_vibor_elem)
            elif not polsovatel2 in spis_chat_id:
                send = bot.send_message(polsovatel1, f"Пользователь не найден в базе данных бота! {text2}", parse_mode="Markdown", reply_markup=markup4)
                bot.register_next_step_handler(send, randomaizer_mp_vib)
        elif polsovatel1 == polsovatel2:
            send = bot.send_message(polsovatel1, f"Извините самого себя пригласить нельзя! Выберите заново способ приглашения друга ниже и попробуйте еще раз!\nЧто делать если возникает такая ошибка? Ищите {text}", parse_mode="Markdown", reply_markup=markup4)
            bot.register_next_step_handler(send, randomaizer_mp_vib)
    except:
        markup1 = types.ReplyKeyboardMarkup(True)
        but1 = types.KeyboardButton(sposob_prig[0])
        but2 = types.KeyboardButton(sposob_prig[1])
        but3 = types.KeyboardButton(stop)
        markup1.add(but1, but2).add(but3)
        send = bot.send_message(message.chat.id, f"Похоже ваш друг скрыл свой аккаунт и мы не можем распознать его Chat Id. {text_AttributeError}", reply_markup=markup4)
        bot.register_next_step_handler(send, randomaizer_mp_vib)
    baza_random.write("bazarandomaizer.xml", encoding="UTF-8")

def randomaizer_mp(message):
    text2 = f"Попросите вашего друга зайти в бот и нажать кнопку /start, а потом выберите заново способ приглашения друга ниже, либо нажмите {stop} для прекращения приглашений друга!!\nОшибка повторяется? Ответ ищите [здесь](https://t.me/kontrol_chek185/1131)"
    text = "[здесь](https://t.me/kontrol_chek185/1131)"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да!")
    but2 = types.KeyboardButton("Нет!")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardRemove()
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/stop")
    markup2.add(but)
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but3 = types.KeyboardButton("/start")
    markup3.add(but3)
    markup4 = types.ReplyKeyboardMarkup(True)
    but4 = types.KeyboardButton(sposob_prig[0])
    but5 = types.KeyboardButton(sposob_prig[1])
    markup4.add(but4, but5)
    chat_global_file = open("chat.txt", "r")
    allText = chat_global_file.read()
    spis_chat_id = list(map(str, allText.split()))
    if message.text.isdigit():
        polsovatel1 = baza_random.find(f"user{message.chat.id}").attrib['id']
        user1 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
        if baza_random.find(f"user{message.chat.id}").find("polsovatel2") == None:
            polsov2 = ET.Element("polsovatel2")
            polsov2.attrib['id'] = str(message.text)
            polsov2.text = None
            baza_random.find(f"user{message.chat.id}").append(polsov2)
            polsovatel2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
        elif baza_random.find(f"user{message.chat.id}").find("polsovatel2") != None:
            polsov2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2")
            polsov2.attrib['id'] = str(message.text)
            polsov2.text = None
            polsovatel2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
        if baza_random.find(f"user{message.text}") == None:
            polsov = ET.Element(f"user{message.text}")
            polsov.attrib['id'] = str(message.text)
            name = ET.Element("namepolsov")
            name.text = None
            polsov.append(name)
            polsov2 = ET.Element("polsovatel2")
            polsov2.attrib['id'] = str(message.chat.id)
            polsov2.text = user1
            polsov.append(polsov2)
            baza_random_r.append(polsov)
        elif baza_random.find(f"user{message.text}") != None:
            polsov = baza_random.find(f"user{message.text}")
            name = polsov.find("namepolsov")
            name.text = None
            if polsov.find("polsovatel2") == None:
                polsov2 = ET.Element("polsovatel2")
                polsov2.attrib['id'] = str(message.chat.id)
                polsov2.text = user1
                polsov.append(polsov2)
            elif polsov.find("polsovatel2") != None:
                polsov2 = polsov.find("polsovatel2")
                polsov2.attrib['id'] = str(message.chat.id)
                polsov2.text = user1
        if polsovatel1 != polsovatel2:
            if polsovatel2 in spis_chat_id:
                bot.send_message(polsovatel1, "Отправили твое приглашение! Ожидай ответа!", reply_markup=markup1)
                send = bot.send_message(polsovatel2, f"Вам пришло приглашение от пользователя {user1}! Вы принимаете его приглашение?", reply_markup=markup)
                bot.register_next_step_handler(send, randomaizer_mp_vibor_elem)
            elif not polsovatel2 in spis_chat_id:
                send = bot.send_message(polsovatel1, f"Пользователь не найден в базе данных бота! {text2}", parse_mode="Markdown", reply_markup=markup4)
                bot.register_next_step_handler(send, randomaizer_mp_vib)
        elif polsovatel1 == polsovatel2:
            send = bot.send_message(polsovatel1, f"Извините самого себя пригласить нельзя! Выберите заново способ приглашения друга ниже и попробуйте еще раз!\nЧто делать если возникает такая ошибка? Ищите {text}", parse_mode="Markdown", reply_markup=markup4)
            bot.register_next_step_handler(send, randomaizer_mp_vib)
    elif not message.text.isdigit() and message.text != "/stop":
        send = bot.send_message(polsovatel1, "Вводите только цифры!", reply_markup=markup2)
        bot.register_next_step_handler(send, randomaizer_mp)
    elif not message.text.isdigit() and message.text == "/stop":
        bot.send_message(polsovatel1, "Принял! Нажми на одну из кнопок ниже!", reply_markup=markup3)
    chat_global_file.close()
    baza_random.write("bazarandomaizer.xml", encoding="UTF-8")

def randomaizer_mp_vibor_elem(message):
    polsovatel1 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
    user1 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").text
    polsovatel2 = baza_random.find(f"user{message.chat.id}").attrib['id']
    user2 = baza_random.find(f"user{message.chat.id}").find("namepolsov")
    user = baza_random.find(f"user{polsovatel1}").find("polsovatel2")
    if message.from_user.last_name == None:
        user2.text = str(message.from_user.first_name)
        user.text = str(message.from_user.first_name)
    elif message.from_user.last_name != None:
        user2.text = f"{message.from_user.first_name} {message.from_user.last_name}"
        user.text = f"{message.from_user.first_name} {message.from_user.last_name}"
    user2 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
    markup = types.ReplyKeyboardRemove()
    if message.text.title() in slova:
        if message.text.title() == "Да!":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"] = []
            send = bot.send_message(polsovatel1, f"{user2} принял приглашение! Начните вводить нужные вам или вашему другу значения!")
            bot.send_message(polsovatel2, f"Вы приняли приглашение! Подожди пока {user1} выберет нужные значения!", reply_markup=markup)
            bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_1)
        elif message.text.title() == "Нет!":
            bot.send_message(polsovatel1, f"{user2} отклонил приглашение!")
            bot.send_message(polsovatel2, "Вы отклонили приглашение!")
    elif not message.text.title() in slova:
        send = bot.send_message(polsovatel2, "Ой")
        bot.register_next_step_handler(send, randomaizer_mp_vibor_elem)
    baza_random.write("bazarandomaizer.xml", encoding="UTF-8")

def randomaizer_mp_vibor_elem_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да!")
    but2 = types.KeyboardButton("Нет!")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but3 = types.KeyboardButton("/stop")
    but4 = types.KeyboardButton("Передать возможность добавить второму игроку нужное значение")
    markup1.add(but4).add(but3)
    markup2 = types.ReplyKeyboardRemove()
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = types.KeyboardButton("/stop")
    but6 = types.KeyboardButton("Передать возможность добавить первому игроку нужное значение")
    markup3.add(but6).add(but5)
    polsovatel1 = baza_random.find(f"user{message.chat.id}").attrib['id']
    user1 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
    polsovatel2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
    user2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").text
    if message.content_type == "text" and not message.text in slova2:
        random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"].append(str(message.text))
        send = bot.send_message(polsovatel1, "Добавил! Добавь еще!", reply_markup=markup1)
        bot.send_message(polsovatel2, "Один элемент добавлен! Добавляются еще!", reply_markup=markup2)
        bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_1)
    elif message.text in slova2:
        if message.text == "Передать возможность добавить второму игроку нужное значение":
            bot.send_message(polsovatel1, f"Окей! Отправил {user2} такую возможность!", reply_markup=markup2)
            send = bot.send_message(polsovatel2, f"{user1} предоставил вам возможность добавить элементы в список! Введите в строку ниже нужные элементы!", reply_markup=markup3)
            bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_2)
        elif message.text == slova2[2]:
            if len(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"]) > 1:
                random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_bs"] = ", ".join(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"])
                send = bot.send_message(polsovatel1, f"Ваш с {user2} список выглядит вот так:\n*" + str(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_bs"]) + "*\n\nВы согласны использовать такой список?", reply_markup=markup, parse_mode="Markdown")
                bot.register_next_step_handler(send, randomaizer_mp_vibor1)
            elif len(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"]) <= 1:
                send = bot.send_message(polsovatel1, f"Извините, но в вашем с {user2} списке очень мало элементов, из-за этого работа рандомайзера невозможна! Пожалуйста, добавьте еще элементов в список!", reply_markup=markup1, parse_mode="Markdown")
                bot.send_message(polsovatel2, f"Извините, но в вашем с {user1} оказалось очень мало элементов, из-за этого работа рандомайзера невозможна! {user1} уже добавляет элементы в ваш список!")
                bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_1)

def randomaizer_mp_vibor_elem_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да!")
    but2 = types.KeyboardButton("Нет!")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but3 = types.KeyboardButton("/stop")
    but4 = types.KeyboardButton("Передать возможность добавить первому игроку нужное значение")
    markup1.add(but4).add(but3)
    markup2 = types.ReplyKeyboardRemove()
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = types.KeyboardButton("/stop")
    but6 = types.KeyboardButton("Передать возможность добавить второму игроку нужное значение")
    markup3.add(but6).add(but5)
    polsovatel2 = baza_random.find(f"user{message.chat.id}").attrib['id']
    user2 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
    polsovatel1 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
    user1 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").text
    if message.content_type == "text" and not message.text in slova2:
        random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"].append(str(message.text))
        send = bot.send_message(polsovatel2, "Добавил! Добавь еще!", reply_markup=markup1)
        bot.send_message(polsovatel1, "Один элемент добавлен! Добавляются еще!", reply_markup=markup2)
        bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_2)
    elif message.text in slova2:
        if message.text == "Передать возможность добавить первому игроку нужное значение":
            bot.send_message(polsovatel2, f"Окей! Отправил {user1} такую возможность!", reply_markup=markup2)
            send = bot.send_message(polsovatel1, f"{user2} предоставил вам возможность добавить элементы в список! Введите в строку ниже нужные элементы!", reply_markup=markup3)
            bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_1)
        elif message.text == slova2[2]:
            if len(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"]) > 1:
                random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_bs"] = ", ".join(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"])
                send = bot.send_message(polsovatel2, f"Ваш с {user1} список выглядит вот так:\n*" + str(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_bs"]) + "*\n\nВы согласны использовать такой список?", reply_markup=markup, parse_mode="Markdown")
                bot.register_next_step_handler(send, randomaizer_mp_vibor1_2)
            elif len(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"]) <= 1:
                send = bot.send_message(polsovatel2, f"Извините, но в вашем с {user1} списке очень мало элементов, из-за этого работа рандомайзера невозможна! Пожалуйста, добавьте еще элементов в список!", reply_markup=markup1, parse_mode="Markdown")
                bot.send_message(polsovatel1, f"Извините, но в вашем с {user2} оказалось очень мало элементов, из-за этого работа рандомайзера невозможна! {user1} уже добавляет элементы в ваш список!")
                bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_2)

def randomaizer_mp_vibor1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да!")
    but2 = types.KeyboardButton("Нет!")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/stop")
    markup1.add(but)
    markup2 = types.ReplyKeyboardRemove()
    polsovatel1 = baza_random.find(f"user{message.chat.id}").attrib['id']
    user1 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
    polsovatel2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
    user2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").text
    if message.text.title() in slova:
        if message.text.title() == "Да!":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_bs"] = ", ".join(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"])
            bot.send_message(polsovatel1, f"Окей! Отправил вопрос {user2}. Ожидайте ответа!", reply_markup=markup2)
            send = bot.send_message(polsovatel2, f"Ваш с {user1} список выглядит вот так:\n*" + str(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_bs"]) + "*\n\nВы согласны использовать такой список?", reply_markup=markup, parse_mode='Markdown')
            bot.register_next_step_handler(send, randomaizer_mp_vibor2)
        if message.text.title() == "Нет!":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"].clear()
            send = bot.send_message(polsovatel1, "Введите другие значения в список!", reply_markup=markup1)
            bot.send_message(polsovatel2, f"{user1} сбросил список и сейчас заполняет его заного! Подождите немного!", reply_markup=markup2)
            bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_1)
    elif not message.text.title() in slova:
        send = bot.send_message(message.chat.id, "Ой!")
        bot.register_next_step_handler(send, randomaizer_mp_vibor1)

def randomaizer_mp_vibor1_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да!")
    but2 = types.KeyboardButton("Нет!")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/stop")
    markup1.add(but)
    markup2 = types.ReplyKeyboardRemove()
    polsovatel2 = baza_random.find(f"user{message.chat.id}").attrib['id']
    user2 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
    polsovatel1 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
    user1 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").text
    if message.text.title() in slova:
        if message.text.title() == "Да!":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_bs"] = ", ".join(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"])
            bot.send_message(polsovatel2, f"Окей! Отправил вопрос {user1}. Ожидайте ответа!", reply_markup=markup2)
            send = bot.send_message(polsovatel1, f"Ваш с {user2} список выглядит вот так:\n*" + str(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_bs"]) + "*\n\nВы согласны использовать такой список?", reply_markup=markup, parse_mode="Markdown")
            bot.register_next_step_handler(send, randomaizer_mp_vibor2_2)
        if message.text.title() == "Нет!":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"].clear()
            send = bot.send_message(polsovatel2, "Введите другие значения в список!", reply_markup=markup1)
            bot.send_message(polsovatel1, f"{user2} сбросил список и сейчас заполняет его заного! Подождите немного!")
            bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_2)
    elif not message.text.title() in slova:
        send = bot.send_message(message.chat.id, "Ой!")
        bot.register_next_step_handler(send, randomaizer_mp_vibor1_2)

def randomaizer_mp_vibor2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Крутить")
    but2 = types.KeyboardButton("Завершить")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardRemove()
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/stop")
    markup2.add(but)
    polsovatel2 = baza_random.find(f"user{message.chat.id}").attrib['id']
    user2 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
    polsovatel1 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
    user1 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").text
    if message.text.title() in slova:
        if message.text.title() == "Да!":
            shifron_mp = []
            while True:
                kluchi = choice(kluchi_shifron)
                shifron_mp.append(kluchi)
                if len(shifron_mp) == len(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"]):
                    kluchi_bez_skobok = ", ".join(shifron_mp)
                    print(f"Получен новый список от {polsovatel1} и {polsovatel2}: {kluchi_bez_skobok}")
                    break
            send = bot.send_message(polsovatel1, f"Окей, принял! Нажми кнопку ниже!", reply_markup=markup)
            bot.send_message(polsovatel2, f"Приняли! Ждем выбора {user1}", reply_markup=markup1)
            bot.register_next_step_handler(send, randomaizer_mp_random)
            shifron_mp.clear()
        if message.text.title() == "Нет!":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"].clear()
            send = bot.send_message(polsovatel2, "Введите другие значения в список!", reply_markup=markup2)
            bot.send_message(polsovatel1, f"{user2} сбросил список и сейчас заполняет его заного! Подождите немного!", reply_markup=markup1)
            bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_2)
    elif not message.text.title() in slova:
        send = bot.send_message(message.chat.id, "Ой!")
        bot.register_next_step_handler(send, randomaizer_mp_vibor2)

def randomaizer_mp_vibor2_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Крутить")
    but2 = types.KeyboardButton("Завершить")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardRemove()
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/stop")
    markup2.add(but)
    polsovatel1 = baza_random.find(f"user{message.chat.id}").attrib['id']
    user1 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
    polsovatel2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
    user2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").text
    if message.text.title() in slova:
        if message.text.title() == "Да!":
            shifron_mp = []
            while True:
                kluchi = choice(kluchi_shifron)
                shifron_mp.append(kluchi)
                if len(shifron_mp) == len(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"]):
                    kluchi_bez_skobok = ", ".join(shifron_mp)
                    print(f"Получен новый список от {polsovatel1} и {polsovatel2}: {kluchi_bez_skobok}")
                    break
            bot.send_message(polsovatel2, f"Окей! Ждем пользователя {user1}!", reply_markup=markup1)
            send = bot.send_message(polsovatel1, f"{polsovatel2} принял список! Нажми кнопку ниже!", reply_markup=markup)
            bot.register_next_step_handler(send, randomaizer_mp_random)
            shifron_mp.clear()
        if message.text.title() == "Нет!":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"].clear()
            send = bot.send_message(polsovatel1, "Введите другие значения в список!", reply_markup=markup2)
            bot.send_message(polsovatel2, f"{user1} сбросил список и сейчас заполняет его заного! Подождите немного!", reply_markup=markup1)
            bot.register_next_step_handler(send, randomaizer_mp_vibor_elem_1)
    elif not message.text.title() in slova:
        send = bot.send_message(message.chat.id, "Ой!")
        bot.register_next_step_handler(send, randomaizer_mp_vibor2_2)

def randomaizer_mp_random(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Крутить")
    but2 = types.KeyboardButton("Удалить")
    but3 = types.KeyboardButton("Завершить")
    markup.add(but1, but2).add(but3)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/start")
    markup1.add(but)
    polsovatel1 = baza_random.find(f"user{message.chat.id}").attrib['id']
    user1 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
    polsovatel2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
    user2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").text
    if message.text.title() in slo1_1:
        if message.text.title() == "Крутить":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_itog"] = choice(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"])
            send = bot.send_message(polsovatel1, f"Итог: *" + str(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_itog"]) + "*\n\nВыберите действие ниже!", parse_mode="Markdown", reply_markup=markup)
            bot.send_message(polsovatel2, f"Итог: *" + str(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_itog"]) + f"*\n\nПодождите действие {user1}!", parse_mode="Markdown")
            bot.register_next_step_handler(send, randomaizer_mp_random_vib)
        elif message.text.title() == "Завершить":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"].clear()
            bot.send_message(polsovatel1, "Окей! Завершаем использование сервисом! Спасибо за использование!", reply_markup=markup1)
            bot.send_message(polsovatel2, f"{user1} принял решение завершить работу с рандомайзером! Спасибо за использование!", reply_markup=markup1)
    elif not message.text.title() in slo1_1:
        send = bot.send_message(polsovatel1, "Ой")
        bot.register_next_step_handler(send, randomaizer_mp_random)

def randomaizer_mp_random_vib(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Крутить")
    but2 = types.KeyboardButton("Завершить")
    markup.add(but1, but2)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("/start")
    markup1.add(but)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but3 = types.KeyboardButton("Крутить")
    but4 = types.KeyboardButton("Удалить")
    but5 = types.KeyboardButton("Завершить")
    markup2.add(but3, but4).add(but5)
    polsovatel1 = baza_random.find(f"user{message.chat.id}").attrib['id']
    user1 = baza_random.find(f"user{message.chat.id}").find("namepolsov").text
    polsovatel2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").attrib['id']
    user2 = baza_random.find(f"user{message.chat.id}").find("polsovatel2").text
    if message.text.title() in slo1:
        if message.text.title() == "Удалить":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"].remove(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_itog"])
            if len(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"]) != 0:
                send = bot.send_message(polsovatel1, "Данный элемент удален! Нажмите кнопку ниже!", reply_markup=markup)
                bot.send_message(polsovatel2, f"{user1} удалил из списка *" + str(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_itog"]) + "*! Ждем его действие!", parse_mode="Markdown")
                bot.register_next_step_handler(send, randomaizer_mp_random)
            elif len(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"]) == 0:
                bot.send_message(polsovatel1, "Данный элемент удален, а список весь закончился! Спасибо за уделенное время!", reply_markup=markup1)
                bot.send_message(polsovatel2, "Последний элемент в списке удален, и на сегодня работа закончена! Спасибо за уделенное время!", reply_markup=markup1)
        elif message.text.title() == "Крутить":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_itog"] = choice(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"])
            send = bot.send_message(polsovatel1, f"Итог: *" + str(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_itog"]) + "*\n\nВыберите действие ниже!", parse_mode="Markdown", reply_markup=markup2)
            bot.send_message(polsovatel2, f"Итог: *" + str(random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2_itog"]) + f"*\n\nПодождите действие {user1}!", parse_mode="Markdown")
            bot.register_next_step_handler(send, randomaizer_mp_random_vib)
        elif message.text.title() == "Завершить":
            random_dict[f"{polsovatel1}and{polsovatel2}randomaizer_na_2"].clear()
            bot.send_message(polsovatel1, "Окей! Завершаем использование сервисом! Спасибо за использование!", reply_markup=markup1)
            bot.send_message(polsovatel2, f"{user1} принял решение завершить работу с рандомайзером! Спасибо за использование!", reply_markup=markup1)
    elif not message.text.title() in slo1:
        send = bot.send_message(polsovatel1, "Ой!")
        bot.register_next_step_handler(send, randomaizer_mp_random_vib)

@bot.message_handler(commands=['info'])
def info(message):
    markup = types.ReplyKeyboardMarkup(True)
    but = "/start"
    markup.add(but)
    photo = open("info.jpg", "rb")
    bot.send_photo(message.chat.id, photo=photo, caption=f"*Немножечко о боте:*\n\nKONTROL CHEK inc. официальный бот - это Telegram-бот разработанный KONTROL CHEK для того чтобы мои пользователи могли:\n_1. Подать мне идеи для новых видео на канал KONTROL CHEK!_\n_2. Проверить свой уровень знаний игр Keplerians!_\n_3. Смогли со своими друзьями сыграть в игру Камень-ножницы-бумага (два или три человека)_\n_4. Решить свой спор из-за выбора с помощью Рандомайзера!_\n\nKONTROL CHEK inc. официальный бот разработан на языке Python и работает на сервисе Pythonanywhere от Anaconda (не реклама). Исходный код всегда доступен на Github (ссылка в последнем сообщении)!\n\nВерсия сборки бота: *{vershion}*", parse_mode="Markdown")
    bot.send_message(message.chat.id, f"*О его разработчике:*\n\nKONTROL CHEK - YouTube-геймер из Тульской области, начал ввести свой YouTube-канал в 2020 году под названием МАТЧ! ЖИЗНЬ. Успех пришел после публикации видео «Монахиня в реальной жизни» которая активно идет к отметке 4000 просмотров! В 2021 году канал сменил название на KONTROL CHEK, а позже была опубликована реакция на клип «Райм - Мир», которая принесла ещё большую популярность!\n\nНа данный момент на канале KONTROL CHEK {subscribe} подписчиков и около 130000 просмотров на YouTube за все видеоролики!", parse_mode="Markdown")
    bot.send_message(message.chat.id, "*Социальные сети:*\nИсходный код: [Github](https://github.com/KONTROLCHEK/KONTROL-CHEK-inc.-)\n\n[YouTube](https://www.youtube.com/channel/UC55I9ugkMohczMY8F0WQP6Q)\n[Группа VK](https://vk.com/kontrol.chek)\n[Telegram-канал](https://kontrol_chek185.t.me/)\n[Группа Одноклассники](https://ok.ru/group/61265119084644)\n[Twitch](https://twitch.tv/kontrolchek)\n[Rutube](https://rutube.ru/channel/23551879/)\n[VK Play Live](https://vkplay.live/kontrolchek185)", parse_mode="Markdown")
    bot.send_message(message.chat.id, "Спасибо за использование бота!\n*KONTROL CHEK - МЕНЯЙСЯ К ЛУЧШЕМУ!*", "Markdown", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def ne(message):
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but5 = "/start"
    markup3.add(but5)
    bot.send_message(message.chat.id, "Ой, не совсем тебя понял! Нажми кнопку ниже!", reply_markup=markup3)

bot.polling(none_stop=True, interval=0)
