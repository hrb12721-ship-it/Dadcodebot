import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# --- تنظیمات اختصاصی دادکُد ---
# این بخش را با اطلاعات خودت پر کن
TG_BOT_TOKEN = "8933088010:AAFARHEe3dHoXHZScbQXOMRuvX8B4CPEVBQ"
BALE_BOT_TOKEN = "162149318:Io3oxPfSkXPIhOiyGj_WiJiXqMa5L2ODmxc"
ADMIN_USER_ID =  6196901789
# --- راه‌اندازی ربات‌ها ---
bot_tg = Bot(token=TG_BOT_TOKEN)
bot_bale = Bot(token=BALE_BOT_TOKEN)
dp = Dispatcher()

async def main():
    print("دادکُد در حال اجراست...")
    # در اینجا منطق پایش سایت‌ها و سایر دستورات قرار می‌گیرد
    # ربات شروع به گوش دادن به پیام‌ها می‌کند
    await dp.start_polling(bot_tg)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
