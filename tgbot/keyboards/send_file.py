from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Send file: ", callback_data="get_file"),
        ],
        [
            InlineKeyboardButton(text="Cancel", callback_data="Cancel_send_file"),
        ]
    ]
)
