import telebot

bot = telebot.TeleBot('6541411646:AAHBVULnZze-XpGu491ivHvv_SSnJwQvWcs')

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.reply_to(message, f'hi {message.from_user.first_name} ')
