from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="My profile"),
            KeyboardButton(text="INFORMATION"),
            KeyboardButton(text="Send file")
        ]
    ],
    resize_keyboard=True
)
