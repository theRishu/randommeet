from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


partgen_keyboard = InlineKeyboardMarkup(row_width=3)

partner_male_button = InlineKeyboardButton(text="🧔", callback_data="B")
partgen_keyboard.insert(partner_male_button)

partner_female_button = InlineKeyboardButton(text="👩", callback_data="G")
partgen_keyboard.insert(partner_female_button)

partner_anon_button = InlineKeyboardButton(text="👩🗣🧔", callback_data="AL")
partgen_keyboard.insert(partner_anon_button)
