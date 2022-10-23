import constant
from aiogram import types


delete_profile_markup = types.ReplyKeyboardMarkup(
    one_time_keyboard=True, resize_keyboard=True, row_width=1
)
# default row_width is 3, so here we can omit it actually
# kept for clearness
btns_text = (constant.DPYES, constant.DPNO)
delete_profile_markup.row(*(types.KeyboardButton(text) for text in btns_text))
# adds buttons as a new row to the existing keyboard
# the behaviour doesn't depend on row_width attribute
