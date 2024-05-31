import aiohttp
from functools import wraps
from decorators import authorization
import json

base_url = "http://127.0.0.1:8000"


@authorization(base_url)
async def get_bot_token(token):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{base_url}/api/v1/bottokens/manage/1',
                    headers=headers
            ) as response:
                # print(await response.json())
                return dict(await response.json())['residentBotToken']
    except aiohttp.ClientError as e:
        print(e)


@authorization(base_url)
async def get_complexes_list(token):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{base_url}/api/v1/complex/',
                    headers=headers
            ) as response:
                # print(await response.json())
                return list(await response.json())
    except aiohttp.ClientError as e:
        print(e)


@authorization(base_url)
async def get_houses_list(token, complex_id):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{base_url}/api/v1/complex/{complex_id}/houses',
                    headers=headers
            ) as response:
                # print(await response.json())
                return list(await response.json())
    except aiohttp.ClientError as e:
        print(e)


# @authorization(base_url)
async def check_user_exists(token, user_id):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{base_url}/api/v1/resident/by_tgid/{user_id}',
                    headers=headers
            ) as response:
                resp = dict(await response.json())
                if resp['exists']:
                    return True, dict(resp['resident'])['pk']
                else:
                    return False, -1
    except aiohttp.ClientError as e:
        print(e)


# @authorization(base_url)
async def get_or_create_resident(token, state):
    headers = {
        'Authorization': f'Token {token}',
    }

    user_data = dict(await state.get_data())

    check, resident_id = await check_user_exists(token, user_data['user_tg_id'])

    if check:
        return resident_id
    else:
        try:
            data = {
                'name': user_data['resident_name'],
                'surname': user_data['resident_surname'],
                'phone': user_data['phone_number'],
                'tg_id': user_data['user_tg_id']
            }

            if 'resident_patronymic' in user_data and user_data['resident_patronymic'] is not '-':
                data['patronymic'] = user_data['resident_patronymic']

            async with aiohttp.ClientSession() as session:
                async with session.post(
                        url=f'{base_url}/api/v1/resident/create/',
                        headers=headers,
                        data=data
                ) as response:
                    return dict(await response.json())['pk']
        except aiohttp.ClientError as e:
            print(e)


@authorization(base_url)
async def create_new_request(token, state, bot):
    headers = {
        'Authorization': f'Token {token}',
    }

    user_data = dict(await state.get_data())

    form = aiohttp.FormData()
    form.add_field('text', str(user_data['request_reason']))
    form.add_field('status', 1)
    form.add_field('resident', await get_or_create_resident(token, state))
    form.add_field('address', int(user_data['selected_address_id']))

    if 'apartment_number' in user_data:
        form.add_field('apartment', int(user_data['apartment_number']))

    if 'request_photo' in user_data:
        async with aiohttp.ClientSession() as session:
            try:
                file = await bot.get_file(user_data['request_photo'])
                file_path = file.file_path
                async with session.get(f'https://api.telegram.org/file/bot{get_bot_token()}/'
                                       f'{file_path}') as response:
                    if response.status == 200:
                        photo_data = await response.read()

                        form.add_field('photo',
                                       photo_data,
                                       filename='request_photo.jpg',
                                       content_type='multipart/form-data')
            except aiohttp.ClientError as e:
                print(e)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=f'{base_url}/api/v1/request/create/',
                    headers=headers,
                    data=form
            ) as response:
                return await response.json()
    except aiohttp.ClientError as e:
        print(e)


# async def get_test_data():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://localhost:8000/api/v1/test/') as response:
#             return await response.json()
#
#
# async def get_complexes_data():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://127.0.0.1:8000/api/v1/complexes/') as response:
#             return await response.json()
#
#
# async def get_houses_data():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://127.0.0.1:8000/api/v1/houses/') as response:
#             return await response.json()
#
#
# async def get_complex_houses_data(complex_id: int):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f'http://127.0.0.1:8000/api/v1/complex_houses/{complex_id}') as response:
#             return await response.json()
#
#
# async def get_user_by_tgID(user_tgID: int):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f'http://127.0.0.1:8000/api/v1/resident/by_tgID/{user_tgID}') as response:
#             return await response.json()
#
#
# async def create_user(snp: str, phone: str, user_tgID: int):
#     async with aiohttp.ClientSession() as session:
#         data = {
#             'snp': snp,
#             'phone': phone,
#             'tg_id': user_tgID
#         }
#         async with session.post(f'http://127.0.0.1:8000/api/v1/resident', data=data) as response:
#             return await response.json()
#
#
# async def create_request(text: str, resident: int, house: int, apartment: int, photo: str):
#     async with aiohttp.ClientSession() as session:
#         data = {
#             'text': text,
#             'resident': resident,
#             'address': house,
#         }
#         if apartment != -1:
#             data['apartment'] = apartment
#         if photo != '-1':
#             data['photo'] = photo
#         async with session.post(f'http://127.0.0.1:8000/api/v1/requests/', data=data) as response:
#             return await response.json()


# async def send_data_to_api(bot_data):
#     async with aiohttp.ClientSession() as session:
#         url = 'http://localhost:8000/api/v1/requests/'  # Предполагая, что это URL вашего API для создания объектов Request
#         headers = {'Content-Type': 'application/json'}
#         async with session.post(url, data=json.dumps(bot_data), headers=headers) as response:
#             if response.status == 201:  # Проверяем успешность создания объекта на сервере
#                 return True
#             else:
#                 return False
