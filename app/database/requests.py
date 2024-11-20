from app.database.models import async_session
from app.database.models import User, Reminder
from sqlalchemy import select, update
from datetime import timedelta, datetime

async def set_user(tg_id, name):
	async with async_session() as session:
		user = await session.scalar(select(User).where(User.tg_id == tg_id))

		if not user:
			session.add(User(tg_id=tg_id, name=name))
			await session.commit()

async def get_reminder(tg_id):
	async with async_session() as session:
		user_id = await session.scalar(select(User.id).where(User.tg_id == tg_id))
		check_reminder = await session.scalar(select(Reminder.reminder).where(Reminder.user_id == user_id))
		if check_reminder:
			result = await session.scalars(select(Reminder).where(Reminder.user_id == user_id))
			return  result
		else:
			return "Мне еще нечего помнить"

async def set_reminder(time, reminder, tg_id):
	async with async_session() as session:
		user_id = await session.scalar(select(User.id).where(User.tg_id == tg_id))
		session.add(Reminder(time=time, reminder=reminder, user_id=user_id))
		await session.commit()

async def get_time(current_time):
	async with async_session() as session:
		reminders = await session.scalars(select(Reminder).where((Reminder.time - current_time) < timedelta(minutes=30)))
		rya = datetime.strptime('2024-11-20 21:00:00', "%Y-%m-%d %H:%M:%S")
		test = rya - current_time
		if test < timedelta(minutes=30):
			print (f"{test}")
#		user_id = await session.scalar(select(User.id).where(User.tg_id == tg_id))
#		await session.commit()
		return reminders
