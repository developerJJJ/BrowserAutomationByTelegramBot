import os
import telebot

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['run'])
def greet(message):
    bot.reply_to(message, "This bot is made by chatGPT")

bot.polling()