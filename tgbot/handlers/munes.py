import logging

from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery

from tgbot.keyboards.callbacks_data import buy_callback
from tgbot.keyboards.goods_2 import goods_2, good


def register_menus(dp: Dispatcher):
    @dp.message_handler(Command("show_goods"))
    async def show_goods_2(message: Message):
        await message.answer(text="Goods: ", reply_markup=goods_2)

    @dp.callback_query_handler(buy_callback.filter(item_name="6.2cc"))
    async def buy_account(call: CallbackQuery, callback_data: dict):
        await call.answer(cache_time=60)
        logging.info(f"callback_data = {call.data}")
        logging.info(f"callback_data dict = {callback_data}")
        await call.message.answer(f"You bought for {callback_data.get('quantity')}", reply_markup=good)

    @dp.callback_query_handler(text="cancel")
    async def cancel_buying(call: CallbackQuery):
        await call.answer("You canceled this purchase", show_alert=True)
        await call.message.edit_reply_markup()
