import asyncio
import logging

from aiogram import Bot, Dispatcher, types

from settings import setting

logging.basicConfig(level=logging.INFO)
bot = Bot(token=setting.bot_token.get_secret_value(), parse_mode="HTML")
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())