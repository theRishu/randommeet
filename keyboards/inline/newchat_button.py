from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


NEWCHAT_BUTTON = InlineKeyboardMarkup(row_width=1)

newchat_button = InlineKeyboardButton(
    text="💬 New Chat", callback_data="newchat")
NEWCHAT_BUTTON.insert(newchat_button)