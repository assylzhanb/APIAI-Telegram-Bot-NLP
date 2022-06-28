from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
TOKEN = '1063164614:AAHWIx1Pb1P4VZYeHZHsxRqJYmpJ-AexHIU'
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher


def hello_func(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def text_messaje(update, context):
    request = apiai.ApiAI('c9b37202de784dc9b3f63489ffb5204d').text_request()
    request.lang = 'ru'
    request.session_id = 'BatlabAIBot'

    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        context.bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text='Простите но я вас не понял')

start_command_handler = CommandHandler('start', hello_func)
text_message_handler = MessageHandler(Filters.text, text_messaje)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()
