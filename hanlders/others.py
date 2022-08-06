from TelegramBot import dp
from aiogram.types import Message


@dp.message_handler()
async def echo(message: Message):
    text = f"Ты написал{message.text}"
    await message.reply(text=text)
