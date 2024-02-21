from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import keyboards as kbs
import backend_connection


router = Router()

intermediate_data = {}
intermediate_user_status = {}


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.delete()
    await message.answer(
        text="Привет, я бот Управляющей Компании \"Симфония\"!\n\n"
             "Через меня можно обратиться в компанию и оставить аварийную заявку.\n\n"
             "Чтобы оставить обращение, нажмите на кнопку.",
        reply_markup=await kbs.start_keyboard()
    )


@router.message(F.text == 'Тест')
async def test_text(message: Message):
    await message.answer(text=backend_connection.get_test_data())


# Для обработки инлайн кнопок
# @router.callback_query(F.data.startswith('send_request'))
# async def callback_query(callback: CallbackQuery):
#     # Отправка обычного текста
#     await callback.message.answer(f'{callback.data}')
#     # Отправка уведомления
#     await callback.answer('SSSS')