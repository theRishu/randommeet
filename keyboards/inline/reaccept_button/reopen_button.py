from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

reopen_keyboard = InlineKeyboardMarkup(row_width=2)

ryes_ = InlineKeyboardButton(text="Yes ", callback_data="ryes")

reopen_keyboard.insert(ryes_)

rno_ = InlineKeyboardButton(text="No", callback_data="rno")

reopen_keyboard.insert(rno_)
