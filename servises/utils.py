from random import choices

from .game_tokens import Token


def get_stiker(token_set: list[Token]) -> str:
    return getattr(choices(token_set)[0], "sticker_id")
