import os
import asyncio
import logging
from threading import Thread
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

TG_BOT_TOKEN = "GAPGPTMASKTOKEN162bfgg7jemX0X"
ADMIN_USER_ID = 6196901789

# ساخت کلاینت ربات
bot = Bot(token=GAPGPTMASKTOKEN162bfgg7jemX1X
dp = Dispatcher()

# تعریف وب‌سرور برای زنده نگه‌داشتن روی رندر
app = Flask(__name__)

@app.route("/")
def index():
    return "Dadcode is live!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, use_reloader=False)

# هندلر دستور استارت
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("سلام حسن عزیز! 🌸\nربات دادکُد فعال است و پیام شما دریافت شد.")

# هندلر تمام پیام‌های متنی
@dp.message()
async def all_messages_handler(message: types.Message):
    await message.reply(f"پیام شما دریافت شد:\n{message.text}")

async def run_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # اجرای وب‌سرور در پس‌زمینه
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # اجرای ربات اصلی
    asyncio.run(run_bot())
