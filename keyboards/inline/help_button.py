from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import help_callback

choice = InlineKeyboardMarkup(row_width=2)


command = InlineKeyboardButton(text="Commands ❓ ", callback_data="commands")
choice.insert(command)

bot_info = InlineKeyboardButton(text="Bot Info ℹ️ ", callback_data="bot_info")
choice.insert(bot_info)

feedback_button = InlineKeyboardButton(
    text="Send a feedback ", callback_data="feedback"
)
choice.insert(feedback_button)

cancel_button = InlineKeyboardButton(text="Cancel ❌", callback_data="cancel")
choice.insert(cancel_button)


back_keyboard = InlineKeyboardMarkup(row_width=2)

back_button = InlineKeyboardButton(text="🔙 Back", callback_data="back")
back_keyboard.insert(back_button)
