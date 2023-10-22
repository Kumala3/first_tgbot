from aiogram import Dispatcher, types
from tgbot.filters.admin import AdminFilter
from tgbot.misc.throttling import rate_limit
from tgbot.misc.allow_access import allow_access
from tgbot.texts.admin_text import admin_text
from tgbot.keyboards.admin_func import admin_funcs


def register_admin(dp: Dispatcher):
    @allow_access(True)
    @rate_limit(30, key="admin_start", num_messages=5)
    @dp.message_handler(AdminFilter(is_admin=True), commands=['start'])
    async def admin_start(message: types.Message):
        await message.answer(admin_text, reply_markup=admin_funcs)
