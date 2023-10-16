import asyncio

from aiogram.dispatcher.handler import current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram import types
from aiogram import Dispatcher
from aiogram.utils.exceptions import Throttled
from aiogram.dispatcher.handler import CancelHandler

from typing import Union


class ThrottlingMiddleWare(BaseMiddleware):

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix="antiflood"):
        super(ThrottlingMiddleWare, self).__init__()
        self.limit = limit
        self.prefix = key_prefix

    async def throttle(self, target: Union[types.Message, types.CallbackQuery]):
        handler = current_handler.get()
        if not handler:
            return

        dp = Dispatcher.get_current()

        limit = getattr(handler, "throttling_rate_limit", self.limit)
        # key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        key = getattr(handler, "throttling_key", None)
        if not key:
            return

        try:
            await dp.throttle(key=key, rate=limit)
        except Throttled as thr:
            await self.target_throttled(target, thr, dp, key)
            raise CancelHandler()

    @staticmethod
    async def target_throttled(target: Union[types.Message, types.CallbackQuery],
                               throttled: Throttled, dispatcher: Dispatcher, key: str):
        message = target.message if isinstance(target, types.CallbackQuery) else target
        delta = throttled.rate - throttled.delta

        if throttled.exceeded_count == 5:
            await message.reply("Пожалуйста не нажимайте на кнопки слишком часто или же вы попадете в мут на 3 минуты")
            return
        elif throttled.exceeded_count == 7:
            await message.reply(f"Вы превысили предел нажимания на кнопки.Вы отправились в мут на {delta} секунд.")
            return

        await asyncio.sleep(delta)

        thr = await dispatcher.check_key(key)
        if thr.exceeded_count == throttled.exceeded_count:
            await message.reply("Вы были размучены, пожалуйста не нужно нажимать на кнопки слишком часто!")

    async def on_process_message(self, message, data):
        await self.throttle(message)

    async def on_process_callback_query(self, call, data):
        await self.throttle(call)
