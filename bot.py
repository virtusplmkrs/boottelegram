from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

STATE1 = 1
STATE2 = 2

def welcome(update, context):
    message = "Olá, " + update.message.from_user.first_name + "!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def especialidade(update, context):
    message = '''Por favor, que informação você deseja? \n
            1 - Automação \n
            2 - Programação'''
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
    return STATE1

def inputEspecialidade(update, context):
    try:
        especialidade = (update.message.text).lower()
        print(especialidade)
        if (especialidade == '1' 
                or especialidade == 'automação'
                or especialidade == 'arduino'
                or especialidade == 'raspbarry'):
            message = '''Modelo: https://youtu.be/njq1_fANhzY \n
                        Mod. 01: https://youtu.be/ju8-27eRHXM'''
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return STATE2
        elif (especialidade == '2'
                or especialidade == 'programação'
                or especialidade == 'python'
                or especialidade == 'php'):
            message = '''Python: https://youtu.be/3Uzbn2UoPjs \n
                        PHP: https://youtu.be/ju8-27eRHXM'''
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return STATE2
    except Exception as e:
        print(str(e))


def inputAssunto(update, context):
    message = "Muito obrigada em breve teremos novos temas!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def cancel(update, context):
    return ConversationHandler.END

def main():
    token   = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    updater = Updater(token=token, use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('especialidade', especialidade)],
        states={
            STATE1: [MessageHandler(Filters.text, inputEspecialidade)],
            STATE2: [MessageHandler(Filters.text, inputAssunto)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)
    
    updater.start_polling()
    print('Olá, eu sou o Virtus' + str(updater))
    updater.idle()


if __name__ == "__main__":
    main()
