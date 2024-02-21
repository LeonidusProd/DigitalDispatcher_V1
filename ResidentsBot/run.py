import asyncio
import logging

from aiogram import Bot, Dispatcher

from backend_config.settings import RESIDENTS_BOT_TOKEN
from handlers import router


dp = Dispatcher()


async def main():
    bot = Bot(token=RESIDENTS_BOT_TOKEN)
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')