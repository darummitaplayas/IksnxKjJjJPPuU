import telebot
from telebot import types

# Conexión con nuestro BOT
TOKEN = '7523701728:AAE85RREULwBMBZHLD0vwiWGckaETFt7_ZM'
bot = telebot.TeleBot(TOKEN)

# Comando /retiredbot
@bot.message_handler(commands=['retiredbot'])
def send_welcome(message):
    # Botones principales en un mensaje en línea
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn_youtube = types.InlineKeyboardButton('🎥 YouTube', callback_data='youtube')
    btn_descargas = types.InlineKeyboardButton('📥 Descargas', callback_data='descargas')
    btn_apps = types.InlineKeyboardButton('📱 Top 5 Apps', callback_data='apps')
    
    markup.add(btn_youtube, btn_descargas, btn_apps)
    bot.send_message(message.chat.id, '¡Bienvenido! Elige una categoría:', reply_markup=markup)

# Manejo de los botones en línea
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'youtube':
        send_youtube_links(call.message)
    elif call.data == 'descargas':
        send_download_links(call.message)
    elif call.data == 'apps':
        send_apps_links(call.message)

# Función para enviar enlaces de YouTube
def send_youtube_links(message):
    markup = types.InlineKeyboardMarkup()
    
    video1 = types.InlineKeyboardButton('OMM REBIRTH', url='https://youtu.be/9-f8dFPkqjw')
    video2 = types.InlineKeyboardButton('COOPDX ONLINE', url='https://youtu.be/BNsbLSQZ6Ik')
    video3 = types.InlineKeyboardButton('EXCOOP ANDROID', url='https://youtu.be/WHoekKbzje4')
    video4 = types.InlineKeyboardButton('MARIO ODYSSEY', url='https://youtu.be/OiB3FrA0tYg')
    video5 = types.InlineKeyboardButton('LUIGI ODYSSEY', url='https://youtu.be/k5EGZrfopFY')
    
    markup.add(video1, video2, video3, video4, video5)
    bot.send_message(message.chat.id, 'Aquí tienes una lista de videos recomendados:', reply_markup=markup)

# Función para enviar enlaces de descarga
def send_download_links(message):
    markup = types.InlineKeyboardMarkup()
    
    download1 = types.InlineKeyboardButton('WONDER ANDROID', url='https://github.com/Manzft27/SMBW-Fangame/releases/download/v0.7-alpha/SMBW-Fangame-v0.7-alpha-android.apk')
    download2 = types.InlineKeyboardButton('Descarga 2', url='https://github.com/Manzft27/SMBW-Fangame/releases/download/v0.7-alpha/SMBW-Fangame-v0.7-alpha-android.apk')
    download3 = types.InlineKeyboardButton('Descarga 3', url='https://github.com/Manzft27/SMBW-Fangame/releases/download/v0.7-alpha/SMBW-Fangame-v0.7-alpha-android.apk')
    download4 = types.InlineKeyboardButton('Descarga 4', url='https://github.com/Manzft27/SMBW-Fangame/releases/download/v0.7-alpha/SMBW-Fangame-v0.7-alpha-android.apk')
    download5 = types.InlineKeyboardButton('Descarga 5', url='https://github.com/Manzft27/SMBW-Fangame/releases/download/v0.7-alpha/SMBW-Fangame-v0.7-alpha-android.apk')
    
    markup.add(download1, download2, download3, download4, download5)
    bot.send_message(message.chat.id, 'Aquí tienes una lista de descargas disponibles:', reply_markup=markup)

# Función para enviar enlaces de aplicaciones
def send_apps_links(message):
    markup = types.InlineKeyboardMarkup()
    
    app1 = types.InlineKeyboardButton('App 1', url='https://play.google.com/store/apps/details?id=com.discord')
    app2 = types.InlineKeyboardButton('App 2', url='https://play.google.com/store/apps/details?id=com.discord')
    app3 = types.InlineKeyboardButton('App 3', url='https://play.google.com/store/apps/details?id=com.discord')
    app4 = types.InlineKeyboardButton('App 4', url='https://play.google.com/store/apps/details?id=com.discord')
    app5 = types.InlineKeyboardButton('App 5', url='https://play.google.com/store/apps/details?id=com.discord')
    
    markup.add(app1, app2, app3, app4, app5)
    bot.send_message(message.chat.id, 'Aquí tienes una lista de las mejores apps recomendadas:', reply_markup=markup)

# Iniciar el bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
