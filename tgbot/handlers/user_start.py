from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

from tgbot.texts.my_profile import show_start_text
from tgbot.texts.info_text import text_info
from tgbot.texts.user_text import user_info

from tgbot.keyboards.send_file import keyboard
from tgbot.keyboards.start_panel import keyboard_panel
from tgbot.keyboards.support import support_user

def register_user(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def user_start(message: Message):
        username = message.from_user.username
        await message.answer(text=show_start_text(username), reply_markup=keyboard_panel)

    @dp.message_handler(text="My profile")
    async def cancel_sending_file(message: Message):
        user_id = message.from_user.id
        username = message.from_user.username
        await message.answer(text=user_info(user_id, username))

    @dp.message_handler(text="INFORMATION")
    async def info(message: Message):
        await message.answer(text=text_info, reply_markup=support_user)
