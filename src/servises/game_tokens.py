from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    name_token: str
    number_token: int
    sticker_id: str


WATER_LOCATION = (
    Token(
        "Каэр Сирен",
        1,
        "CAACAgIAAxkBAAEKVIJlCIxuD2jn6BSbBbgfOvjBE_uN3wACJz0AApkkMEg4gPju8Dv0NDAE",
    ),
    Token(
        "Бан Ард",
        4,
        "CAACAgIAAxkBAAEKVJdlCJc0rDWCVYAqV5jitO0BlxCLnwACZTsAAqJaMUgkpXO71gwDGTAE",
    ),
    Token(
        "Цидарис",
        5,
        "CAACAgIAAxkBAAEKVJllCJev7_hemSvDnAUNXbIPdd-6VAACFDUAAuGKMEi9s5FxRgQigzAE",
    ),
    Token(
        "Гленмор",
        12,
        "CAACAgIAAxkBAAEKVKNlCJfSXHmoWoUa0jB_AtRqyy8TLgAC2TUAAmLkMEiqDetno1hAIzAE",
    ),
    Token(
        "Лок Ихор",
        14,
        "CAACAgIAAxkBAAEKVKllCJf1FziAZCyU1SmJ_Am7hpZqKgACpjIAAvPOOEgVMOxsQ8pbnDAE",
    ),
    Token(
        "Гортур Гвазд",
        15,
        "CAACAgIAAxkBAAEKVK9lCJgN0e-wmMvHkFdmzAsNAkwAAWQAAtw2AAItMzhIcgkT_ak3BZ0wBA",
    ),
)


MOUNTAIN_LOCATION = (
    Token(
        "Хенгфорс",
        2,
        "CAACAgIAAxkBAAEKVQRlCKEYw_iX_IcTtr5RDpktwASp3AAC8z4AAuvdMEh-_5aEECNe8jAE",
    ),
    Token(
        "Каэр Морхен",
        3,
        "CAACAgIAAxkBAAEKVQZlCKE2FLg0e_hWhM_pRmAgh6GAOAACyTcAAsBJMUhpqXfWJaeLgTAE",
    ),
    Token(
        "Цинтра",
        9,
        "CAACAgIAAxkBAAEKVQhlCKFPyKTCDlZzUGuODL5J9Kq37gACajcAAoloMEioc43fMDp9hTAE",
    ),
    Token(
        "Боклер",
        11,
        "CAACAgIAAxkBAAEKVQplCKFsDKRBwtix9PT7bKLBY8050wACsTkAAuJ7MUgks1LK7GtD0TAE",
    ),
    Token(
        "Долтес",
        13,
        "CAACAgIAAxkBAAEKVQxlCKF-yqBB08AS_qBBMs5iNIhvGAACZzoAAhPwMUhPVUhOvd-iXTAE",
    ),
    Token(
        "Ард Модрон",
        18,
        "CAACAgIAAxkBAAEKVQ5lCKGcUI5omIGEqXOGlj91wW9VLgACWzUAAvmNMEhJX2Z7unq9rTAE",
    ),
)


FOREST_LOCATION = (
    Token(
        "Новиград",
        6,
        "CAACAgIAAxkBAAEKVRBlCKOh_kYXoQQm3n7FUIBL1lpGUwAC7jgAAgGUMUg28VZ-dzv01zAE",
    ),
    Token(
        "Вызима",
        7,
        "CAACAgIAAxkBAAEKVRJlCKO_1vIxMrtTFdbpew1Ot82FCwACWTsAAih2MUj2dHe8U4nUrDAE",
    ),
    Token(
        "Венгербург",
        8,
        "CAACAgIAAxkBAAEKVRhlCKPRBUyJjXfQEfzO2U0WYkGUzwACzDgAArH7MUjsvA7JJwrIYzAE",
    ),
    Token(
        "Хфзрн Кадух",
        10,
        "CAACAgIAAxkBAAEKVRxlCKQMyzBZcfFbSHbR3VPV20LqgAAC4DYAAsB5MEhVYKz-DMwrqzAE",
    ),
    Token(
        "Дувод",
        16,
        "CAACAgIAAxkBAAEKVSBlCKQtjTUVqpyaExCPBJmaaNkMawAC8zAAAphmMEhHoiB5kR5mEjAE",
    ),
    Token(
        "Ард Модрон",
        17,
        "CAACAgIAAxkBAAEKVSJlCKRBcOtWPYG-Hc7yHuQoadn1SAACuDsAAj77MUitJVyCe-mFgDAE",
    ),
)


ATACK = (
    Token(
        "Укус",
        0,
        "CAACAgIAAxkBAAEKVnBlCdlImz2lJgdQoPQc97FqwM_7ZgAC1DwAArYnUUgdToxamFvQ-zAE",
    ),
    Token(
        "Удар",
        0,
        "CAACAgIAAxkBAAEKVnJlCdlK8B15-A6Z9ebCoU5PJQABanwAAvI2AAIPPlFIgDLZyfwWwl8wBA",
    ),
)
