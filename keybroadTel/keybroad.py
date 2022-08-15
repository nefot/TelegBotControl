from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_client = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/клик'),KeyboardButton(text='/команды')],
        [KeyboardButton(text='/c dir'), KeyboardButton(text='/фото'),
         KeyboardButton(text='/текст'), KeyboardButton(text='/c cd ..'), KeyboardButton(text='/меню')],
        [KeyboardButton(text='/выйти из системы')]
    ],
    resize_keyboard=True
)


menu_dir = ReplyKeyboardMarkup(

    keyboard=[
        [KeyboardButton(text='/кирилл'), KeyboardButton(text='/артем'), KeyboardButton(text='/программы'),
         KeyboardButton(text='/назад')]
    ]
)
