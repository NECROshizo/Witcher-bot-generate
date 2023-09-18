from random import choices

from .game_token import LocationToken


def get_stiker(token_set: list[LocationToken]) -> str:
    return getattr(choices(token_set)[0], "sticker_id")
