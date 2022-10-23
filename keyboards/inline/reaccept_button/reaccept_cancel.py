from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cancel_button = InlineKeyboardMarkup(row_width=2)

button = InlineKeyboardButton(text="Cancel", callback_data="stoprequest")
cancel_button.insert(button)
