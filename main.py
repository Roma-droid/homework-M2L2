import telebot
from telebot import TeleBot
import lmstudio as lms
bot = telebot.TeleBot()


@bot.message_handler(commands=['start', 'info'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to ChatGPT by nature, write a question")

@bot.message_handler(commands=['about'])
def send_adout(message):
    model = lms.llm("llama-3.1-tulu-3.1-8b")
    result = model.respond("Напиши о природе")
    bot.reply_to(message, result)

@bot.message_handler(commands=['news'])
def send_news(message):
    model = lms.llm("llama-3.1-tulu-3.1-8b")
    result = model.respond("Напиши новости о природе в России")
    bot.reply_to(message, result)




bot.infinity_polling()
