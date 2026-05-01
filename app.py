import telebot
import os
from flask import Flask
import threading

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is working!")

@bot.message_handler(func=lambda m: True)
def handle(message):
    bot.reply_to(message, message.text.upper())

# Flask app for Render
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
