import random

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from keyboards import builders as bl, reply
from api.nasa import get_random_apod
from api.languages import translate_text
from api.currency import get_currency
from database.sqlt import get_user, add_user, get_users

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\n'
                         'Я Ваш личный помощник. Выберите одну из команд в меню.', reply_markup=reply.main)


@router.message(Command('random_apod'))
async def cmd_random_apod(message: Message):
    apod = get_random_apod()
    if apod:
        title = translate_text(apod['title'])
        photo_url = apod['url']
        await message.answer_photo(photo_url, caption=title)
    else:
        await message.answer('Не удалось получить фото от NASA')


@router.message(F.text == 'Регистрация')
async def cmd_registration(message: Message):
    user = get_user(message.from_user.id)
    if user:
        await message.answer('Вы уже зарегистрированы')
    else:
        add_user(message.from_user.id, message.from_user.full_name)
        await message.answer('Спасибо за регистрацию!')


@router.message(F.text == 'Курс валют')
async def cmd_currency(message: Message):
    currency = get_currency()
    usd_to_rub = currency["conversion_rates"]["RUB"]
    usd_to_eur = currency["conversion_rates"]["EUR"]
    eur_to_rub = usd_to_eur * usd_to_rub

    if currency:
        await message.answer(f'1 USD = {usd_to_rub:.2f} RUB\n'
                             f'1 USD = {usd_to_eur:.2f} EUR\n'
                             f'1 EUR = {eur_to_rub:.2f} RUB')
    else:
        await message.answer('Не удалось получить курс валюты')


@router.message(F.text == 'Советы по экономии')
async def cmd_tips(message: Message):
    tips = [
        'Создайте бюджет: Разработайте ежемесячный бюджет, чтобы отслеживать доходы и расходы. Это поможет вам понять, на что уходят деньги и где можно сократить затраты.',
        'Откладывайте деньги: Старайтесь откладывать хотя бы 10% от каждого дохода на сберегательный счёт или в инвестиции. Это поможет создать финансовую подушку безопасности',
        'Избегайте импульсивных покупок: Перед покупкой задавайте себе вопрос, действительно ли это необходимо. Дайте себе время подумать, прежде чем совершить покупку.',
        'Сравнивайте цены: Перед покупкой товаров или услуг сравнивайте цены в разных магазинах и онлайн-платформах. Это поможет найти наиболее выгодные предложения.',
        'Используйте скидки и акции: Воспользуйтесь возможностью сэкономить на скидках, распродажах и акциях. Подпишитесь на рассылки от любимых магазинов, чтобы быть в курсе специальных предложений.'
    ]
    tip = random.choice(tips)
    await message.answer(tip)


# @router.message(Command('users'))
# async def cmd_get_users(message: Message):
#     users = get_users()
#
#     if users:
#         users_list = "\n".join(
#             [f"ID: {user['id']}, "
#              f"Телеграм ID: {user['tg_id']},"
#              f"Категория 1: {user['category1']}, "
#              f"Расходы 1: {user['expenses1']}, "
#              f"Категория 2: {user['category2']}, "
#              f"Расходы 2: {user['expenses2']}, "
#              f"Категория 3: {user['category3']}, "
#              f"Расходы 3: {user['expenses3']}, " for user in users])
#         await message.reply(f"Список пользователей:\n{users_list}")
#     else:
#         await message.reply("Список пользователей пуст.")


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
