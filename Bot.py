import openai
import telebot
from config import BOT_TOKEN, OPENAI_API_KEY

# Inisialisasi bot Telegram
bot = telebot.TeleBot(BOT_TOKEN)

# Atur API Key OpenAI
openai.api_key = OPENAI_API_KEY

# Fungsi untuk mendapatkan respon dari OpenAI
def get_openai_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return response['choices'][0]['message']['content']

# Handler untuk setiap pesan yang masuk
@bot.message_handler(func=lambda message: True)
def chat_handler(message):
    response = get_openai_response(message.text)
    bot.reply_to(message, response)

# Menjalankan bot
print("Bot berjalan...")
bot.polling()
