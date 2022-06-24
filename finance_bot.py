import my_data as DATA
import telebot
import request

#create bot
bot = telebot.TeleBot(DATA.API_KEY)

#request command: "/start"
request.command_start(bot)

#sort text
request.command_sorter(bot)

#while start bot
bot.polling(non_stop=True,interval=0)