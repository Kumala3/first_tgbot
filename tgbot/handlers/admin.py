from aiogram import Dispatcher, types
from tgbot.filters.admin import AdminFilter


async def admin_start(message: types.Message):
    await message.answer("Hello Admin!")


def register_admin(dp: Dispatcher):
    admin = AdminFilter(is_admin=True)
    dp.register_message_handler(admin_start, admin, commands=['start'])
