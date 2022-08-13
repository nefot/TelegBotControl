import os
import socket

import aiogram.utils.exceptions
import pyautogui
import win32api
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, InputFile
import Dispether
from cmds import GetAnswer, Setup
from keybroadTel import keybroad
from loader import bot, dp
from screnslover import Make_Photo


class SomeStates(StatesGroup):
    state1 = State()


@dp.message_handler(commands=['click'])
async def clicks(message: Message):
    try:
        pyautogui.click()
        await bot.send_message(message.from_user.id, text='клик произведен', reply_markup=keybroad.keyboard_client)
    except Exception:
        await bot.send_message(message.from_user.id, text='ошибка', reply_markup=keybroad.keyboard_client)


@dp.message_handler(commands=['text'])
async def Command_start(message: Message):
    await message.answer("напишите текст:", reply_markup=None)
    await SomeStates.state1.set()


@dp.message_handler(state=SomeStates.state1)
async def get_username(message: Message, state: FSMContext):
    await state.update_data(address=message.text)

    data = await state.get_data()

    pyautogui.typewrite(f'{data["address"]}\n')
    await message.answer("Комманда " + "<<" + data['address'] + "<<" + " выведена",
                         reply_markup=keybroad.keyboard_client)
    await SomeStates.next()


@dp.message_handler(commands=['c'])  # Запуск команд в командной строке
async def Command_start(message: Message):
    await message.answer("Командная строка:", reply_markup=keybroad.keyboard_client)

    if len(GetAnswer(message.text)) > 4096:
        for x in range(0, len(GetAnswer(message.text)), 4096):
            await bot.send_message(message.chat.id, GetAnswer(message.text)[x:x + 4096])
    else:
        try:
            await bot.send_message(message.chat.id, GetAnswer(message.text))
        except aiogram.utils.exceptions.MessageTextIsEmpty:
            await bot.send_message(message.chat.id, "MessageTextIsEmpty")
            print("MessageTextIsEmpty")


@dp.message_handler(commands=['s'])  # Запуск приложения
async def Command_start(message: Message):
    await message.answer("запускается...", reply_markup=keybroad.keyboard_client)

    if len(Setup(''.join(message.text.split(" ")[1]))) > 4096:
        for x in range(0, len(Setup(''.join(message.text.split(" ")[1]))), 4096):
            await bot.send_message(message.chat.id, Setup(''.join(message.text.split(" ")[1]))[x:x + 4096])
    else:
        await bot.send_message(message.chat.id, Setup(''.join(message.text.split(" ")[1])))




@dp.message_handler(commands=['exists'])
async def command_devices(message: Message):
    win32api.ExitWindows()


@dp.message_handler(commands=['shutdown'])
async def command_devices(message: Message):
    win32api.WinExec()


@dp.message_handler(commands=['shut'])
async def command_devices(message: Message):
    await bot.send_message(message.from_user.id, text='abroad.menu2', reply_markup=keybroad.menu2)


@dp.message_handler(commands=['undo'])
async def command_devices(message: Message):
    await bot.send_message(message.from_user.id, text='keyboard.menu', reply_markup=keybroad.keyboard_client)


@dp.message_handler(commands=['kill'])
async def command_devices(message: Message):
    pyautogui.typewrite('/kill\n')


@dp.message_handler(commands=['foto'])
async def bot_send_foto(message: Message):
    Make_Photo()
    img = InputFile('pic.png')
    await bot.send_photo(message.from_user.id, img)


@dp.message_handler(commands=['menu_dir'])
async def command_devices(message: Message):
    await bot.send_message(message.from_user.id, text='keyboard.menu', reply_markup=keybroad.menu_dir)


@dp.message_handler(commands=['назад'])
async def command_devices(message: Message):
    await bot.send_message(message.from_user.id, text='keyboard.menu', reply_markup=keybroad.keyboard_client)


allowed_names = ["dir", "cd", "tree"]


@dp.message_handler()
async def command_devices(message: Message):
    if message.text.split(" ")[0] in allowed_names:
        await bot.send_message(message.from_user.id, GetAnswer(message.text), reply_markup=None)

    if message.text == "кирилл" or message.text == "/кирилл":
        os.chdir("C:\\Users\kiril\OneDrive\Рабочий стол ")

    if message.text == "артем" or message.text == "/артем":
        os.chdir("C:\\Users\Paavel\Desktop")

    if message.text == "программы" or message.text == "/программы":
        os.chdir("C:\\Program Files")

    if message.text == "Задачи" or message.text == "задачи":
        if len(Dispether.GetTask()) > 4096:
            for x in range(0, len(Dispether.GetTask()), 4096):
                await bot.send_message(message.chat.id, Dispether.GetTask()[x:x + 4096],
                                       reply_markup=keybroad.keyboard_client)
        else:
            await bot.send_message(message.chat.id, Dispether.GetTask())

    if message.text.split(" ")[0] == "убить":
        if message.text.split(" ")[1].isdigit() == False:

            Dispether.KillTask(message.text.split(" ")[1])
        else:

            Dispether.KillTaskInt(int(message.text.split(" ")[1]))

    if message.text.split(" ")[0] == "отправить":
        bot.send_document(message.chat.id, open(message.text.split(" ")[1]))

    if message.text == "функции":
        pass

    else:
        pass


async def Directory(command, message):
    if len(GetAnswer(' '.join(command))) > 4096:
        for x in range(0, len(GetAnswer(' '.join(command))), 4096):
            await bot.send_message(message.chat.id, GetAnswer(' '.join(command))[x:x + 4096],
                                   reply_markup=keybroad.keyboard_client)
    else:
        await bot.send_message(message.chat.id, GetAnswer(' '.join(command)), reply_markup=keybroad.keyboard_client)


async def on_startup():
    user_should_be_notified = 1407136430  # Наверное это должны быть вы сами? Как всезнающий админ:)
    await bot.send_message(user_should_be_notified, 'Бот запущен, хост - ' + socket.gethostname(),
                           reply_markup=keybroad.keyboard_client)
