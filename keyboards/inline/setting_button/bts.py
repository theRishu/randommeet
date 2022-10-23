from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bts_keyboard= InlineKeyboardMarkup(row_width=1)

bts_button = InlineKeyboardButton(text="🔙 Back", callback_data="bts")
bts_keyboard.insert(bts_button)