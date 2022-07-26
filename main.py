#---ДЛЯ РАБОТЫ БОТА НУЖНО УСТАНОВИТЬ (pip install pyTelegramBotApi)
#---Токен бота: "5399221206:AAFu23E3eszo8cTKmxxa1stLvsDLkyRUn14"

import telebot
from telebot import types    #---Для создания меню используется telebot pypes. Мы можем вызывать его обращаясь к телеботу - telebot.pypes или, импортируя, обращаться прямо к types.

bot = telebot.TeleBot("5399221206:AAFu23E3eszo8cTKmxxa1stLvsDLkyRUn14")
apiToken = "a131f75fed65d9b30b5cef60ad696592"

token = "5399221206:AAFu23E3eszo8cTKmxxa1stLvsDLkyRUn14"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])                     #---Обработчик сообщений на команду "start".
def start(message):                                          #---Функция, которая принимает message.
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #---Создаем меню-клавиатуру и прописываем атрибут, позволяющий кнопкам подстраиваться под параметры экрана.
    #---Создаем клавиатуру.
    free_button = types.KeyboardButton('☢ Свободная кнопка')
    weather = types.KeyboardButton('🌦 ПОГОДА')
    exchange_rates= types.KeyboardButton('💹 КУРСЫ ВАЛЮТ')
    website1 = types.KeyboardButton('💾 ИНФОРМАЦИЯ')
    website2 = types.KeyboardButton('🛒 МАГАЗИН')
    markup.add(free_button, weather, exchange_rates, website1, website2)   #---Чтобы добавить кнопки в меню.

    #---Чтобы кнопки появились на экране, нужно через бота отправить какое-то сообщение. Чтобы вывести меню пользователю - reply_markup.
    bot.send_message(message.chat.id, f'<b>Здравствуйте, {message.from_user.first_name}!\n'
                                      f'Пожалуйста, выберите интересующую вас категорию.</b> ', parse_mode='html', reply_markup=markup)




#---ОТСЛЕЖИВАНИЕ КНОПОК. (Когда нажимаем кнопку - в чат отправляется сообщение. По этому сообщению идет отслеживание).
@bot.message_handler(content_types=['text'])
def botMessage(message):
    if message.text == "☢ Свободная кнопка":
        bot.send_message(message.chat.id, "🚫")

    elif message.text == "🌦 ПОГОДА":
        bot.send_message(message.chat.id, "<b>🔧 Функция в разработке</b>", parse_mode='html')

    elif message.text == "💹 КУРСЫ ВАЛЮТ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        dollar = types.KeyboardButton('$ Доллар')
        euro = types.KeyboardButton('€ Евро')
        ruble = types.KeyboardButton('₽ Рубль')
        tenge = types.KeyboardButton('₸ Тенге')
        back = types.KeyboardButton('🔙Назад')
        start = types.KeyboardButton("/start")

        markup.row(dollar, euro, ruble, tenge)
        markup.row(back)
        markup.row(start)

        bot.send_message(message.chat.id, "<b>ВЫБЕРИТЕ ВАЛЮТУ:</b>", parse_mode='html', reply_markup=markup)

    elif message.text == "💾 ИНФОРМАЦИЯ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot_info = types.KeyboardButton('🤖О БОТЕ')
        life_info = types.KeyboardButton('🧬О ЖИЗНИ')
        back = types.KeyboardButton('🔙Назад')
        start = types.KeyboardButton("/start")

        markup.row(bot_info, life_info)
        markup.row(back)
        markup.row(start)

        bot.send_message(message.chat.id, "<b>ИНФОРМАЦИЯ:</b>", parse_mode='html', reply_markup=markup)

    elif message.text == "🛒 МАГАЗИН":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        catalog = types.KeyboardButton('📒КАТАЛОГ')
        admin = types.KeyboardButton('🤵АДМИН')
        delivery = types.KeyboardButton('🚛ДОСТАВКА')
        back = types.KeyboardButton('🔙Назад')
        start = types.KeyboardButton("/start")

        markup.row(catalog, admin, delivery)
        markup.row(back)
        markup.row(start)

        bot.send_message(message.chat.id, "<b>ВЫБЕРИТЕ НУЖНЫЙ РАЗДЕЛ:</b>", parse_mode='html', reply_markup=markup)


    elif message.text == "🔙Назад":
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True)  # ---Создаем меню-клавиатуру и прописываем атрибут, позволяющий кнопкам подстраиваться под параметры экрана.
        # ---Создаем клавиатуру.
        free_button = types.KeyboardButton('☢ Свободная кнопка')
        weather = types.KeyboardButton('🌦 ПОГОДА')
        exchange_rates = types.KeyboardButton('💹 КУРСЫ ВАЛЮТ')
        website1 = types.KeyboardButton('💾 ИНФОРМАЦИЯ')
        website2 = types.KeyboardButton('🛒 МАГАЗИН')

        markup.add(free_button, weather, exchange_rates, website1, website2)  # ---Чтобы добавить кнопки в меню.
        # ---Чтобы кнопки появились на экране, нужно через бота отправить какое-то сообщение. Чтобы вывести меню пользователю - reply_markup.
        bot.send_message(message.chat.id,"<b>ПЕРЕХОДИМ К ОСНОВНОМУ МЕНЮ:</b>", parse_mode='html', reply_markup=markup)


bot.infinity_polling()  #---Чтобы бот не отключался.










