from telegram.ext import Updater, MessageHandler, Filters
import openai
import os

# 🔑 Keys (Replit secrets me add karo)
openai.api_key = os.getenv("AIzaSyA6T-X4XmlbPwqvT8uZtmbhvGxHgJlaRZE")
TELEGRAM_BOT_TOKEN = os.getenv("8211165873:AAGx5ExYn-NxWxDEzzChEIEB3CfYUT0zmQc")

def reply(update, context):
    user_message = update.message.text
    
    try:
        # ChatGPT reply
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_message,
            max_tokens=150,
            temperature=0.7
        )
        bot_reply = response.choices[0].text.strip()
    except Exception as e:
        bot_reply = f"Error: {e}"

    update.message.reply_text(bot_reply)

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    print("🤖 Bot started...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()