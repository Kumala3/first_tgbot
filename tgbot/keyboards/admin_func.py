from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold

admin_funcs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Block user", callback_data="block_user"),
            InlineKeyboardButton(text="UnBlock user", callback_data="unblock_user"),

        ]
    ]
)
