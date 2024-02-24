from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import InlineKeyboardBuilder

import backend_connection as bc


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


async def cancel():
    cancel_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отмена', callback_data='to_start')]
    ])

    return cancel_keyboard


async def complexes():
    complex_keyboard = InlineKeyboardBuilder()
    all_complexes = await bc.get_complexes_data()
    for complex in all_complexes:
        complex_keyboard.add(
            InlineKeyboardButton(text=complex['name'], callback_data=f'complex_{complex['pk']}')
        )
    complex_keyboard.add(InlineKeyboardButton(text='Отмена', callback_data='to_start'))
    return complex_keyboard.adjust(1).as_markup()


async def complex_houses(complex_id: int):
    houses_keyboard = InlineKeyboardBuilder()
    all_houses = await bc.get_complex_houses_data(complex_id)
    for house in all_houses:
        houses_keyboard.add(
            InlineKeyboardButton(text=house['address'], callback_data=f'house_{house['pk']}')
        )
    houses_keyboard.add(InlineKeyboardButton(text='Изменить ЖК', callback_data='back_to_complexes'))
    houses_keyboard.add(InlineKeyboardButton(text='Отмена', callback_data='to_start'))
    return houses_keyboard.adjust(1).as_markup()


async def yes_or_no(param: str):
    if 'ask_apartment' in param:
        yes_text = 'Указать'
        no_text = 'Не указывать'
    elif 'ask_photo' in param:
        yes_text = 'Приложить'
        no_text = 'Не прикладывать'

    yes_or_no_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=yes_text, callback_data=f'{param}_yes')],
        [InlineKeyboardButton(text=no_text, callback_data=f'{param}_no')],
        [InlineKeyboardButton(text='Отмена', callback_data='to_start')]
    ])

    return yes_or_no_keyboard


async def request_phone():
    request_phone_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Отправить номер телефона', request_contact=True)]
    ], resize_keyboard=True)
    return request_phone_keyboard


async def submit_request():
    submit_request_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Всё верно', callback_data=f'submit_request')],
        [InlineKeyboardButton(text='Отмена', callback_data='to_start')]
    ])
    return submit_request_keyboard
