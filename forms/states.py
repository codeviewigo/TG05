from aiogram.fsm.state import StatesGroup, State


class FinanceForm(StatesGroup):
    category1 = State()
    expenses1 = State()
    category2 = State()
    expenses2 = State()
    category3 = State()
    expenses3 = State()
