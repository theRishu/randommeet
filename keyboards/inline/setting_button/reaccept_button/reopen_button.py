from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

accept_keyboard = InlineKeyboardMarkup(row_width=2)

cancel_button = InlineKeyboardButton(text=" Cancel ", callback_data="cancel")
accept_keyboard.insert(cancel_button)
