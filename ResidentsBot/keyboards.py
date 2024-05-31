from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton,
                           ReplyKeyboardRemove, WebAppInfo)
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder
from aiogram.fsm.context import FSMContext

import backend_connection as bc


# Возможный простой вариант для start_keyboard
# send_request_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Отправить заявку', callback_data='send_request')]
# ])


async def start_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Отправить заявку', callback_data='send_req_first_step'))
    keyboard.add(InlineKeyboardButton(text='Проверить статус', callback_data='!check_status'))
    return keyboard.as_markup()


async def request_first_step(state: FSMContext):
    user_data = dict(await state.get_data())
    selected_address = None
    entered_apartment = None

    if 'selected_address_name' in user_data:
        selected_address = user_data['selected_address_name']
    if 'apartment_number' in user_data:
        entered_apartment = user_data['apartment_number']

    if selected_address:
        address_select_btn_text = f'Адрес: {selected_address}. Изменить.'
    else:
        address_select_btn_text = 'Выбрать адрес'

    if entered_apartment:
        entered_apartment_btn_text = f'Квартира: {entered_apartment}. Изменить.'
    else:
        entered_apartment_btn_text = 'Указать квартиру'

    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text=address_select_btn_text, callback_data='select_complex'))
    keyboard.row(InlineKeyboardButton(text=entered_apartment_btn_text, callback_data='input_apartment'))
    if selected_address is not None:
        keyboard.row(InlineKeyboardButton(text='Следующий шаг', callback_data='second_step'))
    return keyboard.as_markup()


async def complexes_list():
    keyboard = InlineKeyboardBuilder()
    all_complexes = await bc.get_complexes_list()

    for complex_el in all_complexes:
        keyboard.row(
            InlineKeyboardButton(text=complex_el['name'], callback_data=f'complex_selected_{complex_el['pk']}')
        )
    # keyboard.add(InlineKeyboardButton(text='Отмена', callback_data='to_start'))
    return keyboard.as_markup()


async def houses_list(complex_id):
    keyboard = InlineKeyboardBuilder()
    all_houses = await bc.get_houses_list(complex_id)

    for house_el in all_houses:
        keyboard.row(
            InlineKeyboardButton(text=house_el['name'],
                                 callback_data=f'house_selected_{house_el['pk']}_{house_el['name']}')
        )
    # keyboard.add(InlineKeyboardButton(text='Отмена', callback_data='to_start'))
    return keyboard.as_markup()


async def request_third_step(state: FSMContext):
    user_data = dict(await state.get_data())
    entered_snp = None
    entered_phone = None

    if 'resident_name' in user_data:
        if 'resident_patronymic' in user_data and user_data['resident_patronymic'] is not '-':
            patronymic = f' {user_data['resident_patronymic']}'
        else:
            patronymic = ''

        entered_snp = f'{user_data['resident_surname']} {user_data['resident_name']}{patronymic}'
    if 'phone_number' in user_data:
        entered_phone = user_data['phone_number']

    if entered_snp:
        entered_snp_btn_text = f'ФИО: {entered_snp}. Изменить.'
    else:
        entered_snp_btn_text = 'Ввести ФИО'

    if entered_phone:
        entered_phone_btn_text = f'Номер телефона: {entered_phone}. Изменить.'
    else:
        entered_phone_btn_text = 'Указать номер телефона'

    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text=entered_snp_btn_text, callback_data='input_snp'))
    keyboard.row(InlineKeyboardButton(text=entered_phone_btn_text, callback_data='input_phone'))
    if entered_snp is not None and entered_phone is not None:
        keyboard.row(InlineKeyboardButton(text='Сохранить заявку', callback_data='save_request'))
    return keyboard.as_markup()


async def share_phone_number():
    request_phone_keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Отправить номер телефона', request_contact=True)]],
        resize_keyboard=True
    )
    return request_phone_keyboard
# keyboard = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Поделиться номером телефона', request_contact=True)]
# ], resize_keyboard=True)
# return keyboard


# async def start_keyboard():
#     start_keyboard = InlineKeyboardBuilder()
#     # Возможная динамическая генерация
#     start_keyboard.add(
#         InlineKeyboardButton(text='Отправить заявку', callback_data='send_request')
#     )
#     return start_keyboard.as_markup()


# async def cancel():
#     cancel_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='Отмена', callback_data='to_start')]
#     ])
#
#     return cancel_keyboard
#
#
# async def complexes():
#     complex_keyboard = InlineKeyboardBuilder()
#     all_complexes = await bc.get_complexes_data()
#     for complex in all_complexes:
#         complex_keyboard.add(
#             InlineKeyboardButton(text=complex['name'], callback_data=f'complex_{complex['pk']}')
#         )
#     complex_keyboard.add(InlineKeyboardButton(text='Отмена', callback_data='to_start'))
#     return complex_keyboard.adjust(1).as_markup()
#
#
# async def complex_houses(complex_id: int):
#     houses_keyboard = InlineKeyboardBuilder()
#     all_houses = await bc.get_complex_houses_data(complex_id)
#     for house in all_houses:
#         houses_keyboard.add(
#             InlineKeyboardButton(text=house['address'], callback_data=f'house_{house['pk']}')
#         )
#     houses_keyboard.add(InlineKeyboardButton(text='Изменить ЖК', callback_data='back_to_complexes'))
#     houses_keyboard.add(InlineKeyboardButton(text='Отмена', callback_data='to_start'))
#     return houses_keyboard.adjust(1).as_markup()
#
#
# async def yes_or_no(param: str):
#     if 'ask_apartment' in param:
#         yes_text = 'Указать'
#         no_text = 'Не указывать'
#     elif 'ask_photo' in param:
#         yes_text = 'Приложить'
#         no_text = 'Не прикладывать'
#
#     yes_or_no_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text=yes_text, callback_data=f'{param}_yes')],
#         [InlineKeyboardButton(text=no_text, callback_data=f'{param}_no')],
#         [InlineKeyboardButton(text='Отмена', callback_data='to_start')]
#     ])
#
#     return yes_or_no_keyboard
#
#
# async def request_phone():
#     request_phone_keyboard = ReplyKeyboardMarkup(keyboard=[
#         [KeyboardButton(text='Отправить номер телефона', request_contact=True)]
#     ], resize_keyboard=True)
#     return request_phone_keyboard
#
#
# async def submit_request():
#     submit_request_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='Всё верно', callback_data=f'submit_request')],
#         [InlineKeyboardButton(text='Отмена', callback_data='to_start')]
#     ])
#     return submit_request_keyboard
