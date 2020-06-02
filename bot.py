from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    message = "Olá, " + update.message.from_user.first_name + "!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token   = '1162143286:AAFp6iw1Apc7aahFmQSKT80OosgFtU46pkg'
    updater = Updater(token=token, use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.start_polling()
    print(str('Olá, eu sou o Virtus' + updater))
    updater.idle()


if __name__ == "__main__":
    main()
