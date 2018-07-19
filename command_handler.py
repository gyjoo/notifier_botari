from telegram.ext import Updater, MessageHandler, Filters, CommandHandler  # import modules
import id, notifier

print('start telegram chat bot')


# message reply function
def get_message(bot, update) :
    update.message.reply_text("/check : 빗썸 html 전문 확인")
#    update.message.reply_text(update.message.text)


# help reply function
def check_command(bot, update) :
    update.message.reply_text(notifier.get_html_body())
    print('msg sent')


updater = Updater(id.my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

check_handler = CommandHandler('check', check_command)
updater.dispatcher.add_handler(check_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()
