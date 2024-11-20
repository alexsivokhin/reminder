import time
import logging
import asyncio
import os
import datetime

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.methods import SendMessage

import app.keyboard as kb
import app.database.requests as rq

#async def command_wir_handler(message: types.Message):
async def sender():
	current_time = datetime.datetime.now()
	reminders = await rq.get_time(current_time)
	for reminder in reminders:
#		await bot.send_message()
		print (f"{reminder.time} {reminder.reminder}")
#        tg_id = message.from_user.id
#        remembers = await rq.get_reminder(tg_id)
#        if remembers!="Мне еще нечего помнить":
#                for remember in remembers:
#                        if remember.time > current_time:
#                                await message.answer(f"{remember.time} {remember.reminder}")
#        else:
#                await message.answer(f"{remembers}")


async def main():
	load_dotenv()
	bot = Bot(token=os.getenv('TOKEN'))
	await sender()
#        await dp.start_polling(bot)

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	asyncio.run(main())
