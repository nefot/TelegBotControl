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
from config import MY_ID
from keybroadTel import keybroad
from loader import bot, dp
from screnslover import Make_Photo
from aiogram import types


class SomeStates(StatesGroup):
    state1 = State()


@dp.message_handler(commands=['клик'])
async def clicks(message: Message):
    try:
        pyautogui.click()
        await bot.send_message(message.from_user.id, text='клик произведен', reply_markup=keybroad.keyboard_client)
    except Exception:
        await bot.send_message(message.from_user.id, text='ошибка', reply_markup=keybroad.keyboard_client)


@dp.message_handler(commands=['текст'])
async def Command_start(message: Message):
    await message.answer("напишите текст:", reply_markup=None)
    await SomeStates.state1.set()


@dp.message_handler(state=SomeStates.state1)
async def get_username(message: Message, state: FSMContext):
    await state.update_data(address=message.text)

    data = await state.get_data()

    pyautogui.typewrite(f'{data["address"]}\n')
    await message.answer("Команда " + "<< " + data['address'] + " >>" + " выведена",
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
            # print("MessageTextIsEmpty")


@dp.message_handler(commands=['s'])  # Запуск приложения
async def Command_start(message: Message):
    await message.answer("запускается...", reply_markup=keybroad.keyboard_client)

    if len(Setup(''.join(message.text.split(" ")[1]))) > 4096:
        for x in range(0, len(Setup(''.join(message.text.split(" ")[1]))), 4096):
            await bot.send_message(message.chat.id, Setup(''.join(message.text.split(" ")[1]))[x:x + 4096])
    else:
        await bot.send_message(message.chat.id, Setup(''.join(message.text.split(" ")[1])))


@dp.message_handler(commands=['выйти из системы'])
async def command_devices(message: Message):
    win32api.ExitWindows()


@dp.message_handler(commands=['назад'])
async def command_devices(message: Message):
    await bot.send_message(message.from_user.id, text='keyboard.menu', reply_markup=keybroad.keyboard_client)



@dp.message_handler(commands=["фото"])
async def bot_send_foto(message: Message):
    Make_Photo()
    img = InputFile('pic.png')
    await bot.send_photo(message.from_user.id, img)


@dp.message_handler(commands=['меню'])
async def command_devices(message: Message):
    await bot.send_message(message.from_user.id, text='keyboard.menu', reply_markup=keybroad.menu_dir)


@dp.message_handler(commands=['команды'])
async def command_devices(message: Message):
    await on_startup()


@dp.message_handler(commands=['назад'])
async def command_devices(message: Message):
    await bot.send_message(message.from_user.id, text='keyboard.menu', reply_markup=keybroad.keyboard_client)


allowed_command_names = ["dir", "cd", "tree"]
allowed_names = ["кирилл", "артем", "программы", "задачи", "убить", "отправить"]


@dp.message_handler()
async def command_devices(message: Message):
    # "dir", "cd", "tree"
    try:
        if message.text.split(" ")[0] in allowed_command_names:
            await bot.send_message(message.from_user.id, GetAnswer(message.text), reply_markup=None)
        #  кирилл
        if message.text == allowed_names[0] or message.text == "/" + allowed_names[0]:
            os.chdir("C:\\Users\kiril\OneDrive\Рабочий стол ")
        # артем
        if message.text == allowed_names[1] or message.text == "/" + allowed_names[1]:
            os.chdir("C:\\Users\Paavel\Desktop")
        #   программы
        if message.text == allowed_names[2] or message.text == "/" + allowed_names[2]:
            os.chdir("C:\\Program Files")
        # Задачи
        if message.text == allowed_names[3] or message.text == "/" + allowed_names[3]:
            if len(Dispether.GetTask()) > 4096:
                for x in range(0, len(Dispether.GetTask()), 4096):
                    await bot.send_message(message.chat.id, Dispether.GetTask()[x:x + 4096],
                                           reply_markup=keybroad.keyboard_client)
            else:
                await bot.send_message(message.chat.id, Dispether.GetTask())
        # убить
        if message.text.split(" ")[0] == allowed_names[4]:
            if not message.text.split(" ")[1].isdigit():

                Dispether.KillTask(message.text.split(" ")[1])
            else:

                Dispether.KillTaskInt(int(message.text.split(" ")[1]))

        if message.text.split(" ")[0] == allowed_names[5]:
            try:
                print(" ".join(message.text.split(" ")[1:]))
                await bot.send_message(message.chat.id, 'Загрузка файла')
                file = open(" ".join(message.text.split(" ")[1:]), 'rb')
                await bot.send_document(message.chat.id, file)

            except PermissionError as err:
                await bot.send_message(message.chat.id, err)

        if message.text == "функции":
            pass

        else:
            await bot.send_message(message.chat.id, 'что вы хотите этим сказать?')
    except Exception as error:
        await bot.send_message(message.chat.id, error)


async def Directory(command, message):
    if len(GetAnswer(' '.join(command))) > 4096:
        for x in range(0, len(GetAnswer(' '.join(command))), 4096):
            await bot.send_message(message.chat.id, GetAnswer(' '.join(command))[x:x + 4096],
                                   reply_markup=keybroad.keyboard_client)
    else:
        await bot.send_message(message.chat.id, GetAnswer(' '.join(command)), reply_markup=keybroad.keyboard_client)


async def on_startup():
    user_should_be_notified = MY_ID  # ID админа
    await bot.send_message(user_should_be_notified,
                           'Телеграм бот успешно запущен✔️\n'
                           f'хост -  {socket.gethostname()}\n\n'
                           f'<ins><b>Доступные быстрые команды:</b></ins>\n\n' + '\n'.join(allowed_names) + "\r\n\n" +
                           f'<ins><b>Доступные быстрые команды командной строки:</b></ins>\n\n' + '\n'.join(
                               allowed_command_names),

                           reply_markup=keybroad.keyboard_client, parse_mode=types.ParseMode.HTML)
