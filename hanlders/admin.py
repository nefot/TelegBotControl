from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher.filters.state import State, StatesGroup
from keybroad.keybroad import admin_keyboard

from loader import dp, bot
from aiogram.types import Message


@dp.message_handler(commands='moderator', is_chat_admin=True)
async def make_changes(message: Message):
    global admin_id
    admin_id = message.from_user.id
    await bot.send_message(message.from_user.id, "ЧТО НАДО ХОЗЯИН", reply_markup=admin_keyboard)
    await message.delete


class FSMAdmin(StatesGroup):
    icon = State()
    name = State()
    description = State()


def check_rules(func):
    async def wrapper(message: Message, state=None):
        if message.from_user == admin_id:
            return await func(message, state)

        else:
            return await message.reply('bfjhgrhghrghr')

        return wrapper


@dp.message_handler(commands='Загрузить', state=None)
async def sm_star(message: Message):
    if message.from_user == admin_id:
        await FSMAdmin.icon.set()

        await message.reply('Загрузи иконку')


@check_rules
@dp.message_handler(content_types=['photo'], state=FSMAdmin.icon)
async def load_icon(message: Message, state: FSMContext):
    if message.from_user.id == admin_id:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Введите название ")


@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: Message, state: FSMContext):
    if message.from_user == admin_id:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите описание")


@dp.message_handler(state=FSMAdmin.description)
async def load_name(message: Message, state: FSMContext):
    if message.from_user == admin_id:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply("Все")

        async with state.proxy() as data:
            await message.reply(str(data))
        await sql_add_device(state)
        await state.finish()


@dp.message_handler(state='*', commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: Message, state: FSMContext):
    if message.from_user == admin_id:

        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Canceled')
