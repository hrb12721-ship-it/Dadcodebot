import asyncio
import logging
import os
from threading import Thread
from flask import Flask
from aiogram import Bot, Dispatcher, types

# --- تنظیمات اختصاصی دادکُد ---
TG_BOT_TOKEN = "8933088010:AAFARHEE3doHXHZScbQ"
BALE_BOT_TOKEN = "162149318:Io3oxPfSkXPIhOiyGj"
ADMIN_USER_ID = 6196901789

# --- راه اندازی ربات‌ها ---
bot_tg = Bot(token=TG_BOT_TOKEN)
bot_bale = Bot(token=BALE_BOT_TOKEN)
dp = Dispatcher()

# --- ایجاد وب‌سرور برای حل مشکل پورت در Render ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Dadcode Bot is running successfully!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

async def main():
    print("...دادکُد در حال اجراست...")
    await dp.start_polling(bot_tg)

if __name__ == "__main__":
    # اجرای وب‌سرور در پس‌زمینه برای راضی نگه داشتن رندر
    Thread(target=run_web).run = lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
    web_thread = Thread(target=run_web)
    web_thread.daemon = True
    web_thread.start()

    # اجرای ربات
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    
