from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.types import Message

from tgbot.config import load_config
from tgbot.keyboards.send_file import send_file_keybord
from tgbot.keyboards.start_panel import keyboard_panel
from tgbot.keyboards.support import support_user
from tgbot.services.postreSQL import DataBase
from tgbot.texts.info_text import text_info
from tgbot.texts.my_profile import show_start_text
from tgbot.texts.send_file import file_send_rules_notifier
from tgbot.texts.user_text import user_info


def register_user(dp: Dispatcher):
    @dp.message_handler(commands=["start"])
    async def user_start(message: Message):
        db = DataBase()

        await db.create_pool()
        await db.create_table_users()
        await db.add_user(telegram_id=message.from_user.id,
                          username=message.from_user.username,
                          full_name=message.from_user.full_name,
                          lang_code=message.from_user.language_code,
                          is_premium=str(message.from_user.is_premium),
                          registered_time=str(message.date.replace())
                          )
        await message.answer(text=show_start_text(message.from_user.username), reply_markup=keyboard_panel)

    @dp.message_handler(text="My profile")
    async def cancel_sending_file(message: Message):
        user_id = message.from_user.id
        username = message.from_user.username
        await message.answer(text=user_info(user_id, username))

    @dp.message_handler(text="INFORMATION")
    async def info(message: Message):
        await message.answer(text=text_info, reply_markup=support_user)

    @dp.message_handler(text="Send file")
    async def send_file(message: Message):
        await message.answer(text=file_send_rules_notifier, reply_markup=send_file_keybord)

    @dp.message_handler(content_types=types.ContentType.DOCUMENT)
    async def get_file(message: Message):
        config = load_config()
        file_name = message.document.file_name
        if file_name.endswith(('.zip', '.rar')):
            await message.forward(config.tg_bot.channel_username)
            await message.reply(text="Ваш файл успешно отправлен! Ждите сообщения от Администратора!")
        else:
            await message.reply("Пожалуйста, отправьте файл в формате ZIP или RAR.")

    @dp.callback_query_handler(text="Cancel_send_file")
    async def cancel(call: CallbackQuery):
        await call.message.answer(text="Отправка файла отменена", reply_markup=keyboard_panel)
        await call.message.delete()
