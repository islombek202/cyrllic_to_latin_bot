import telebot
import os
from dotenv import load_dotenv
from transliterate import to_cyrillic, to_latin
TOKEN = "8780903331:AAEKC36vJuRpIGxSRoGhiIFG2iTNd5TELGE"
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalom alaykum, botimizga xush kelibsiz")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	text = message.text
	if text.isascii():
		bot.reply_to(message, to_cyrillic(text))
	else: 
		bot.reply_to(message, to_latin(text))
bot.infinity_polling()