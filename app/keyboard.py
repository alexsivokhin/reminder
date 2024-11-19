from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Помни'),
				      KeyboardButton(text='Что я помню'),
				      KeyboardButton(text='Вспомнить всё')]],
			   resize_keyboard=True)
