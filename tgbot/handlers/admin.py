from aiogram import Dispatcher, types
from tgbot.filters.admin import AdminFilter


# async def admin_start(message: types.Message):
#     await message.answer("Hello Admin!")
#

# def register_admin(dp: Dispatcher):
#     admin = AdminFilter(is_admin=True)
#     dp.register_message_handler(admin_start, admin, commands=['start'])


def register_admin(dp: Dispatcher):
    @dp.message_handler(AdminFilter(is_admin=True), commands=['start'])
    async def admin_start(message: types.Message):
        await message.answer("Hello Admin!")
