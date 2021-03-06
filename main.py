import constants as keys
from telegram.ext import *
import responses as r


print("Bot started...")


def start_command(update, context):
    update.message.reply_text("Try something to get started!")

def help_command(update, context):
    update.message.reply_text("This is a Help Command")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")



def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()


main()
