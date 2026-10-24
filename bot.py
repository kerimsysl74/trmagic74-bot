import asyncio
import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Render ortam değişkeninden TOKEN'ı alıyoruz
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN ortam değişkeni bulunamadı! Lütfen Render panelinden TOKEN ekleyin.")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Hoş geldin! 🎮 TRmagic74_bot oyun mağazası botu aktif!")

# Render'ın port bulma şartını karşılamak için mini web sunucusu
async def handle(request):
    return web.Response(text="Bot is running!")

async def web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    # Render'ın atadığı portu yakalıyoruz (varsayılan 10000)
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Web sunucusu {port} portunda başlatıldı.")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot başlatılıyor...")
    
    # Web sunucusunu ve bot polling'i aynı anda (arkada) başlatıyoruz
    await web_server()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot durduruldu.")
