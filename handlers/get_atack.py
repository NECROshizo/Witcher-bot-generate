from aiogram import F, Router
from aiogram.types import Message

from servises import ATACK, get_stiker

atack_router = Router()


@atack_router.message(F.text == "АТАКА")
async def atack(message: Message) -> None:
    await message.answer_sticker(get_stiker(ATACK))
