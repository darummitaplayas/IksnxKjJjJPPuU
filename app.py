import telebot
from telebot import types

# Conexión con nuestro BOT
TOKEN = '7523701728:AAE85RREULwBMBZHLD0vwiWGckaETFt7_ZM'
bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    # Botones principales
    btn_youtube = types.KeyboardButton('📹 YouTube')
    btn_descargas = types.KeyboardButton('📥 Descargas')
    btn_apps = types.KeyboardButton('📱 Top 5 Apps')
    
    markup.add(btn_youtube, btn_descargas, btn_apps)
    bot.send_message(message.chat.id, '¡Bienvenido! Elige una categoría:', reply_markup=markup)

# Manejo del botón de YouTube
@bot.message_handler(func=lambda message: message.text == '📹 YouTube')
def send_youtube_links(message):
    markup = types.InlineKeyboardMarkup()
    
    # Enlaces a videos de YouTube
    video1 = types.InlineKeyboardButton('OMM REBIRTH', url='https://youtu.be/9-f8dFPkqjw')
    video2 = types.InlineKeyboardButton('COOPDX ONLINE', url='https://youtu.be/BNsbLSQZ6Ik')
    video3 = types.InlineKeyboardButton('EXCOOP ANDROID', url='https://youtu.be/WHoekKbzje4')
    video4 = types.InlineKeyboardButton('MARIO ODYSSEY', url='https://youtu.be/OiB3FrA0tYg')
    video5 = types.InlineKeyboardButton('LUIGI ODYSSEY', url='https://youtu.be/k5EGZrfopFY')
    
    markup.add(video1, video2, video3, video4, video5)
    bot.send_message(message.chat.id, 'Aquí tienes una lista de videos recomendados:', reply_markup=markup)

# Manejo del botón de Descargas
@bot.message_handler(func=lambda message: message.text == '📥 Descargas')
def send_download_links(message):
    markup = types.InlineKeyboardMarkup()
    
    # Enlaces de descarga
    download1 = types.InlineKeyboardButton('WONDER ANDROID', url='https://github.com/Manzft27/SMBW-Fangame/releases/download/v0.7-alpha/SMBW-Fangame-v0.7-alpha-android.apk')
    download2 = types.InlineKeyboardButton('Descarga 2', url='https://github.com/Manzft27/SMBW-Fangame/releases/download/v0.7-alpha/SMBW-Fangame-v0.7-alpha-android.apk')
    download3 = types.InlineKeyboardButton('Descarga 3', url='https://github.com/Manzft27/SMBW-Fangame/releases/download/v0.7-alpha/SMBW-Fangame-v0.7-alpha-android.apk')
    download4 = types.InlineKeyboardButton('Descarga 4', url='https://github.com/Manzft27/SMBW-Fangame/releases/download/v0.7-alpha/SMBW-Fangame-v0.7-alpha-android.apk')
    download5 = types.InlineKeyboardButton('Descarga 5', url='https://github.com/Manzft27/SMBW-Fangame/releases/download/v0.7-alpha/SMBW-Fangame-v0.7-alpha-android.apk')
    
    markup.add(download1, download2, download3, download4, download5)
    bot.send_message(message.chat.id, 'Aquí tienes una lista de descargas disponibles:', reply_markup=markup)

# Manejo del botón de Top 5 Apps
@bot.message_handler(func=lambda message: message.text == '📱 Top 5 Apps')
def send_apps_links(message):
    markup = types.InlineKeyboardMarkup()
    
    # Enlaces a aplicaciones
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
