from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from backend_connection import get_test_data


# Возможный простой вариант для start_keyboard
# send_request_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Отправить заявку', callback_data='send_request')]
# ])


async def start_keyboard():
    start_keyboard = InlineKeyboardBuilder()
    # Возможная динамическая генерация
    start_keyboard.add(
        InlineKeyboardButton(text='Отправить заявку', callback_data='send_request')
    )
    return start_keyboard.as_markup()
