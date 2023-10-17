from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()

    text = [
        f"Эхо в состояние: {state_name} ",
        "Сообщение: ",
        message.text
    ]

    await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    @dp.message_handler()
    async def bot_echo(message: types.Message):
        text = [
            "Эхо без состояния",
            "Сообщение: ",
            message.text
        ]

        await message.answer('\n'.join(text), reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Обичная кнопкa", callback_data='button')]
            ]
        ))

    @dp.callback_query_handler(text="button")
    async def get_button(call: types.CallbackQuery):
        await call.message.answer("Вы нажали на кнопку")

    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)
