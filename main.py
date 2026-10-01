import os
import asyncio
import logging
from threading import Thread
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

# توکن ربات دادکد نیوز
BOT_TOKEN = "GAPGPTMASKTOKENmlzcesobawkX0X"

bot = Bot(token=GAPGPTMASKTOKENmlzcesobawkX1X
dp = Dispatcher()
app = Flask(__name__)

@app.route("/")
def index():
    return "Dadcode News Bot is Live!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, use_reloader=False)

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("سلام مریم عزیز! 🌸\nربات دادکُد نیوز (@Dadcode_News_bot) با موفقیت فعال شد و آنلاین است.")

@dp.message()
async def echo_handler(message: types.Message):
    await message.reply(f"پیام شما در دادکُد دریافت شد:\n\n{message.text}")

async def main():
    # حذف وبهوک‌های قبلی و شروع به خواندن پیام‌ها
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    asyncio.run(main())
