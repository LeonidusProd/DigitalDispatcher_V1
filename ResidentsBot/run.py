import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher

from handlers import router


dp = Dispatcher()
RESIDENTS_BOT_TOKEN = str(os.environ.get(
    "RESIDENTS_BOT_TOKEN",
    default='6200922540:AAHYgNdtkiWKAk1pqcHm2oIC8vuCz7hm8Fo'
))
bot = Bot(token=RESIDENTS_BOT_TOKEN, parse_mode='HTML')


async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
