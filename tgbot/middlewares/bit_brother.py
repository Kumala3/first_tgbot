import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class BigBrother(BaseMiddleware):

    def __init__(self, config):
        super().__init__()
        self.config = config

    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info("НОВЫЙ АПДЕЙТ!!!!")
        logging.info("1. Pre Proces Update")
        logging.info("Следующая точка: Proces Update")
        data["middleware_data"] = "Это пройдет до on_pre_progress"

        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return

        if user in self.config.tg_bot.banned_users_ids:
            raise CancelHandler()

    async def on_process_update(self, update: types.Update, data: dict):
        logging.info(f"Вторая точка остановки, Proces Update: {data=}")
        logging.info("Следующая точка: Pre Proces Update")

    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info(f"3. Pre Proces Message: {data=}")
        logging.info("Следующая точка: Filters")
        data["middleware_data"] = "Это пройдет в on_proces_message"

    async def on_pre_process_callback_query(self, callback: types.CallbackQuery, data: dict):
        await callback.answer()