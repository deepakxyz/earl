from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import myMod

def start(update, context):
    update.message.reply_text("Wow")


def help(update, context):
    update.message.reply_text("Help")

def handle_text(update, context):
    if update.message.text == "deepak":
        update.message.reply_text("Aisho")
        print("this is hello")
    
    elif update.message.text == "aisho":
        myMod.startLog(update.message.text)

    else:
        update.message.reply_text("yest")


def main():
    updater = Updater("898532906:AAEUMnF02HK84H9jopjeHpZ_xgHXVhQLtHg", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))


    dp.add_handler(MessageHandler(Filters.text, handle_text))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()

    # 1219075758:AAG0cx63kewvLXGXygb56BYRwAXSOLECT7Y