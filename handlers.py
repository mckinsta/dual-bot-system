from telegram import Update
from telegram.ext import ContextTypes
from db import save_movie, get_movie
from config import ADMIN_ID

pending = {}

# 🎥 STEP 1: receive video
async def receive_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    file = update.message.video or update.message.document

    if not file:
        return

    pending[update.effective_user.id] = file.file_id

    await update.message.reply_text("📥 Video received!\nNow send movie id")

# 📝 STEP 2: save movie_id
async def receive_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id != ADMIN_ID or user_id not in pending:
        return

    movie_id = update.message.text.strip()
    file_id = pending.pop(user_id)

    save_movie(movie_id, file_id)

    await update.message.reply_text(f"✅ Saved: {movie_id}")

# 🚀 SEND MOVIE (/start)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if args:
        movie_id = args[0]

        data = get_movie(movie_id)

        if data:
            await update.message.reply_video(data[0])
        else:
            await update.message.reply_text("❌ Not found")

    else:
        await update.message.reply_text("👋 Welcome bhau")
