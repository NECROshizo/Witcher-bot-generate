import asyncio
import sys
import logging
from logging.handlers import RotatingFileHandler

from aiogram import Bot, Dispatcher

from handlers import atack_router, location_router, start_router
from settings import setting


async def main() -> None:
    stream_handler = logging.StreamHandler(sys.stdout)
    file_handler = RotatingFileHandler("app_logger.log", maxBytes=500000, backupCount=5, encoding="utf-8")
    logging.basicConfig(level=logging.INFO,  handlers=[stream_handler, file_handler],)
    bot = Bot(token=setting.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(atack_router, location_router, start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
