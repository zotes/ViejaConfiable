import telebot



TOKEN = 'token'

tb = telebot.TeleBot(TOKEN)


updater=tb.get_updates();
@tb.message_handler(commands=['sp'])
def sp(message):
    photo = open('C:/path/vieja.png', 'rb')
    tb.send_photo(message.chat.id, photo)
tb.polling()
