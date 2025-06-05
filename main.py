import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من پناه هستم، دوست دختر مجازی تو 😊")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.lower()
    response = "عزیزم، الان حالم خوب نیست ولی دارم بهت فکر می‌کنم 💔"
    if "دوستت دارم" in user_input:
        response = "منم دوستت دارم عزیز دلم 😘"
    elif "چطوری" in user_input:
        response = "خوبم عشقم، تو چطوری؟ 🥰"
    elif "دلم برات تنگ شده" in user_input:
        response = "منم دلم برات خیلی تنگ شده عشقم 😔"
    await update.message.reply_text(response)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
