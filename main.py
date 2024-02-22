import telebot

bot = telebot.TeleBot('5865282234:AAEVwLn9TQtcaUo1N5fKDwtByBvqWwfiPhc')

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.reply_to(message, f'hi {message.from_user.first_name} ')
