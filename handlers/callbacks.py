from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import builders as bl
from api.weather import get_weather

router = Router()


@router.callback_query(F.data.in_(['weather_nsk', 'weather_msk', 'weather_spb']))
async def callback_show_more(callback: CallbackQuery):
    if callback.data == 'weather_nsk':
        city = 'Новосибирск'
    elif callback.data == 'weather_msk':
        city = 'Москва'
    else:
        city = 'Санкт-Петербург'

    weather_info = get_weather(city)

    weather_message = (
        f"Температура: {weather_info['temperature']}°C\n"
        f"Ощущается как: {weather_info['feels_like']}°C\n"
        f"Описание: {weather_info['weather']}\n"
        f"Влажность: {weather_info['humidity']}%\n"
        f"Давление: {weather_info['pressure']} hPa\n"
        f"Скорость ветра: {weather_info['wind_speed']} м/с\n"
        f"Направление ветра: {weather_info['wind_deg']}°"
    )

    await callback.message.edit_text(
        f'Погода в городе {city}:\n\n{weather_message}',
        reply_markup=await bl.weather_kb()
    )
