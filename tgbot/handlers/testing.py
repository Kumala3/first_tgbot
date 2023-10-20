from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from tgbot.misc.states import Test
from aiogram import Dispatcher, types

from tgbot.misc.throttling import rate_limit


def register_tests(dp: Dispatcher):
    @rate_limit(10, key="test", num_messages=5)
    @dp.message_handler(Command('test'), state=None)
    async def testing_user(message: types.Message):
        await message.answer("Вы начали тестирование программы.\n"
                             "Вопрос 1.\n"
                             "Вы часто занимаетесь тупыми делами\n"
                             "Листаете бесконечную ленту тик-тока или ютуб-шортса?")

        await Test.q1.set()

    @dp.message_handler(state=Test.q1)
    async def answer_q1(message: types.Message, state: FSMContext):
        user_answer = message.text

        await state.update_data(answer1=user_answer)

        await message.answer("Your memory's gotten worse lately. You need to work on yourself.")

        await Test.q2.set()

    @dp.message_handler(state=Test.q2)
    async def answer_q2(message: types.Message, state: FSMContext):
        data = await state.get_data()

        answer_1 = data.get("answer1")
        answer_2 = message.text

        await message.answer("Thank you for our test!Have a nice day")
        await message.answer(f"Answer_1: {answer_1}")
        await message.answer(f"Answer_2: {answer_2}")

        await state.reset_state()
