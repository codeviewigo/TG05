from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from keyboards import builders as bl
from api.nasa import get_random_apod
from api.languages import translate_text

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')


@router.message(Command('random_apod'))
async def cmd_random_apod(message: Message):
    apod = get_random_apod()
    if apod:
        title = translate_text(apod['title'])
        photo_url = apod['url']
        await message.answer_photo(photo_url, caption=title)
    else:
        await message.answer('Не удалось получить фото от NASA')


@router.message(Command('weather'))
async def cmd_weather(message: Message):
    await message.answer('Выберите город:', reply_markup=await bl.weather_kb())


@router.message(Command('help'))
async def cmd_help(message: Message):
    help_message = 'Список команд:\n' \
                   '/start - начать диалог\n' \
                   '/help - список команд\n' \
                   '/random_apod - случайная фотография NASA\n' \
                   '/weather - погода в городе'

    await message.answer(help_message)
