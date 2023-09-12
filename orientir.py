import telebot
from telebot import types
API_TOKEN = '6329438858:AAFv1pychZrSW1p2CXuKBzWMbhssqhw5gEQ'
bot = telebot.TeleBot(API_TOKEN)

users_answers = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Хочешь узнать, какое направление тебе подходит? Начни тест с командой /test, так же если хотите начать тест заново или он не работает, нажмите кнопку '/start'")

@bot.message_handler(commands=['test'])
def start_test(message):
    users_answers[message.chat.id] = []
    ask_question(message, "Интересуют ли вас новые технологии?", question_2)


def ask_question(message, text, next_function):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton('Да')
    itembtn2 = telebot.types.KeyboardButton('Нет')
    itembtn3 = telebot.types.KeyboardButton('/start')
    markup.add(itembtn1, itembtn2)
    markup.add(itembtn3)
    msg = bot.send_message(message.chat.id, text, reply_markup=markup)
    bot.register_next_step_handler(msg, next_function)


def handle_answer(message, text, next_function):
    if message.text not in ['Да', 'Нет', "/start"]:
        return
    if message.text == '/start':
        send_welcome(message)
        return
    users_answers[message.chat.id].append(message.text)
    ask_question(message, text, next_function)



def question_2(message):
    handle_answer(message, "Легко ли вам объяснять сложные вещи простыми словами?", question_3)

def question_3(message):
    handle_answer(message, "Любите ли вы рисовать или создавать что-то новое?", question_4)

def question_4(message):
    handle_answer(message, "Нравится ли вам работать с числами и схемами?", question_5)

def question_5(message):
    handle_answer(message, "Чувствуете ли вы себя комфортно, помогая и поддерживая других людей?", question_6)

def question_6(message):
    handle_answer(message, "Занимаетесь ли вы каким-либо творчеством в свободное время?", question_7)

def question_7(message):
    handle_answer(message, "Вам интересно узнавать, как устроены различные устройства и механизмы?", question_8)

def question_8(message):
    handle_answer(message, "Важно ли для вас общение с людьми и социальное взаимодействие в работе?", question_9)

def question_9(message):
    handle_answer(message, "Вдохновляют ли вас истории успешных людей в искусстве и культуре?", question_10)

def question_10(message):
    handle_answer(message, "Любите ли вы решать сложные технические задачи?", question_11)

def question_11(message):
    handle_answer(message, "Любите ли вы изучать программирование или кодинг?", question_12)

def question_12(message):
    handle_answer(message, "Интересуют ли вас космические технологии и изучение космоса?", question_13)

def question_13(message):
    handle_answer(message, "Вы бы хотели работать над созданием роботов или искусственного интеллекта?", question_14)

def question_14(message):
    handle_answer(message, "Легко ли вам находить общий язык с разными людьми?", question_15)

def question_15(message):
    handle_answer(message, "Хотели бы вы работать в сфере образования или медицины?", question_16)

def question_16(message):
    handle_answer(message, "Вы чувствуете, что можете вдохновлять других людей?", question_17)

def question_17(message):
    handle_answer(message, "Вы бы хотели заниматься профессиональной фотографией или кинематографом?", question_18)

def question_18(message):
    handle_answer(message, "Вы часто выражаете свои чувства через искусство или музыку?", question_19)

def question_19(message):
    handle_answer(message, "Мечтали ли вы когда-нибудь написать книгу или стать актёром?", evaluate_results)

def evaluate_results(message):
    users_answers[message.chat.id].append(message.text)
    
    technical_mask = [0, 3, 6, 9, 10, 11, 12]
    social_mask = [1, 4, 7, 13, 14, 15]
    creative_mask = [2, 5, 8, 16, 17, 18]

    directions = {
        "technical": sum(1 for index in technical_mask if users_answers[message.chat.id][index] == "Да"),
        "social": sum(1 for index in social_mask if users_answers[message.chat.id][index] == "Да"),
        "creative": sum(1 for index in creative_mask if users_answers[message.chat.id][index] == "Да")
    }

    max_count = max(directions.values())
    top_directions = [direction for direction, count in directions.items() if count == max_count]

    if len(top_directions) == 1:
        if top_directions[0] == "technical":
            markup = telebot.types.InlineKeyboardMarkup()

            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский медицинский колледж", url="https://college.edunetwork.ru/62/41/c2286/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский технологический колледж", url="https://college.edunetwork.ru/62/41/c2282/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский колледж электроники", url="https://college.edunetwork.ru/62/41/c2284/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский политехнический колледж", url="https://college.edunetwork.ru/62/41/c2143/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский железнодорожный колледж", url="https://college.edunetwork.ru/62/41/c767/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский автотранспортный техникум", url="https://college.edunetwork.ru/62/41/c14/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Колледж Рязанский государственный агротехнологический университет им. П.А. Костычева", url="https://college.edunetwork.ru/62/41/c3709/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский многопрофильный колледж", url="https://college.edunetwork.ru/62/41/c2704/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Станкостроительный колледж", url="https://college.edunetwork.ru/62/41/c3625/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский строительный колледж", url="https://college.edunetwork.ru/62/41/c2281/"),
            )

            bot.send_message(message.chat.id, "На основе ваших ответов 📝, я определил, что вам наиболее подходят технические специальности 🛠️. Это могут быть профессии в области инженерии ⚙️, автоматизации 🤖, программирования 💻 и многие другие. Рад сообщить, что есть отличные колледжи с техническим уклоном 🏢. Рекомендую рассмотреть колледжи в списке под сообщением 📋. Уверен, что вы найдете что-то подходящее для своего будущего 🌟!", reply_markup=markup, parse_mode="Markdown")

        elif top_directions[0] == "social":
            markup = telebot.types.InlineKeyboardMarkup()

            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский медицинский колледж", url="https://college.edunetwork.ru/62/41/c2286/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский технологический колледж", url="https://college.edunetwork.ru/62/41/c2282/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский политехнический колледж", url="https://college.edunetwork.ru/62/41/c2143/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский железнодорожный колледж", url="https://college.edunetwork.ru/62/41/c767/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Колледж Рязанский государственный агротехнологический университет им. П.А. Костычева", url="https://college.edunetwork.ru/62/41/c3709/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Колледж Рязанский государственный медицинский университет им. И.П. Павлова", url="https://college.edunetwork.ru/62/41/c2288/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский педагогический колледж", url="https://college.edunetwork.ru/62/41/c3709/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский многопрофильный колледж", url="https://college.edunetwork.ru/62/41/c2704/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский музыкальный колледж", url="https://college.edunetwork.ru/62/41/c2287/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Станкостроительный колледж", url="https://college.edunetwork.ru/62/41/c4883/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Колледж Рязанский институт традиционного прикладного искусства Высшей школы народных искусств", url="https://college.edunetwork.ru/62/41/c3625/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанское художественное училище", url="https://college.edunetwork.ru/62/41/c2290/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Колледж Московский университет им. С.Ю. Витте", url="https://college.edunetwork.ru/62/41/c5014/"),
            )
            bot.send_message(message.chat.id, "На основе анализа ваших ответов 📝, я пришёл к выводу, что вам идеально подойдут социальные специальности ❤️. Это может включать в себя направления, такие как педагогика 🍎, социальная работа 🤝, психология 🧠 и многие другие. Рад сообщить, что существуют колледжи 🎓 с программами в этой области. Откройте для себя новые возможности и найдите учебное заведение, которое поможет вам осуществить свои амбиции в социальной сфере!🌟", reply_markup=markup, parse_mode="Markdown")
        else:
            markup = telebot.types.InlineKeyboardMarkup()

            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский технологический колледж", url="https://college.edunetwork.ru/62/41/c2282/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский многопрофильный колледж", url="https://college.edunetwork.ru/62/41/c2704/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский музыкальный колледж", url="https://college.edunetwork.ru/62/41/c2287/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанское художественное училище", url="https://college.edunetwork.ru/62/41/c2290/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Рязанский строительный колледж", url="https://college.edunetwork.ru/62/41/c2281/"),
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="Колледж Рязанский институт традиционного прикладного искусства Высшей школы народных искусств", url="https://college.edunetwork.ru/62/41/c3625/"),
            )
            bot.send_message(message.chat.id, "Основываясь на ваших ответах и интересах 🌟, могу сказать, что вам отлично подходят творческие специальности 🎨🎭🎵. Будь то изобразительное искусство, музыка, дизайн или литературное творчество, каждое направление способно раскрыть ваш внутренний потенциал. В рязани есть колледжи предлогающие курсы в области творчества 🎓.", reply_markup=markup, parse_mode="Markdown")
    else:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(
                telebot.types.InlineKeyboardButton(text="Колледжи Рязани", url="https://college.edunetwork.ru/62/41/"),
            )
        bot.send_message(message.chat.id, "По результатам анализа 📊, у вас сбалансированные интересы в различных областях. Это потрясающе, так как это делает вас гибким к выбору профессии и учебного заведения 🌟. В Рязани существует множество колледжей, предлагающих обучение по разнообразным специальностям, отражающим ваши интересы. Чтобы ознакомиться с этими направлениями и выбрать подходящий для вас колледж, перейдите по ссылке ниже 🔗.", reply_markup=markup, parse_mode="Markdown")
    
    del users_answers[message.chat.id]

bot.polling(none_stop=True)
