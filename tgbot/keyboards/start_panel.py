from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="My profile"),
            KeyboardButton(text="Promocode"),
            KeyboardButton(text="INFORMATION")
        ]
    ],
    resize_keyboard=True
)
