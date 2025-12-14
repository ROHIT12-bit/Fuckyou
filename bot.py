import os, importlib
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN=os.getenv("BOT_TOKEN")
BYPASS_DIR="bypass"

async def bypass(update:Update,context:ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("/bypass <link>")
        return
    link=context.args[0].lower()
    for f in os.listdir(BYPASS_DIR):
        if f.endswith(".py") and f!="__init__.py":
            m=importlib.import_module(f"{BYPASS_DIR}.{f[:-3]}")
            if m.match(link):
                await update.message.reply_text(m.bypass(link))
                return
    await update.message.reply_text("❌ Unsupported site")

app=ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("bypass",bypass))
app.run_polling()
