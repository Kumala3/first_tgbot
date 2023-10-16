import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.echo import register_echo
from tgbot.handlers.testing import register_tests
# from tgbot.handlers.user import register_user
from tgbot.middlewares.environment import EnvironmentMiddleware
from tgbot.middlewares.bit_brother import BigBrother
from tgbot.middlewares.throttling import ThrottlingMiddleWare

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    dp.setup_middleware(ThrottlingMiddleWare(limit=10))
    dp.setup_middleware(BigBrother(config=config))
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter, event_handlers=[dp.message_handlers])


def register_all_handlers(dp):
    register_admin(dp)
    register_tests(dp)
    register_echo(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
