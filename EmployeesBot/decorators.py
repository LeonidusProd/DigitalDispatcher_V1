import aiohttp
from functools import wraps


def authorization(base_url):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            token = await login(base_url)
            try:
                result = await func(token, *args, **kwargs)
            finally:
                await logout(base_url, token)
            return result
        return wrapper
    return decorator


# Inner functions
async def login(base_url):
    try:
        async with aiohttp.ClientSession() as session:
            data = {
                'username': 'piter',
                'password': 'pass1234forpiter'
            }

            async with session.post(
                    url=f'{base_url}/auth/token/login',
                    data=data
            ) as response:
                return dict(await response.json())['auth_token']
    except aiohttp.ClientError as e:
        print(e)


async def logout(base_url, token):
    try:
        async with aiohttp.ClientSession() as session:
            headers = {
                'Authorization': f'Token {token}',
            }

            async with session.post(
                    url=f'{base_url}/auth/token/logout',
                    headers=headers
            ) as response:
                return await response.json()
    except aiohttp.ClientError as e:
        print(e)
