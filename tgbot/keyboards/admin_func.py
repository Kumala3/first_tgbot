from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold

admin_funcs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Select_all_users", callback_data="select_all_users"),
            InlineKeyboardButton(text="UnBlock user", callback_data="unblock_user"),

        ]
    ]
)
