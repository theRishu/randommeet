from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

setting_choice = InlineKeyboardMarkup(row_width=1)

gender = InlineKeyboardButton(text="🧔 Gender 👩", callback_data="gender")
setting_choice.insert(gender)


partgend = InlineKeyboardButton(text="🧔 Partner Gender 👩", callback_data="partgen")
setting_choice.insert(partgend)


vip = InlineKeyboardButton(text="🌟 VIP", callback_data="vip")
setting_choice.insert(vip)
"""
age = InlineKeyboardButton(
    text="📆 Age", callback_data="age")
setting_choice.insert(age)
rating = InlineKeyboardButton(
    text="Check your rating", callback_data="show_rating")
setting_choice.insert(rating)
"""
