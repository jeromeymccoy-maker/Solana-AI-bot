import telebot
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN not set")

TARGET_TOKEN = "Duj5mm4pyY6E4RXGpN4oVGtvVns5AzBYGknxTVYnpump"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "🚀 Solana AI Bot Active\nMode: Semi-Auto\n\nCommands:\n/price\n/status\n/analyze"
    )


@bot.message_handler(commands=["status"])
def status(msg):
    bot.send_message(msg.chat.id, "✅ Bot running")


@bot.message_handler(commands=["price"])
def price(msg):
    try:
        url = f"https://api.dexscreener.com/latest/dex/tokens/{TARGET_TOKEN}"
        r = requests.get(url).json()
        price = r["pairs"][0]["priceUsd"]

        bot.send_message(msg.chat.id, f"💰 Price: ${price}")
    except Exception as e:
        bot.send_message(msg.chat.id, "⚠️ Price unavailable")


@bot.message_handler(commands=["analyze"])
def analyze(msg):
    bot.send_message(
        msg.chat.id,
        "📊 Trend: Neutral\nRisk: Medium\nWait for volume."
    )


print("Bot started...")
bot.infinity_polling()
