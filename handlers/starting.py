from aiogram import Router, types
from aiogram.filters import CommandStart

from keybords import get_main_keybort

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer("Начнем играть!", reply_markup=get_main_keybort())
