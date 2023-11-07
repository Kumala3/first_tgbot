from aiogram import Dispatcher
from tgbot.filters.admin import AdminFilter
# from tgbot.misc.throttling import rate_limit
from tgbot.misc.allow_access import allow_access
from tgbot.texts.admin_text import admin_text
from tgbot.keyboards.admin_func import admin_funcs
from tgbot.services.postreSQL import DataBase
from aiogram.types import CallbackQuery, Message
from aiogram.types import InputFile
import json


def register_admin(dp: Dispatcher):
    @allow_access(True)
    # @rate_limit(30, key="admin_start", num_messages=5)
    @dp.message_handler(AdminFilter(is_admin=True), commands=['start'])
    async def admin_start(message: Message):
        await message.answer(admin_text, reply_markup=admin_funcs)

    @dp.callback_query_handler(text="select_all_users")
    async def select_all_users(call: CallbackQuery):
        db = DataBase()
        await db.create_pool()
        all_users = await db.select_all_users()
        converted_users = [dict(record) for record in all_users]
        users_json = json.dumps(converted_users, ensure_ascii=False, indent=2)
        with open("users.json", "w", encoding="utf-8") as file:
            file.write(users_json)
        await call.message.answer_document(document=InputFile("users.json"), caption="Список пользователей")
