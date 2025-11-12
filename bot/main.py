# skeleton only, no concrete downloaders
import os, asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

bot = Bot(os.getenv('TELEGRAM_BOT_TOKEN',''))
dp = Dispatcher()

@dp.message(F.text.lower().startswith('/start'))
async def start(m: Message):
    await m.answer('Пришли поддерживаемую ссылку. Бот скачает файл только из разрешённых источников.')

@dp.message()
async def handle(m: Message):
    await m.answer('Источник пока не поддержан. Добавьте провайдер согласно README.')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
