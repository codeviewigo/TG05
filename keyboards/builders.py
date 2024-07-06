from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

options = [
    {'Новосибирск': 'weather_nsk'},
    {'Москва': 'weather_msk'},
    {'Санкт-Петербург': 'weather_spb'}
]


async def weather_kb():
    keyboard = InlineKeyboardBuilder()
    for option in options:
        for key, value in option.items():
            keyboard.add(InlineKeyboardButton(text=key, callback_data=value))
    return keyboard.adjust(2).as_markup()
