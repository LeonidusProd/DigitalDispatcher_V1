import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from handlers import router
from backend_connection import get_bot_token


dp = Dispatcher()


async def main():
    bot_token = str(await get_bot_token())
    print(bot_token)
    bot = Bot(token=bot_token, parse_mode='HTML')
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
