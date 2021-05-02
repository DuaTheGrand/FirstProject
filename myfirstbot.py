import telebot

bot = telebot.TeleBot('1789846365:AAG2r5Rc1Qrun93V8RUYsgsONeSKkG6s2QM')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Я тестовый бот Руслана. Это его первый бот, поэтому в нем могут быть неполадки. Я знаю команды "привет", "как дела?". А так, приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Здравствуй!')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.from_user.id, 'Прекрасно, у Вас как?')
    else:
        bot.send_message(message.from_user.id, 'Неизвестная команда!')

bot.polling(none_stop=True)