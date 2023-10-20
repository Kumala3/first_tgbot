from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from tgbot.models.first_mode import User


class Sentinel(BaseMiddleware):
    allowed_updates = ["message", "callback_query"]

    async def trigger(self, action, arg):
        obj, *args, data = arg

        if not any(update in action for update in self.allowed_updates):
            return

        if not action.startswith("process_"):
            return
        handler = current_handler.get()
        if not handler:
            return

        allow = getattr(handler, "allow", False)
        if allow:
            return

        user: User = data.get("user")

        if not user.allowed:
            message = obj.message if isinstance(obj, types.CallbackQuery) else obj
            await message.answer("You are blocked")
            raise CancelHandler()
