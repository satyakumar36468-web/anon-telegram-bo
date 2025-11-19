from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 👋 Your bot is working.")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to check bot working.")

# --- Put your new BotFather token below ---
BOT_TOKEN = "8316305335:AAHStS2NUl5cvj28-9C6z4HePQ-A5Cs3uq4"
# ------------------------------------------

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))

app.run_polling()