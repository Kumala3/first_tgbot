from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from aiogram import types


def register_file(dp: Dispatcher):
    @dp.message_handler(content_types=types.ContentType.DOCUMENT)
    async def get_file(message: Message):
        file_id = message.document.file_id
        
