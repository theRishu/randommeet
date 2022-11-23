from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ask_for_perm = InlineKeyboardMarkup(row_width=2)


command = InlineKeyboardButton(text="Allow ✅ ", callback_data="allow")
ask_for_perm.insert(command)



cancel_button = InlineKeyboardButton(text="Deny ❌", callback_data="deny")
ask_for_perm.insert(cancel_button)


