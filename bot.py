import time
import logging
import asyncio
import os

from datetime import datetime
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

import app.keyboard as kb
import app.database.requests as rq

from app.database.models import async_main

dp = Dispatcher()

class ChooseRem(StatesGroup):
	choose_reminder= State()
	choose_time = State()

@dp.message(CommandStart())
async def commmand_start_handler(message: types.Message):
	user_id = message.from_user.id
	user_name = message.from_user.first_name
	user_full_name = message.from_user.full_name

	await rq.set_user(user_id, user_name)
	logging.info(f'{user_id} {user_full_name} {time.asctime()}')
	await message.answer(f"Привет, {user_full_name}!", reply_markup=kb.main)


@dp.message(F.text == 'Помни')
async def command_memento_handler(message: types.Message, state: FSMContext):
	await message.answer('Что запомнить?')
	await state.set_state(ChooseRem.choose_reminder)

@dp.message(ChooseRem.choose_reminder, F.text)
async def chose_remind(message: types.Message, state: FSMContext):
	await state.update_data(choose_reminder=message.text.lower())
	await message.answer('Введите время в формате "YYYY-MM-DD HH:MM:SS"')
	await state.set_state(ChooseRem.choose_time)

@dp.message(ChooseRem.choose_time, F.text)
async def chose_time(message: types.Message, state: FSMContext):
	await state.update_data(choose_time=message.text)
	tg_id = message.from_user.id
	data = await state.get_data()
	time = await time_parser(data.get("choose_time"))

#	await message.answer(f'{data.get("choose_time")}, {data.get("choose_reminder")}, {tg_id}')
	await rq.set_reminder(time, data.get("choose_reminder"), tg_id)
	await message.answer('Принял')
	await state.clear()

@dp.message(F.text == 'Что я помню')
async def command_wir_handler(message: types.Message):
	tg_id = message.from_user.id
	remembers = await rq.get_reminder(tg_id)
	for remember in remembers:
		await message.answer(f"{remember.time} {remember.reminder}")

async def time_parser(dtime):
	result = datetime(2024, 8, 8, 15, 0, 0)
	return result

async def main():
	await async_main()
	load_dotenv()
	bot = Bot(token=os.getenv('TOKEN'))
	await dp.start_polling(bot)

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	asyncio.run(main())
