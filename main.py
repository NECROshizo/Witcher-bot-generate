import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import start_router
from settings import setting


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=setting.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
