from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from tgbot.models.first_mode import User
from tgbot.misc.allow_access import allow_access


def register_acl_test(dp: Dispatcher):
    @allow_access(True)
    @dp.message_handler(Command("block_me"))
    async def block_me(message: types.Message, user: User):
        await message.answer(f"Пользователь имеет статус: {user.allowed}. Теперь доступ запрещен\n"
                             f"Чтобы разблокироваться введите команду /unblock_me")
        user.block()

    @allow_access(True)
    @dp.message_handler(Command("unblock_me"))
    async def unblock_me(message: types.Message, user: User):
        await message.answer(f"Пользователь имеет статус: {user.allowed}. Теперь доступ разрешен\n"
                             f"Чтобы заблокироваться введите команду /block_me")
        user.unblock_me()
