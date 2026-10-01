import asyncio
import logging
import os
from threading import Thread
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# --- تنظیمات لاگینگ ---
logging.basicConfig(level=logging.INFO)

# --- توکن‌های ربات ---
TG_BOT_TOKEN = "GAPGPTMASKTOKENzfcgrv6un8aX0X"
BALE_BOT_TOKEN = "GAPGPTMASKTOKENzfcgrv6un8aX1X"
ADMIN_USER_ID = 6196901789

# --- راه‌اندازی ربات و دیسپچر ---
bot_tg = Bot(token=GAPGPTMASKTOKENzfcgrv6un8aX2X
dp = Dispatcher()

# --- وب‌سرور Flask برای باز نگه‌داشتن پورت رندر ---
app = Flask(__name__)

@app.route('/')
def home():
    return "دادکُد با موفقیت فعال و آنلاین است!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- هندلرهای تلگرام (پاسخ به دستورات و پیام‌ها) ---
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    welcome_text = (
        "سلام مریم عزیز! 🌸\n\n"
        "به ربات **دادکُد** خوش آمدید.\n"
        "سیستم با موفقیت متصل و آماده پاسخگویی است."
    )
    await message.answer(welcome_text)

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"پیام شما در دادکُد دریافت شد:\n{message.text}")

# --- تابع اصلی اجرای ربات ---
async def main():
    print("...ربات دادکُد در حال شروع Polling است...")
    # حذف پیام‌های قبلی که در صف مانده بودند
    await bot_tg.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot_tg)

if __name__ == "__main__":
    # اجرای وب‌سرور در پس‌زمینه
    web_thread = Thread(target=run_web)
    web_thread.daemon = True
    web_thread.start()

    # اجرای حلقه اصلی ربات
    asyncio.run(main())

    
