from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
