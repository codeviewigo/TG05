from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from forms.states import FinanceForm
from database.sqlt import update_user

router = Router()


@router.message(F.text == 'Личные финансы')
async def cmd_finance(message: Message, state: FSMContext):
    await state.set_state(FinanceForm.category1)
    await message.answer('Укажите первую категорию расходов:')


@router.message(FinanceForm.category1)
async def form_category1(message: Message, state: FSMContext):
    await state.update_data(category1=message.text)
    await state.set_state(FinanceForm.expenses1)
    await message.answer(f'Введите сумму расходов для {message.text}')


@router.message(FinanceForm.expenses1)
async def form_expenses1(message: Message, state: FSMContext):
    await state.update_data(expenses1=float(message.text))
    await state.set_state(FinanceForm.category2)
    await message.answer(f'Укажите вторую категорию расходов:')


@router.message(FinanceForm.category2)
async def form_category2(message: Message, state: FSMContext):
    await state.update_data(category2=message.text)
    await state.set_state(FinanceForm.expenses2)
    await message.answer(f'Введите сумму расходов для {message.text}')


@router.message(FinanceForm.expenses2)
async def form_expenses2(message: Message, state: FSMContext):
    await state.update_data(expenses2=float(message.text))
    await state.set_state(FinanceForm.category3)
    await message.answer(f'Укажите третью категорию расходов:')


@router.message(FinanceForm.category3)
async def form_category3(message: Message, state: FSMContext):
    await state.update_data(category3=message.text)
    await state.set_state(FinanceForm.expenses3)
    await message.answer(f'Введите сумму расходов для {message.text}')


@router.message(FinanceForm.expenses3)
async def form_expenses3(message: Message, state: FSMContext):
    await state.update_data(expenses3=float(message.text))

    data = await state.get_data()
    await state.clear()

    update_user(
        message.from_user.id,
        data['category1'],
        data['expenses1'],
        data['category2'],
        data['expenses2'],
        data['category3'],
        data['expenses3']
    )

    await message.answer('Ваши личные финансы обновлены')
