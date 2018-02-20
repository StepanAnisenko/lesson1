from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format="%(name)s-%(levelname)s-%(message)s",
	level=logging.INFO,
	filename="bot.log"
	)
def main():
	updater = Updater("520311378:AAHcP37BRYxQ24lmqmmx4kZQ0w5iwRU5Mwk")
	dp=updater.dispatcher
	dp.add_handler(CommandHandler("start",greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))
	updater.start_polling()
	updater.idle()
	
def greet_user(bot,update):
	text="хэй бро"
	print(text)
	update.message.reply_text(text)
	print(update)
def talk_to_me(bot, update):
	user_text=update.message.text
	print(user_text)
	update.message.reply_text(user_text)
main()