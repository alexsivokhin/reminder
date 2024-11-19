from sqlalchemy import BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

import os
from dotenv import load_dotenv

load_dotenv()
engine = create_async_engine(url=os.getenv('SQLALCHEMY_URL'))

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
	pass

class User(Base):
	__tablename__ = 'users'

	id: Mapped[int] = mapped_column(primary_key=True)
	tg_id = mapped_column(BigInteger)
	name: Mapped[str] = mapped_column(String(50))

class Reminder(Base):
	__tablename__ = 'reminders'

	id: Mapped[int] = mapped_column(primary_key=True)
	time: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
	reminder: Mapped[str] = mapped_column(String(100))
	user_id = mapped_column(ForeignKey('users.id'))

async def async_main():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
