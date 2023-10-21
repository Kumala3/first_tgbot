from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from tgbot.keyboards.goods import goods


def register_menu(dp: Dispatcher):
    @dp.message_handler(Command("menu"))
    async def show_menu(message: types.Message):
        await message.answer("Выберете товар:", reply_markup=goods)

    @dp.message_handler(text="🍔 Бургеры")
    async def get_burgers(message: types.Message):
        await message.answer("Бургеры")

    @dp.message_handler(Text(equals=["🍟 Картошка", "🥤 Напитки"]))
    async def get_drinks(message: types.Message):
        await message.answer(f"You have chosen: {message.text}", reply_markup=ReplyKeyboardRemove())
