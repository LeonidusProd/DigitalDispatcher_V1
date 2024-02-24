import os

from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command, BaseFilter
from aiogram.types import Message, CallbackQuery, ContentType

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import keyboards as kbs
import backend_connection as bc

router = Router()


class InterUserState(StatesGroup):
    at_start = State()
    select_complex = State()
    select_complex_house = State()

    ask_apartment = State()
    get_apartment = State()
    ask_apartment_warning = State()

    get_reason = State()

    ask_reason_photo = State()
    get_reason_photo = State()
    ask_reason_photo_warning = State()

    get_snp = State()
    get_phone_number = State()
    submit_request = State()

    all_requests = State()
    definite_request = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(InterUserState.at_start)
    await message.delete()
    await message.answer(
        text="Привет, я бот Управляющей Компании \"Симфония\"!\n\n"
             "Через меня можно обратиться в компанию и оставить аварийную заявку.\n\n"
             "Чтобы оставить обращение, нажмите на кнопку.",
        reply_markup=await kbs.start_keyboard()
    )


@router.callback_query(lambda query: query.data in ['to_start', 'cancel'])
async def callback_to_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(InterUserState.at_start)
    await callback.message.delete()
    await callback.message.answer(
        text="Привет, я бот Управляющей Компании \"Симфония\"!\n\n"
             "Через меня можно обратиться в компанию и оставить аварийную заявку.\n\n"
             "Чтобы оставить обращение, нажмите на кнопку.",
        reply_markup=await kbs.start_keyboard()
    )


@router.callback_query(lambda query: query.data in ['send_request', 'back_to_complexes'])
async def get_complex(callback: CallbackQuery, state: FSMContext):
    await state.set_state(InterUserState.select_complex)
    await callback.message.delete()
    await callback.message.answer(
        text='Выберите свой жилой комплекс',
        reply_markup=await kbs.complexes()
    )


@router.callback_query(F.data.startswith('complex_'))
async def get_house(callback: CallbackQuery, state: FSMContext):
    complex_id = callback.data.split('_')[1]
    await state.update_data(complex=int(complex_id))
    await state.set_state(InterUserState.select_complex_house)
    await callback.message.delete()
    await callback.message.answer(
        text='Выберите свой жилой дом',
        reply_markup=await kbs.complex_houses(complex_id=int(complex_id))
    )


@router.callback_query(F.data.startswith('house_'))
async def ask_apartment(callback: CallbackQuery, state: FSMContext):
    house_id = callback.data.split('_')[1]
    await state.update_data(house=int(house_id))
    await state.set_state(InterUserState.ask_apartment)
    await callback.message.delete()
    await callback.message.answer(
        text='Хотите указать номер квартиры?',
        reply_markup=await kbs.yes_or_no(param='ask_apartment')
    )


@router.callback_query(lambda query: query.data in ['ask_apartment_yes', 'ask_apartment_warning_yes'])
async def get_apartment(callback: CallbackQuery, state: FSMContext):
    await state.set_state(InterUserState.get_apartment)
    await callback.message.delete()
    await callback.message.answer(
        text='Напишите ваш номер квартиры:',
        reply_markup=await kbs.cancel()
    )


@router.callback_query(lambda query: query.data in ['ask_apartment_no'])
async def ask_apartment_warning(callback: CallbackQuery, state: FSMContext):
    await state.set_state(InterUserState.ask_apartment_warning)
    await callback.message.delete()
    await callback.message.answer(
        text='Ваш номер квартиры может быть нужен для нахождения вас.\n\n'
             'Вы уверены, что не хотите его указать?',
        reply_markup=await kbs.yes_or_no(param='ask_apartment_warning')
    )


@router.callback_query(lambda query: query.data in ['ask_apartment_warning_no'])
async def ask_apartment_warning(callback: CallbackQuery, state: FSMContext):
    await state.set_state(InterUserState.get_reason)
    await callback.message.delete()
    await callback.message.answer(
        text='Расскажите в одном-двух предложениях, что у вас случилось?',
        reply_markup=await kbs.cancel()
    )


@router.message(lambda message: message.content_type == ContentType.TEXT)
async def union_text_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == InterUserState.get_apartment:
        await state.update_data(apartment=message.text)
        await state.set_state(InterUserState.get_reason)
        await message.delete()
        await message.chat.delete_message(message.message_id - 1)
        await message.answer(
            text='Расскажите в одном-двух предложениях, что у вас случилось?',
            reply_markup=await kbs.cancel()
        )
    elif current_state == InterUserState.get_reason:
        await state.update_data(reason=message.text)
        await state.set_state(InterUserState.ask_reason_photo)
        await message.delete()
        await message.chat.delete_message(message.message_id - 1)
        await message.answer(
            text='Хотите приложить фотографию?',
            reply_markup=await kbs.yes_or_no(param='ask_photo')
        )
    elif current_state == InterUserState.get_snp:
        await state.update_data(snp=message.text)
        await state.set_state(InterUserState.get_phone_number)
        await message.delete()
        await message.chat.delete_message(message.message_id - 1)
        await message.answer(
            text='Нам нужен ваш номер телефона',
            reply_markup=await kbs.request_phone()
        )


@router.callback_query(lambda query: query.data in ['ask_photo_yes', 'ask_photo_warning_yes'])
async def get_photo(callback: CallbackQuery, state: FSMContext):
    await state.set_state(InterUserState.get_reason_photo)
    await callback.message.delete()
    await callback.message.answer(
        text='Отправьте фото следующим сообщением:',
        reply_markup=await kbs.cancel()
    )


@router.callback_query(lambda query: query.data in ['ask_photo_no'])
async def ask_photo_warning(callback: CallbackQuery, state: FSMContext):
    await state.set_state(InterUserState.ask_reason_photo_warning)
    await callback.message.delete()
    await callback.message.answer(
        text='Имея фотографию нам будет легче исправить проблему.\n\n'
             'Вы уверены, что не хотите её приложить?',
        reply_markup=await kbs.yes_or_no(param='ask_photo_warning')
    )


@router.callback_query(lambda query: query.data in ['ask_photo_warning_no'])
async def ask_apartment_warning(callback: CallbackQuery, state: FSMContext):
    await state.set_state(InterUserState.get_snp)
    await callback.message.delete()
    await callback.message.answer(
        text='Представьтесь, как вас зовут?',
        reply_markup=await kbs.cancel()
    )


@router.message(lambda message: message.content_type == ContentType.PHOTO)
async def union_photo_handler(message: Message, state: FSMContext, bot: Bot):
    current_state = await state.get_state()
    if current_state == InterUserState.get_reason_photo:
        photo = message.photo[-1]
        photo_info = await bot.get_file(photo.file_id)
        photo_inner_path = photo_info.file_path
        photo_out_dir = f"media/request/{message.from_user.id}"
        if not os.path.exists(photo_out_dir):
            os.makedirs(photo_out_dir)
        photo_out_path = f'{photo_out_dir}/{photo.file_id}.jpg'

        await bot.download_file(photo_inner_path, photo_out_path)
        await state.update_data(photo_path=photo_out_path)

        await state.set_state(InterUserState.get_snp)
        await message.delete()
        await message.chat.delete_message(message.message_id - 1)
        await message.answer(
            text='Представьтесь, как вас зовут?',
            reply_markup=await kbs.cancel()
        )


@router.message(lambda message: message.content_type == ContentType.CONTACT)
async def handle_contact(message: Message, state: FSMContext, bot: Bot):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()
    await state.set_state(InterUserState.submit_request)
    await message.delete()

    all_complexes = await bc.get_complexes_data()
    our_complex = next(item["name"] for item in all_complexes if item["pk"] == data['complex'])

    all_houses = await bc.get_houses_data()
    our_house = next(item["address"] for item in all_houses if item["pk"] == data['house'])

    message_text = (f'Давайте проверим информацию:\n\n'
                    f'ЖК: {our_complex}\n'
                    f'Дом: {our_house}\n'
                    f'Квартира: {data.get('apartment', 'Не указана')}\n'
                    f'Причина: {data['reason']}\n'
                    f'ФИО: {data['snp']}\n'
                    f'Номер телефона: {data['phone_number']}\n')

    if data.get('photo_id', None) is not None:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=data['photo_id'],
            caption=message_text,
            reply_markup=await kbs.submit_request()
        )
    else:
        await message.answer(
            text=message_text,
            reply_markup=await kbs.submit_request()
        )


@router.callback_query(lambda query: query.data in ['submit_request'])
async def submit_request(callback: CallbackQuery, state: FSMContext, bot: Bot):
    inter_data = await state.get_data()

    check_user = await bc.get_user_by_tgID(int(callback.message.from_user.id))

    if not check_user[0]['is_exist']:
        out_user_id = await bc.create_user(inter_data['snp'], inter_data['phone_number'], int(callback.message.from_user.id))
    else:
        out_user_id = check_user[0]['pk']

    new_request = await bc.create_request(inter_data['reason'], out_user_id, inter_data['house'],
                                          inter_data.get('apartment', -1), inter_data.get('photo_path', '-1'))


    # if inter_data.get('photo_id', None) is not None:
    #     photo = await bot.get_file(inter_data['photo_id'])
    #     photo_inner_path = photo.file_path
    #     photo_out_path = f"../media/request/{callback.from_user.id}{inter_data['photo_id']}.jpg"
    #     await bot.download_file(photo_inner_path, photo_out_path)







    # send_data = {
    #
    # }

    # await bc.send_data_to_api(data)
    # await callback.answer('Отправлено')
