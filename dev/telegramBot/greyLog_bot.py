from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import fileExe

# start bot function
context_v = "Grey Bot is online"
def start(update, context):
    update.message.reply_text("Grey Bot is online")

# help command string
helpstr = '''/start - check weather the bot is online.
/help - get all the existing commands.

'''
def help(update, context):
    update.message.reply_text(helpstr)


#windows command
def sysCmd(update, context):
    textInput = update.message.text
    if textInput.startswith("open."):
        cmd = textInput.split('.')
        if cmd[1] == "maya":
            fileExe.sFMaya(cmd[0])

    else:
        "Invalid Command"
    
    if textInput.startswith("close."):
        cmd = textInput.split('.')
        if cmd[1] == "maya":
            fileExe.sFMaya(cmd[0])
            


# main function
def main():
    updater = Updater ("1219075758:AAG0cx63kewvLXGXygb56BYRwAXSOLECT7Y", use_context= True)

    dp = updater.dispatcher

    #command handler
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    #message handler
    dp.add_handler(MessageHandler(Filters.text, sysCmd))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
