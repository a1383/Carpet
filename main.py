
import os
from telegram import Update, Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from collections import defaultdict

BOT_TOKEN = os.getenv("BOT_TOKEN")
user_requests = defaultdict(int)
FREE_LIMIT = 2

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "سلام! به Carpetia خوش آمدید. متن یا تصویر فرش خود را ارسال کنید تا طرح پیشنهادی دریافت کنید."
    )

def handle_text(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_requests[user_id] >= FREE_LIMIT:
        update.message.reply_text("شما از حد رایگان خود استفاده کرده‌اید. لطفاً اشتراک تهیه کنید.")
        return
    user_requests[user_id] += 1
    update.message.reply_text("در حال ساخت طرح فرش برای توصیف شما... (این فقط نمونه است)")

def handle_photo(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_requests[user_id] >= FREE_LIMIT:
        update.message.reply_text("شما از حد رایگان خود استفاده کرده‌اید. لطفاً اشتراک تهیه کنید.")
        return
    user_requests[user_id] += 1
    update.message.reply_text("در حال آنالیز تصویر و ساخت طرح مشابه... (این فقط نمونه است)")

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
