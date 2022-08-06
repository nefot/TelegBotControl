from hanlders import client
from loader import dp


async def on_start(_):
    print("Бот стартовал")


if __name__ == '__main__':
    from aiogram import executor

    executor.start(dp, client.on_startup())
    executor.start_polling(dp, on_startup=on_start, skip_updates=True)
