from telegram.ext import Application, MessageHandler, CommandHandler, filters
from config import TOKEN
from handlers import start, search

def main():
    app = Application.builder().token(TOKEN).build()

    # /start
    app.add_handler(CommandHandler("start", start))

    # search
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    print("🔥 Movie Search Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
