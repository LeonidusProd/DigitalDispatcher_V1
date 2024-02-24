import aiohttp
import json


async def get_test_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8000/api/v1/test/') as response:
            return await response.json()


async def get_complexes_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/api/v1/complexes/') as response:
            return await response.json()


async def get_houses_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/api/v1/houses/') as response:
            return await response.json()


async def get_complex_houses_data(complex_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://127.0.0.1:8000/api/v1/complex_houses/{complex_id}') as response:
            return await response.json()


async def get_user_by_tgID(user_tgID: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://127.0.0.1:8000/api/v1/resident/by_tgID/{user_tgID}') as response:
            return await response.json()


async def create_user(snp: str, phone: str, user_tgID: int):
    async with aiohttp.ClientSession() as session:
        data = {
            'snp': snp,
            'phone': phone,
            'tg_id': user_tgID
        }
        async with session.post(f'http://127.0.0.1:8000/api/v1/resident', data=data) as response:
            return await response.json()


async def create_request(text: str, resident: int, house: int, apartment: int, photo: str):
    async with aiohttp.ClientSession() as session:
        data = {
            'text': text,
            'resident': resident,
            'address': house,
        }
        if apartment != -1:
            data['apartment'] = apartment
        if photo != '-1':
            data['photo'] = photo
        async with session.post(f'http://127.0.0.1:8000/api/v1/requests/', data=data) as response:
            return await response.json()


# async def send_data_to_api(bot_data):
#     async with aiohttp.ClientSession() as session:
#         url = 'http://localhost:8000/api/v1/requests/'  # Предполагая, что это URL вашего API для создания объектов Request
#         headers = {'Content-Type': 'application/json'}
#         async with session.post(url, data=json.dumps(bot_data), headers=headers) as response:
#             if response.status == 201:  # Проверяем успешность создания объекта на сервере
#                 return True
#             else:
#                 return False
