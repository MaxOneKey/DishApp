import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Завантажуємо токен
load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

WEB_APP_URL = "https://nonlucratively-nonunderstandable-mignon.ngrok-free.dev" 

@dp.message(CommandStart())
async def start(message: types.Message):
    # Створюємо кнопку, яка відкриває Mini App
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🍳 Відкрити Кухню", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    await message.answer("Привіт! Натисни кнопку, щоб відкрити додаток:", reply_markup=keyboard)

async def main():
    print("Бот запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())