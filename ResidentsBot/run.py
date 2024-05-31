import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher

from handlers import router

from backend_connection import get_bot_token


dp = Dispatcher()
# RESIDENTS_BOT_TOKEN = str(os.environ.get(
#     "RESIDENTS_BOT_TOKEN",
#     default='6200922540:AAHYgNdtkiWKAk1pqcHm2oIC8vuCz7hm8Fo'
# ))
# RESIDENTS_BOT_TOKEN = ''
# bot = Bot(token=RESIDENTS_BOT_TOKEN, parse_mode='HTML')


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
