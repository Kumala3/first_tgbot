from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from tgbot.keyboards.callbacks_data import buy_callback

goods_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buy account: 100 lvl",
                                 callback_data=buy_callback.new(item_name="6.2cc", quantity=1)),
            InlineKeyboardButton(text="Buy account: 89 lvl", callback_data="buy:3.65cc:89"),
            InlineKeyboardButton(text="Boo", url="https://www.youtube.com/@MrBeast"),
            InlineKeyboardButton(text="MrBeast Channel", url="https://www.youtube.com/channel/UCkUaqajjf0OMKpAE_XYdpuw")
        ],
        [
            InlineKeyboardButton(text="cancel", callback_data="cancel")
        ]
    ],
    resize_keyboard=True
)

good = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="100 niger", url="https://www.youtube.com/@MrBefds"),
        ]
    ],
    resize_keyboard=True
)
