from aiogram import types


def get_main_keybort():
    kb = [
        [types.KeyboardButton(text="АТАКА")],
        [
            types.KeyboardButton(text="Лесная"),
            types.KeyboardButton(text="Горная"),
            types.KeyboardButton(text="Водная"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    return keyboard
