from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

gender_keyboard = InlineKeyboardMarkup(row_width=3)

male_button = InlineKeyboardButton(text="🧔", callback_data="M")
gender_keyboard.insert(male_button)

female_button = InlineKeyboardButton(text="👩", callback_data="F")
gender_keyboard.insert(female_button)

anon_button = InlineKeyboardButton(text="👩🧔", callback_data="NA")
gender_keyboard.insert(anon_button)

back_to_setting_button = InlineKeyboardButton(
    text="🔙 Back", callback_data="bts")
gender_keyboard.insert(back_to_setting_button)
