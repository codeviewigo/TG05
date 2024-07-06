import asyncio, logging
from aiogram import Bot, Dispatcher

from config import TG_TOKEN
from handlers import commands, callbacks


async def main():
    bot = Bot(TG_TOKEN)
    dp = Dispatcher()
    dp.include_routers(
        commands.router,
        callbacks.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен пользователем!')
