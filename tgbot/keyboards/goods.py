from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

goods = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍔 Бургеры"),
        ],
        [
            KeyboardButton(text="🍟 Картошка"),
            KeyboardButton(text="🥤 Напитки"),
        ]
    ],
    resize_keyboard=True
)
