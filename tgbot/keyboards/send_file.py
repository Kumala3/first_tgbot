from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

send_file_keybord = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Cancel", callback_data="Cancel_send_file"),
        ],

    ]
)
