from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Помни'),
				      KeyboardButton(text='Что я помню')]],
			   resize_keyboard=True)
