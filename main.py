import telebot
import os
from dotenv import load_dotenv
from transliterate import to_cyrillic, to_latin
TOKEN = "8780903331:AAFengmcAYh7vyf0xD8wzvY2-dZbgL3nybQ"
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id,"✨ Xush kelibsiz 👋🏻\n\n🌐 Cyrillic ⇄ Latin Converter Bot\n\n🔄 Kirill va lotin yozuvlarini\nbir zumda o‘zgartiring!\n\n⚡ Tezkor\n💎 Qulay\n🚀 Zamonaviy\n\n📝 Matningizni yuboring 👇\n\n🔄⚡🌐🔥")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	text = message.text
	if text.isascii():
		bot.send_message(message.chat.id, to_cyrillic(text))
	else: 
		bot.send_message(message.chat.id, to_latin(text))
bot.infinity_polling()
print(TOKEN)