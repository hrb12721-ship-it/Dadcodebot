import asyncio
import logging
import os
from threading import Thread
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

TG_BOT_TOKEN = "GAPGPTMASKTOKENkw383plmuubX0X"
ADMIN_USER_ID = 6196901789

bot_tg = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()

app = Flask(__name__)

@app.route('/')
def home():
    return "Dadcode Bot is Live!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("سلام مریم عزیز! 🌸\nربات دادکُد فعال است.")

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"پیام شما دریافت شد:\n{message.text}")

async def main():
    await bot_tg.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot_tg)

if __name__ == "__main__":
    web_thread = Thread(target=run_web)
    web_thread.daemon = True
    web_thread.start()
    
    asyncio.run(main())
