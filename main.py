# -*- coding: utf-8 -*-
import time

from Token import *
import telebot
from telebot import types

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
    btn2 = types.KeyboardButton('Частые ошибки 🤥')
    btn3 = types.KeyboardButton('Поддержка 🤙')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func_1(message):
    if message.text == 'Как собрать компьютер ? 🤔':
        bot.send_message(message.chat.id, 'Первый этап: *Подготовка*', parse_mode='Markdown')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn2 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn2)
        bot.send_photo(message.chat.id, open('photos/photo_2023-05-03_22-39-55.jpg', 'rb'), 'Для начала подготовьте обычную крестовую отвертку, именно с этим инструментом вы будете работать 95% процентов сборки. 🔩', reply_markup=markup)
        bot.register_next_step_handler(message, func_2)
    elif message.text == 'Поддержка 🤙':
        bot.send_message(message.chat.id, 'Если появились какие-то вопросы на счет функционала бота или вопросы по сборке пк пиши на этот [аккаунт](https://t.me/bashka06), по возможности всем ответим. 😉 Так же нужна обратная связь, поэтому можете писать свое мнение тоже на этот же аккаунт', parse_mode='Markdown')

    elif message.text == 'Частые ошибки 🤥':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(types.KeyboardButton('Неправильное распределение бюджета на будущий компьютер 💸'))
        markup.add(types.KeyboardButton('Экономия на блоке питания ⚠️'))
        markup.add(types.KeyboardButton('Экономия на SSD 💽'))
        markup.add(types.KeyboardButton('Переплата за бренд 🤩'))
        markup.add(types.KeyboardButton('Экономия на двухканальном режиме ОЗУ 🤓'))
        markup.add(types.KeyboardButton('Спешка и неудобное место для сборки 😰'))
        markup.add(types.KeyboardButton('Неправильная установка блока питания 🤔'))
        markup.add(types.KeyboardButton('Неаккуратная установка процессора в сокет 😵‍💫'))
        markup.add(types.KeyboardButton('Неправильная установка материнской платы в корпус ❌'))
        markup.add(types.KeyboardButton('Неправильное подключение проводов 🔌'))
        markup.add(types.KeyboardButton('Вернутся в главное меню⬇️'))
        bot.send_message(message.chat.id, 'Выберите категорию, которая вас интересует!', reply_markup=markup)


    elif message.text == 'Неправильное распределение бюджета на будущий компьютер 💸':
        bot.send_message(message.chat.id, 'Самое главное - определится, какие задачи будет выполнять ваш новый компьютер. Это поможет грамотно распределить бюджет между комплектующими, выбрать максимально подходящую видеокарту и процессор в ваш будущий компьютер.')
    elif message.text == 'Экономия на блоке питания ⚠️':
        bot.send_message(message.chat.id, 'Не экономьте на блоке питания! Экономия на столь ответственном компоненте может сыграть с вами злую шутку. Блок питания отвечает за стабильное питание и безопасность ваших комплектующих. И даже может стать причиной возгорания!'
'Самый частый виновник нестабильной работы компьютера - некачественный блок питания. И что самое страшное, блок питания может отдать концы не один, а прихватив с собой видеокарту или материнскую плату.'
'Первый симптом некачественного блока питания - зависание компьютера, спонтанные перезагрузки, особенно под нагрузкой.')
    elif message.text == 'Экономия на SSD 💽':
        bot.send_message(message.chat.id, "Отсутствие SSD в сборке - это ошибка! Дело даже не в ускорении загрузки операционной системы, а в повышении отклика компьютера на действия пользователя. Щелчок мыши и программа запущена, не надо ждать минуту и слушать треск жесткого диска.Тем более, что SSD стремительно дешевеют. 250 гигабайт вполне хватит на обычную игровую систему."
"Попробовав раз работу с SSD, уже не сможешь отказаться и работа на компьютере с HDD будет казаться мукой.")
    elif message.text == 'Переплата за бренд 🤩':
        bot.send_message(message.chat.id, 'Не стоит переплачивать за комплектующие той или иной компании, даже если вы ее фанат. Особенно, если ваш бюджет ограничен. Несмотря на любовь к определенному бренду, надо быть объективным.'
'Очень часто отказ от свистоперделок и цветомузыки позволяет купить более простую, но более производительную деталь вашего компьютера.'
'Например, любая, даже самая дешевая версия GTX 1660 Ti будет лучше самой навороченной версии GTX 1660 с монструозным охлаждением и 12-ю фазами питания, которые ей совершенно не нужны.')
    elif message.text == 'Экономия на двухканальном режиме ОЗУ 🤓':
        bot.send_message(message.chat.id, 'Всегда ставьте ОЗУ в двухканал. Как показывает практика, большинство компьютеров, собранных с прицелом на будущее и одной планкой ОЗУ на 8 гигабайт, чтобы потом поставить еще 8, так и остаются с этой планкой до своего морального устаревания.'
'Времена, когда пропускная способность памяти была не критична - давно прошли. Игры и прикладной софт очень хорошо отзываются даже на высокочастотную память, не говоря уже о двухканале.')
    elif message.text == 'Спешка и неудобное место для сборки 😰':
        bot.send_message(message.chat.id, 'Не спешить! Вымыть руки прохладной водой с мылом! Поставить хорошее освещение!'
' Мытье рук прохладной водой с мылом уберет с них пот, жир и снизит их выделение. Потожировые следы очень портят вид комплектующих и даже могут вызывать коррозию контактов!'
'Спешка ни к чему хорошему не приводит. Компьютерные компоненты становятся все миниатюрнее с каждым годом и повредить их все легче. Даже небольшой изгиб материнской платы может привести к внутренним микротрещинам.'
'Поэтому не торопитесь, не прикладывайте излишнюю силу, в результате сэкономите кучу времени и денег.'
'Яркий свет крайне важен потому, что в темноте можно ошибиться и легко повредить комплектующие.')
    elif message.text == 'Неправильная установка блока питания 🤔':
        bot.send_message(message.chat.id, 'Блок питания нужно устанавливать в первую очередь! Потом приблизительно уложить провода. Установка блока питания в уже собранный компьютер может легко повредить материнскую плату или видеокарту.')
    elif message.text == 'Неаккуратная установка процессора в сокет 😵‍💫':
        bot.send_message(message.chat.id, 'Сокеты LGA 1151 и им подобные крайне чувствительны к малейшим воздействиям, стоит вам ткнуть туда пальцем или углом процессора, и все, сокет поврежден, ножки погнуты и включение такого компьютера может убить и процессор, и материнскую плату. Процессоры АМ4 несут ножки на себе, и с ними нужно соблюдать не меньшую осторожность. Если что-то идет не так, и процессор не вставляется - не суетитесь и медленно и спокойно все проверьте!')
    elif message.text == 'Неправильная установка материнской платы в корпус ❌':
        bot.send_message(message.chat.id, 'Всегда проверьте перед сборкой - установится ли охлаждение после установки материнской платы в корпус. Обычно всегда удобнее установить охлаждение на процессор и потом устанавливать материнскую плату в корпус. Не забывайте установить заглушку портов до установки материнской платы! Всегда проверяйте количество и места установки латунных стоек материнской платы. Отсутствие стоек может вызвать изгиб и провисание, лишняя стойка может вызвать замыкание! ОЗУ тоже лучше установить в слоты до того, как вы установите материнскую плату в корпус.')
    elif message.text == 'Неправильное подключение проводов 🔌':
        bot.send_message(message.chat.id, 'Иногда встречаются случаи, когда к материнской плате или блоку питания подключают провода не туда, куда нужно. Например, USB от передней панели корпуса в разъем звуковой карты. Будьте аккуратны и читайте мануал.')
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)


def func_2(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_photo(message.chat.id, open('photos/photo_2023-05-05_20-16-17.jpg', 'rb'), 'Далее стоит подготовить термопасту для охлаждения центрального процессора (если термопаста на процессоре стоит с завода, то тюбик с термопастой не понадобится)', reply_markup=markup)
        bot.register_next_step_handler(message, func_3)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
def func_3(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_photo(message.chat.id, open('photos/photo_2023-05-05_20-16-20.jpg', 'rb'),
                       'Понадобится еще один важный элемент - USB-флешка заранее подготовленной с операционной системой. 💽')
        bot.register_next_step_handler(message, func_4)
    elif message.text == 'Назад⬅️':
        bot.send_message(message.chat.id, 'Первый этап: *Подготовка*', parse_mode='Markdown')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn2 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn2)
        bot.send_photo(message.chat.id, open('photos/photo_2023-05-03_22-39-55.jpg', 'rb'),
                       'Для начала подготовьте обычную крестовую отвертку, именно с этим инструментом вы будете работать 95% процентов сборки. 🔩',
                       reply_markup=markup)
        bot.register_next_step_handler(message, func_2)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)

def func_4(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,
                       'С таким небольшим комплектом инструментов и вещей можно *начинать сборку* своего персонального компьютера 😼', parse_mode='Markdown')

        bot.register_next_step_handler(message, func_5)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_photo(message.chat.id, open('photos/photo_2023-05-05_20-16-17.jpg', 'rb'),
                       'Далее стоит подготовить термопасту для охлаждения центрального процессора (если термопаста на процессоре стоит с завода, то тюбик с термопастой не понадобится)',
                       reply_markup=markup)
        bot.register_next_step_handler(message, func_3)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)

def func_5(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Второй этап: *Материнская плата*', parse_mode='Markdown')
        bot.send_photo(message.chat.id, open('photos/Mat_plata.jpg', 'rb'),
                       'Сборку начнем с материнской платы. (*Мат. плата* - является основой построения модульного устройства - компьютера) ⚡️',
                       parse_mode='Markdown', reply_markup=markup)
        bot.send_message(message.chat.id,
                         '💡 Совет все болтики, винтики и провода складывай в контейнер, кружку или другую любую емкость под рукой, чтобы в будущем ничего не потерять.',
                         parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         '💡 После распаковки материнской платы рекомендую положить ее на какую нибудь *мягкую поверхность* или на специальный паралон, который идет обычно в комплекте к материнской плате.',
                         parse_mode='Markdown')
        bot.register_next_step_handler(message, func_6)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_photo(message.chat.id, open('photos/photo_2023-05-05_20-16-20.jpg', 'rb'),
                       'Понадобится еще один важный элемент - USB-флешка заранее подготовленной с операционной системой. 💽')
        bot.register_next_step_handler(message, func_4)


def func_6(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,
                         'Третий этап: *Установка процессора*', parse_mode='Markdown')

        bot.send_message(message.chat.id,
                       '*Центральный процессор* - это электронный блок и главная часть аппаратного обеспечения твоего компьютера. Устанавливается в сокет материнской платы.',
                       parse_mode='Markdown', reply_markup=markup)

        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('photos/photo_2_2023-05-01_22-55-42.jpg', 'rb')), telebot.types.InputMediaPhoto(open('photos/photo_5_2023-05-01_23-01-03.jpg', 'rb'))])
        bot.send_message(message.chat.id, '💡Для установки процессора нам нужна плавно в центре материнской платы открыть сокет, *потенув рычажок вверх*. Далее металической стороной вверх устанавливаем процессор в сокет. 📥',
                         parse_mode='Markdown')

        bot.send_message(message.chat.id,
                         'Очень важная деталь ❗️: У процессора на одном из углов есть треугольник, он называются *ключик*. На сокете тоже находятся точно такой же ключик вам нужно установить их к правильной стороной к друг другу иначе процессор не вставится в сокет. 🔐',
                         parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_7)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Второй этап: *Материнская плата*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/Mat_plata.jpg', 'rb'),
                       'Сборку начнем с материнской платы. (*Мат. плата* - является основой построения модульного устройства - компьютера) ⚡️',
                       parse_mode='Markdown', reply_markup=markup)

        bot.send_message(message.chat.id,
                         '💡 Совет все болтики, винтики и провода складывай в контейнер, кружку или другую любую емкость под рукой, чтобы в будущем ничего не потерять.',
                         parse_mode='Markdown')

        bot.send_message(message.chat.id,
                         '💡 После распаковки материнской платы рекомендую положить ее на какую нибудь *мягкую поверхность* или на специальный паралон, который идет обычно в комплекте к материнской плате.',
                         parse_mode='Markdown')
        bot.register_next_step_handler(message, func_6)


def func_7(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Если процессор встал нормально, то могу поздравить тебя с установкой процессора 🎉. Правда это было одно из самых простых этапов, поэтому уверенно двигаемся дальше! 💪', parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_8)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,
                         'Третий этап: *Установка процессора*', parse_mode='Markdown')

        bot.send_message(message.chat.id,
                         '*Центральный процессор* - это электронный блок и главная часть аппаратного обеспечения твоего компьютера. Устанавливается в сокет материнской платы.',
                         parse_mode='Markdown', reply_markup=markup)

        bot.send_media_group(message.chat.id,
                             [telebot.types.InputMediaPhoto(open('photos/photo_2_2023-05-01_22-55-42.jpg', 'rb')),
                              telebot.types.InputMediaPhoto(open('photos/photo_5_2023-05-01_23-01-03.jpg', 'rb'))])
        bot.send_message(message.chat.id,
                         '💡Для установки процессора нам нужна плавно в центре материнской платы открыть сокет, *потенув рычажок вверх*. Далее металической стороной вверх устанавливаем процессор в сокет. 📥',
                         parse_mode='Markdown')

        bot.send_photo(message.chat.id,
                       'Очень важная деталь ❗️: У процессора на одном из углов есть треугольник, он называются *ключик*. На сокете тоже находятся точно такой же ключик вам нужно установить их к правильной стороной к друг другу иначе процессор не вставится в сокет. 🔐',
                       parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_7)

def func_8(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,
                         'Четвертый этап: *Установка оперативной памяти*', parse_mode='Markdown', reply_markup=markup)

        bot.send_photo(message.chat.id, open('photos/modul-ozu.jpg', 'rb'),
                         '*Оперативка* - энергозависимая часть системы компьютерной памяти, в которой во время работы компьютера хранится выполнимый машинный код, а также входные, выходные и промежуточные данные.', parse_mode='Markdown')
        bot.send_photo(message.chat.id, open('photos/photo_12_2023-05-01_23-01-03.jpg', 'rb'), 'Для начала находим слоты под оперативную память на материнской плате, выглядят они примерно так: ', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_9)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,
                         'Если процессор встал нормально, то могу поздравить тебя с установкой процессора 🎉. Правда это было одно из самых простых этапов, поэтому уверенно двигаемся дальше! 💪',
                         parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_8)

def func_9(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,
                         'После вам нужно с небольшим усилием открыть замки которые находятся сбоку от слотов оперативной памяти.', parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_10)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,
                         'Четвертый этап: *Установка оперативной памяти*', parse_mode='Markdown', reply_markup=markup)

        bot.send_photo(message.chat.id, open('https://mirinfo.ru/wp-content/uploads/2021/11/modul-ozu.jpg', 'rb'),
                       '*Оперативка* - энергозависимая часть системы компьютерной памяти, в которой во время работы компьютера хранится выполнимый машинный код, а также входные, выходные и промежуточные данные.',
                       parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_12_2023-05-01_23-01-03.jpg', 'rb'),
                       'Для начала находим слоты под оперативную память на материнской плате, выглядят они примерно так: ',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_9)

def func_10(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,
                         'Для установки вам нужно найти на оперативной памяти прорези и сопоставить их с прорезями на слотах мат. платы. Немного надавливаем на оперативную память до *щелчка*', parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_11)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,
                         'После вам нужно с небольшим усилием открыть замки которые находятся сбоку от слотов оперативной памяти.',
                         parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_10)

def func_11(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Пятый этап: *Установка SSD M2*', parse_mode='Markdown', reply_markup=markup)

        bot.send_message(message.chat.id, '*SSD (Solid State Drive)*- устройство для постоянного хранения данных с использованием твердотельной (обычно - флэш) памяти. 💾', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_9_2023-05-01_23-01-03.jpg', 'rb'),
                         'Ищем слот для SSD на материнской плате. Аккуратно его вставляем сначала под углом. После берем винтик который идет идет в комплекте и надавливаем SSD вниз и *фиксируем диск винтиком* (закручиваем не до упора).', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_12)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,
                         'Для установки вам нужно найти на оперативной памяти прорези и сопоставить их с прорезями на слотах мат. платы. Немного надавливаем на оперативную память до *щелчка*',
                         parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_11)

def func_12(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id,  'Шестой этап: *Установка кулера на центральный процессор*', parse_mode='Markdown', reply_markup=markup)
        bot.send_photo(message.chat.id, open('photos/Screenshot_13.png', 'rb'), 'Вернемся к нашему процессору, протираем наш процессор влажный диском 🧽. Рядом с процессором есть заглушки которые нужно открутить отверткой. ⚙️', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_13)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Пятый этап: *Установка SSD M2*', parse_mode='Markdown', reply_markup=markup)

        bot.send_message(message.chat.id,
                         '*SSD (Solid State Drive)*- устройство для постоянного хранения данных с использованием твердотельной (обычно - флэш) памяти. 💾',
                         parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_9_2023-05-01_23-01-03.jpg', 'rb'),
                       'Ищем слот для SSD на материнской плате. Аккуратно его вставляем сначала под углом. После берем винтик который идет идет в комплекте и надавливаем SSD вниз и *фиксируем диск винтиком* (закручиваем не до упора).',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_12)

def func_13(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_photo(message.chat.id, open('photos/photo_7_2023-05-01_23-01-03.jpg', 'rb'),
                         'Далее наносим термопасту. Важный момент ❗️ Пасту лучше наносить аккуратным тонким слоем и постараться, чтобы паста была на *всей поверхности* процессора. Именно в таком случае охлаждение будет лучше и эффективнее.', parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_14)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Шестой этап: *Установка кулера на центральный процессор*',
                         parse_mode='Markdown', reply_markup=markup)
        bot.send_photo(message.chat.id, open('photos/Screenshot_13.png', 'rb'),
                       'Вернемся к нашему процессору, протираем наш процессор влажный диском 🧽. Рядом с процессором есть заглушки которые нужно открутить отверткой. ⚙️',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_13)

def func_14(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_photo(message.chat.id, open('photos/photo_8_2023-05-01_22-55-42.jpg', 'rb'),
                         'После нанесения термопасты аккуратно ставим кулер железной поверхностью вниз на процессор.', parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_15)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_photo(message.chat.id, open('photos/photo_7_2023-05-01_23-01-03.jpg', 'rb'),
                       'Далее наносим термопасту. Важный момент ❗️ Пасту лучше наносить аккуратным тонким слоем и постараться, чтобы паста была на *всей поверхности* процессора. Именно в таком случае охлаждение будет лучше и эффективнее.',
                       parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_14)

def func_15(message):
    if message.text == 'Далее➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_photo(message.chat.id, open('photos/photo_9_2023-05-01_22-55-42.jpg', 'rb'),
                         'После этих действий подключаем провод от кулера в слот рядом с процессором 🔌', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_16)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_photo(message.chat.id, open('photos/photo_8_2023-05-01_22-55-42.jpg', 'rb'),
                       'После нанесения термопасты аккуратно ставим кулер железной поверхностью вниз на процессор.',
                       parse_mode='Markdown', reply_markup=markup)
        bot.register_next_step_handler(message, func_15)

def func_16(message):
    if message.text == 'Далее➡️':
        bot.send_message(message.chat.id,
                         'Седьмой этап: *Распаковка корпуса*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_3_2023-05-01_22-55-42.jpg', 'rb'),
                         'Достаем корпус из коробки и прикручиваем винтиками которые идут в комплекте вентиляторы сбоку корпуса (у каждого корпуса вентиляторы в разном месте находятся).', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_17)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Далее➡️')
        btn3 = types.KeyboardButton('Вернутся в главное меню⬇️')
        markup.add(btn1)
        markup.add(btn3)
        bot.send_photo(message.chat.id, open('photos/photo_9_2023-05-01_22-55-42.jpg', 'rb'),
                       'После этих действий подключаем провод от кулера в слот рядом с процессором 🔌',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_16)

def func_17(message):
    if message.text == 'Далее➡️':
        bot.send_message(message.chat.id,
                         'Седьмой этап: *Установка блока питания*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_7_2023-05-01_22-55-42.jpg', 'rb'),
                         'Вставляем блок питания *вниз корпуса* в определенный для него отсек. С другой стороны корпуса прикручиваем блок питания болтиками.', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_18)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_message(message.chat.id,
                         'Седьмой этап: *Распаковка корпуса*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_3_2023-05-01_22-55-42.jpg', 'rb'),
                       'Достаем корпус из коробки и прикручиваем винтиками которые идут в комплекте вентиляторы сбоку корпуса (у каждого корпуса вентиляторы в разном месте находятся).',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_17)

def func_18(message):
    if message.text == 'Далее➡️':
        bot.send_message(message.chat.id,
                         'Как ты мог заметить у блока питания много проводов😵‍💫. Сейчас я *объясню* какой провод за что отвечает.', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/Screenshot_1.png', 'rb'),
                         'Этот провод отвечает за *питание материнской платы*, я думаю ты сразу его заметишь. Подключаем его обычно в правый угол материнской платы.', parse_mode='Markdown')
        bot.send_photo(message.chat.id, open('photos/Screenshot_2.png', 'rb'))
        bot.register_next_step_handler(message, func_19)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_message(message.chat.id,
                         'Седьмой этап: *Установка блока питания*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_7_2023-05-01_22-55-42.jpg', 'rb'),
                       'Вставляем блок питания *вниз корпуса* в определенный для него отсек. С другой стороны корпуса прикручиваем блок питания болтиками.',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_18)

def func_19(message):
    if message.text == 'Далее➡️':
        bot.send_photo(message.chat.id, open('photos/Screenshot_3.png', 'rb'), 'Следующий провод это *питание для центрального процессора* (чаще всего подписывается CPU). Подключаем в левый верхний угол материнской платы.',
                       parse_mode='Markdown')
        bot.send_photo(message.chat.id, open('photos/Screenshot_4.png', 'rb'))
        bot.register_next_step_handler(message, func_20)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_message(message.chat.id,
                         'Как ты мог заметить у блока питания много проводов😵‍💫. Сейчас я *объясню* какой провод за что отвечает.',
                         parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/Screenshot_1.png', 'rb'),
                       'Этот провод отвечает за *питание материнской платы*, я думаю ты сразу его заметишь. Подключаем его обычно в правый угол материнской платы.',
                       parse_mode='Markdown')
        bot.send_photo(message.chat.id, open('photos/Screenshot_2.png', 'rb'))
        bot.register_next_step_handler(message, func_19)

def func_20(message):
    if message.text == 'Далее➡️':
        bot.send_photo(message.chat.id, open('photos/Screenshot_5.png', 'rb'),
                         'Дальше очень похожий провод - это *питание для твоей видеокарты*, подключается напрямую в твой видеокарту.', parse_mode='Markdown')
        bot.send_photo(message.chat.id, open('photos/Screenshot_6.png'))
        bot.register_next_step_handler(message, func_21)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_photo(message.chat.id, open('photos/Screenshot_3.png', 'rb'),
                       'Следующий провод это *питание для центрального процессора* (чаще всего подписывается CPU). Подключаем в левый верхний угол материнской платы.',
                       parse_mode='Markdown')
        bot.send_photo(message.chat.id, open('photos/Screenshot_4.png'))
        bot.register_next_step_handler(message, func_20)

def func_21(message):
    if message.text == 'Далее➡️':
        bot.send_photo(message.chat.id, open('photos/Screenshot_7.png', 'rb'),
                         'Последние провода служат для подключения *жестких дисков и вентиляторов и подсветки*', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_22)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_photo(message.chat.id, open('photos/Screenshot_5.png', 'rb'),
                       'Дальше очень похожий провод - это *питание для твоей видеокарты*, подключается напрямую в твой видеокарту.',
                       parse_mode='Markdown')
        bot.send_photo(message.chat.id, open('photos/Screenshot_6.png'))
        bot.register_next_step_handler(message, func_21)

def func_22(message):
    if message.text == 'Далее➡️':
        bot.send_message(message.chat.id,
                         'После небольшой теории по проводам переходим к следующему 8 этапу: *Установка материнской платы*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/Screenshot_8.png'),
                         'Для начала в корпус вставляем заглушку на месте где будет материнская плата. Вставляем ее вот таким образом:', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_23)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_photo(message.chat.id, open('photos/Screenshot_7.png', 'rb'),
                       'Последние провода служат для подключения *жестких дисков и вентиляторов и подсветки*',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_22)

def func_23(message):
    if message.text == 'Далее➡️':
        bot.send_message(message.chat.id,
                         'Дальше закрепляем материнскую плату специальными ножками, которые идут в комплекте сопостовляя разъемы с отверстиями в заглушке.', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_24)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_message(message.chat.id,
                         'После небольшой теории по проводам переходим к следующему 8 этапу: *Установка материнской платы*',
                         parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/Screenshot_8.png', 'rb'),
                       'Для начала в корпус вставляем заглушку на месте где будет материнская плата. Вставляем ее вот таким образом:',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_23)

def func_24(message):
    if message.text == 'Далее➡️':
        bot.send_message(message.chat.id,
                        'Девятый этап: *Установка жесткого диска*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_1_2023-05-01_22-55-47.jpg'),
                         'Жесткий диск устанавливается в специальные отсеки внизу корпуса (похожие на небольшие железные полочки). Достаем данные отсеки прикручиваем их к жетским дискам и убираем обратно в корпус. Подключаем жесткий диск при помощи *кабелей SATA* и от блока питания *T-образный провод*. Подключаем их к жесткому диску. Берем другой конец провода SATA и подключаем их к нужному разъему материнской платы (обычно эти разъемы находятся сбоку).', parse_mode='Markdown')
        bot.send_photo(message.chat.id, open('photos/Screenshot_9.png'),
                       'Подключаем жесткий диск при помощи *кабелей SATA* и от блока питания *T-образный провод*. Подключаем их к жесткому диску. Берем другой конец провода SATA и подключаем их к нужному разъему материнской платы (обычно эти разъемы находятся сбоку).',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_25)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_message(message.chat.id,
                         'Дальше закрепляем материнскую плату специальными ножками, которые идут в комплекте сопостовляя разъемы с отверстиями в заглушке.',
                         parse_mode='Markdown')
        bot.register_next_step_handler(message, func_24)

def func_25(message):
    if message.text == 'Далее➡️':
        bot.send_message(message.chat.id, 'Переходим к самому сложному этапу - *Подключение всех проводов*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/Screenshot_10.png'), 'Вентиляторы подключаются напрямую к материнской плате в *разъемы FAN*', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_26)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_message(message.chat.id,
                         'Девятый этап: *Установка жесткого диска*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_1_2023-05-01_22-55-47.jpg'),
                       'Жесткий диск устанавливается в специальные отсеки внизу корпуса (похожие на небольшие железные полочки). Достаем данные отсеки прикручиваем их к жетским дискам и убираем обратно в корпус. Подключаем жесткий диск при помощи *кабелей SATA* и от блока питания *T-образный провод*. Подключаем их к жесткому диску. Берем другой конец провода SATA и подключаем их к нужному разъему материнской платы (обычно эти разъемы находятся сбоку).',
                       parse_mode='Markdown')
        bot.send_photo(message.chat.id, open('photos/Screenshot_9.png'),
                       'Подключаем жесткий диск при помощи *кабелей SATA* и от блока питания *T-образный провод*. Подключаем их к жесткому диску. Берем другой конец провода SATA и подключаем их к нужному разъему материнской платы (обычно эти разъемы находятся сбоку).',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_25)

def func_26(message):
    if message.text == 'Далее➡️':
        bot.send_photo(message.chat.id, open('photos/Screenshot_11.png'), 'Далее берем *кабель HDD-AUDIO*, который отвечает за наушники и микрофон. Ищем 2 разъема HDD-AUDIO на материнской плате и двумя сторонами провода подключаем их по кротчайшему пути.', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_27)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_message(message.chat.id, 'Переходим к самому сложному этапу - *Подключение всех проводов*',
                         parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/Screenshot_10.png'),
                       'Вентиляторы подключаются напрямую к материнской плате в *разъемы FAN*', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_26)

def func_27(message):
    if message.text == 'Далее➡️':
        bot.send_photo(message.chat.id, open('photos/photo_26_2023-05-01_23-01-03.jpg', 'rb'), 'Подключаем провод USB так же по кротчайшему пути на материнской плате. Позже уже подключаем большой кабель USB 3.0. На материнской плате будет похожий разъем как провод и с похожим названием.', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_28)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_photo(message.chat.id, open('photos/Screenshot_11.png'),
                       'Далее берем *кабель HDD-AUDIO*, который отвечает за наушники и микрофон. Ищем 2 разъема HDD-AUDIO на материнской плате и двумя сторонами провода подключаем их по кротчайшему пути.',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_27)

def func_28(message):
    if message.text == 'Далее➡️':
        bot.send_photo(message.chat.id, open('photos/photo_30_2023-05-01_23-01-03.jpg', 'rb'),
                         'Подключаем провод от блока питания CPU и на материнской плате находим такой же разъем. После берем большой кабель для питания материнской платы и подключаем ее также к плате.', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_29)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_photo(message.chat.id, open('photos/photo_26_2023-05-01_23-01-03.jpg', 'rb'),
                       'Подключаем провод USB так же по кротчайшему пути на материнской плате. Позже уже подключаем большой кабель USB 3.0. На материнской плате будет похожий разъем как провод и с похожим названием.',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_28)

def func_29(message):
    if message.text == 'Далее➡️':
        bot.send_message(message.chat.id, '11 этап: *Установка видеокарты*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_16_2023-05-01_23-01-03.jpg', 'rb'), 'Примеряем видеокарту в корпус и выкручиваем нужные заглушки из корпуса. После этого в слоте под видеокарту открываем спец. ключик и вставляем в этот слот нашу видеокарту. Берем провод на 12V⚡️ и проводим через корпус провод подключая к видеокарте.', parse_mode='Markdown')

        bot.send_message(message.chat.id,
                         'После этого рекомендую тебе провести небольшой кабель-менеджмент, используя тяжки для проводов.🤓 После подключаем к компьютеру перефирию: наушники, клавиатуру и т.д. 🎧 ⌨️', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_30)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_photo(message.chat.id, open('photos/photo_30_2023-05-01_23-01-03.jpg', 'rb'),
                       'Подключаем провод от блока питания CPU и на материнской плате находим такой же разъем. После берем большой кабель для питания материнской платы и подключаем ее также к плате.',
                       parse_mode='Markdown')
        bot.register_next_step_handler(message, func_29)

def func_30(message):
    if message.text == 'Далее➡️':
        bot.send_photo(message.chat.id, open('photos/photo_5_2023-05-01_22-55-50.jpg', 'rb'),
                         'Поздравляю, ты собрал компьютер! 🥳 Желаю тебе удачного пользования. Заботься и ухаживай за своим устройством, если появились какие то вопросы я буду рад на них ответить!', parse_mode='Markdown')
        bot.register_next_step_handler(message, func_31)
    elif message.text == 'Вернутся в главное меню⬇️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Как собрать компьютер ? 🤔')
        btn2 = types.KeyboardButton('Частые ошибки 🤥')
        btn3 = types.KeyboardButton('Поддержка 🤙')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         'Привет! Я бот-помощник 🤖, помогу тебе во время сборки своего компьютера. Я тебе покажу, что собирать свой компьютер это не совсем сложно, а интересно и довольно легко.\nЯ поэтапно расскажу и покажу, как собрать компьютер в домашних условиях. Ты сможешь, пересмотреть каждый этап и также отдельно будет полное руководство, как собрать по запчастям свой компьютер.\n Расскажу о популярных проблемах которые возникают во время сборки пк и покажу как их решить',
                         reply_markup=markup)
    elif message.text == 'Назад⬅️':
        bot.send_message(message.chat.id, '11 этап: *Установка видеокарты*', parse_mode='Markdown')

        bot.send_photo(message.chat.id, open('photos/photo_16_2023-05-01_23-01-03.jpg', 'rb'),
                       'Примеряем видеокарту в корпус и выкручиваем нужные заглушки из корпуса. После этого в слоте под видеокарту открываем спец. ключик и вставляем в этот слот нашу видеокарту. Берем провод на 12V⚡️ и проводим через корпус провод подключая к видеокарте.',
                       parse_mode='Markdown')

        bot.send_message(message.chat.id,
                         'После этого рекомендую тебе провести небольшой кабель-менеджмент, используя тяжки для проводов.🤓 После подключаем к компьютеру перефирию: наушники, клавиатуру и т.д. 🎧 ⌨️',
                         parse_mode='Markdown')
        bot.register_next_step_handler(message, func_30)


bot.polling(non_stop=True)