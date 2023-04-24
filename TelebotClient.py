import telebot
import os
import socket

TOKEN = os.getenv("TOKEN")
print(TOKEN)

# Set up the socket connection to the Selenium script
# Create TCP socket
host = "localhost"
port = 9226

s = socket.create_connection((host, port))
print(f"Connected to the server at {host}:{port}")

# Replace YOUR_TOKEN_HERE with your bot's token
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to my bot!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "This bot can perform various tasks. Here are the available commands:\n/move - move to a specified URL\n/get_title - get the title of the current page\n/stop - stop the bot")

@bot.message_handler(commands=['move'])
def move_to_url(message):
    # Replace with your code to move to a specified URL
    url = message.text.replace("/move ", "").strip()
    print(url)
    try:
        s.sendall(url.encode('utf-8'))
        bot.reply_to(message, "Moved to specified URL")
    except ConnectionResetError:
        bot.reply_to(message, "Failed to move to specified URL")

@bot.message_handler(commands=['get_title'])
def get_title(message):
    # Replace with your code to get the title of the current page
    bot.reply_to(message, "Title of current page: TITLE_HERE")

@bot.message_handler(commands=['stop'])
def stop_bot(message):
    # Stop the bot
    bot.stop_polling()
    bot.reply_to(message, "Bot stopped")

# Start the bot
bot.polling()

# Close the socket connection once the bot is stopped
s.close()
