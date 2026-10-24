import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

TOKEN = "8819887624:AAGXVwSYiFqZx3cbG7j1waDyZbhxrBN3FOs"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    inline_builder = InlineKeyboardBuilder()
    inline_builder.button(text="🔑 Normal Anahtarlar", callback_data="normal_keys")
    inline_builder.button(text="🏷️ İndirimli Anahtarlar", callback_data="discount_keys")
    inline_builder.button(text="⏳ Haftalık/2 Haftalık", callback_data="weekly_keys")
    inline_builder.adjust(2, 1)

    reply_builder = ReplyKeyboardBuilder()
    reply_builder.button(text="🛒 Mağaza")
    reply_builder.button(text="📢 Duyurular")
    reply_builder.button(text="💬 Destek")
    reply_builder.button(text="📖 Kurallar")
    reply_builder.button(text="📦 Siparişlerim")
    reply_builder.adjust(2, 2, 1)

    photo_url = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe"
    caption = "🎮 **ARDA STORE'a hoş geldin!**\nMenüden mağazaya veya siparişlerine ulaşabilirsin."

    await message.answer_photo(
        photo=photo_url,
        caption=caption,
        parse_mode="Markdown",
        reply_markup=inline_builder.as_markup()
    )
    
    await message.answer(
        "Aşağıdaki menüyü kullanabilirsiniz:",
        reply_markup=reply_builder.as_markup(resize_keyboard=True)
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

