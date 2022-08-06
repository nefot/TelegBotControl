from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_client = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/click'), KeyboardButton(text='/shut')],
        [KeyboardButton(text='/kill'), KeyboardButton(text='/c dir'), KeyboardButton(text='/foto'),
         KeyboardButton(text='/text' ), KeyboardButton(text='/c cd ..'),KeyboardButton(text='/menu_dir' )]
    ],
    resize_keyboard=True
)
menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/exists'), KeyboardButton(text='/shutdown'), KeyboardButton(text='/undo')]
    ],
    resize_keyboard=True
)

menu_dir = ReplyKeyboardMarkup(

    keyboard=[
        [KeyboardButton(text='/кирилл '),KeyboardButton(text='/артем '),KeyboardButton(text='/программы '),
         KeyboardButton(text='/назад ')]
    ]
)


admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/temp'), KeyboardButton(text='/alert')]
    ],
    resize_keyboard=True

)
