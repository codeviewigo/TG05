from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Регистрация'),
            KeyboardButton(text='Курс валют')
        ],
        [
            KeyboardButton(text='Советы по экономии'),
            KeyboardButton(text='Личные финансы')
        ]
],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Воспользуйтесь клавиатурой для выбора...'
)