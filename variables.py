import xml.etree.ElementTree as ET

language = 'ru'
chat = ''
chat1 = ''
kamen = "Камень"
noshik = "Ножницы"
bumaga = "Бумага"
stop = "/stop"
kanal = "@kontrol_chek185"

shet = {}
idea = {}
random_dict = {}

baza = ET.parse("baza.xml")
root = baza.getroot()
baza_random = ET.parse("bazarandomaizer.xml")
baza_random_r = baza_random.getroot()
kmn2 = ET.parse("bazakmn2.xml")
kmn2r = kmn2.getroot()
kmn3 = ET.parse("bazakmn3.xml")
kmn3r = kmn3.getroot()

vershion = "1.5"
subscribe = "1120"
text_AttributeError = "Пожалуйста, выберите заново способ приглашения друга!"
text = "[здесь](https://t.me/kontrol_chek185/1131)"
text2 = f"Попросите вашего друга зайти в бот и нажать кнопку /start, а потом внизу выберите заново способ приглашения друга и повторите попытку, либо нажмите {stop} для прекращения приглашений друга!!\nОшибка повторяется? Ответ ищите [здесь](https://t.me/kontrol_chek185/1131)"
text3 = "Выберите способ приглашения друга снова и попробуйте еще раз!"
text_photo = "*Важно! Что такое Chat Id и как его получить?*\nChat Id - это уникальный идентификатор, который используется в ботах для отправки сообщений пользователям (надеюсь объяснил понятно).\nДля того чтобы получить Chat Id вашего друга нужно найти сообщение друга и отправить его боту @userinfobot и скопировать набор цифр из *ВТОРОЙ СТРОКИ* и отправить его в ответ на это сообщение!\n_P.S. кнопка /stop это для того чтобы отменить выбор!_"
black_list_text = "Вы добавлены в черный список этого бота!"
bot_knb1 = [kamen, noshik, bumaga, stop]
bot_knb = ["Камень", "Ножницы", "Бумага"]
kmn_reshim = ["Одиночный", "Сетевой"]
admin_chat = [chat, chat1]
slova = ["Да!", "Нет!"]
blogers = ["KONTROL CHEK", "IlyuhichPLAY"]
slo1 = ["Крутить", "Удалить", "Завершить"]
slo1_1 = ["Крутить", "Завершить"]
kluchi_shifron = ["24gjshtu35", "7kd66sgsty", "dgnhj246cx", "124hgjydss", "78e4gaytre", "232ccxuk44", "56njhftttt", "445gfsytrw", "086chgdfdd", "1233ffyrey", "rrw444dksh", "gfrrgr4566", "qw434gfh34", "mnv664ngbx", "kjyu562gse", "rytjhg3442", "klhopg4543", "243hgs6uyu", "7kjg8l7g8", "gra412grwr", "rhteyh2y6j", "h54u2u65j", "g525y5h52", "4y52jhj62", "h264u632uh", "6423ujj62", "jnyj475hg", "kkuukjuo6", "kj47uku6847", "ujtkjrutkur", "m4k675um745", "rg2hth325", "btwh6jh63", "tw365h36h", "n6356j35jyhg", "ytreukut5", "jyeje6u47", "jtryyurkj4", "jyteyjj547", "aeqwtgt4rq", "qgrgqwehw24", "52htrhytrh", "35htjhyrj6jy", "rsjjyeyuy543", "h645u6u32j63", "yjejytj7kj6", "wrjywjwuy", "tjh6j356iy", "agtqty456n", "kulilio88lo", "jhfbgfhgg7", "45ythyth6ru6u", "thytjyjy6h4", "thhjjdytjy656", "gfhtjht432"]
vib = ["Да!", "Нет!"]
vib1 = ["Отменить игру", "Пригласить другого пользователя", "Играть в двоем"]
kmn_kolvo = ["2 игрока", "3 игрока"]
slova2 = ["Передать возможность добавить второму игроку нужное значение", "Передать возможность добавить первому игроку нужное значение", "/stop"]
sposob_prig = ["Через Сообщения От Друга", "Через Chat Id"]
text_photo1 = f"Отлично! Введи Chat Id одного из нужных пользователя!\n{text_photo}"
kto_priglasit = ["Я", "Игрок 2"]
poluchat = ["Внутри бота!", "В ТГ-канал"]
ft = ["Фото", "Текст"]
deis_mes = ["Изменить его", "Удалить"]
