import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Render ortam değişkeninden veya sistemden TOKEN'ı güvenli bir şekilde alıyoruz
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN ortam değişkeni bulunamadı! Lütfen Render panelinden TOKEN ekleyin.")

# Bot ve Dispatcher nesnelerini oluşturuyoruz
bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start komutu için handler
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "Hoş geldin! 🎮 TRmagic74_bot oyun mağazası botu başarıyla çalışıyor ve aktif!"
    )

# Botun ana çalıştırma fonksiyonu (Polling)
async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot başlatılıyor...")
    # Eski update'leri temizleyerek polling'i başlatıyoruz
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot durduruldu.")
