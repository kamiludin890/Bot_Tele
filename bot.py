from telegram import Update
from dotenv import load_dotenv
import os
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

load_dotenv()

TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Saya bot Telegram."
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if update.message.reply_to_message:
        replied_text = update.message.reply_to_message.text

        await update.message.reply_text(
            f"{replied_text} Status {text}"
        )
    else:
        await update.message.reply_text(
            f"Ini jawaban : {text}"
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, echo))

print("Bot berjalan...")
app.run_polling()