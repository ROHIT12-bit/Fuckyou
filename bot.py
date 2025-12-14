import os
import importlib
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Absolute path fix (IMPORTANT)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BYPASS_DIR = os.path.join(BASE_DIR, "bypass")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Hello, 『𝚁𝚒𝚘 𝚂𝚑𝚒𝚗』 ᴰᴱⱽ!\n\n"
        "I'm your friendly URL bypasser bot. Just send me a link and "
        "I'll work my magic to get you the direct content. ✨\n\n"
        "🔗 I can handle a variety of link shorteners and websites.\n"
        "⚡️ My goal is to provide a fast and seamless experience.\n\n"
        "Ready to begin? Just send a URL my way!"
    )

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Bot update ⚙️", url="https://t.me/BOTSKINGDOMS")]]
    )

    await update.message.reply_text(text, reply_markup=keyboard)

# /bypass command
async def bypass(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Send a link.\n\nExample:\n/bypass https://example.com")
        return

    url = context.args[0].strip().lower()

    if not os.path.isdir(BYPASS_DIR):
        await update.message.reply_text("❌ Bypass folder missing.")
        return

    for file in os.listdir(BYPASS_DIR):
        if file.endswith(".py") and file != "__init__.py":
            module = importlib.import_module(f"bypass.{file[:-3]}")
            if hasattr(module, "match") and module.match(url):
                try:
                    result = module.bypass(url)
                    await update.message.reply_text(result)
                except Exception as e:
                    await update.message.reply_text(f"❌ Error:\n{e}")
                return

    await update.message.reply_text("❌ Unsupported site.")

# Run bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("bypass", bypass))
app.run_polling()
