from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_keybort() -> ReplyKeyboardMarkup:
    botton = [
        [KeyboardButton(text="АТАКА")],
        [
            KeyboardButton(text="Лесная"),
            KeyboardButton(text="Горная"),
            KeyboardButton(text="Водная"),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=botton,
    )
