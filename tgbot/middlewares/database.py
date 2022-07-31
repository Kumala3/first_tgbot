from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware


class DatabaseMiddleware(LifetimeControllerMiddleware):

    def __init__(self, session_pool) -> None:
        super().__init__()
        self.session_pool = session_pool

    async def on_process_message(self, message, data):
