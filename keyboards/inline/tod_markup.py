from aiogram import types
import constant
tod_markup = types.ReplyKeyboardMarkup(
    one_time_keyboard=False, resize_keyboard=True, row_width=3)
# default row_width is 3, so here we can omit it actually
# kept for clearness
btns_text = (constant.T, constant.D, constant.M)
tod_markup.row(*(types.KeyboardButton(text) for text in btns_text))
# adds buttons as a new row to the existing keyboard
# the behaviour doesn't depend on row_width attribute

more_btns_text = (constant.BNC)
tod_markup.add(types.KeyboardButton(more_btns_text))
# adds buttons. New rows are formed according to row_width parameter