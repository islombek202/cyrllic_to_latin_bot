import telebot
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN="8780903331:AAEC1X6nkjCWzFgm2GZc27XEaHY5q37SbsU"
bot = telebot.TeleBot(TOKEN, parse_mode=None) 
TOKEN=os.getenv("BOT_TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "👋 Assalomu alaykum / Здравствуйте / Hello!\n\n"
    "🤖 Bu bot matnlarni Lotin ➡️ Kirill va Kirill ➡️ Lotin alifbosiga bir zumda o'girib beradi.\n"
    "🤖 Этот бот мгновенно переводит текст с латиницы на кириллицу и наоборот.\n"
    "🤖 This bot instantly converts text between Latin and Cyrillic alphabets.\n\n"
    "✍️ Matnni yuboring / Отправьте текст / Send your text!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
 bot.reply_to(message, message.text)

bot.infinity_polling()