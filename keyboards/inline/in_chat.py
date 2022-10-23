
from aiogram import types
import constant
in_chat_markup = types.ReplyKeyboardMarkup(
    one_time_keyboard=False, resize_keyboard=True, row_width=2)
# default row_width is 3, so here we can omit it actually
# kept for clearness
btns_text = (constant.LC, constant.AC,)
in_chat_markup.row(*(types.KeyboardButton(text) for text in btns_text))
# adds buttons as a new row to the existing keyboard
# the behaviour doesn't depend on row_width attribute

more_btns_text = (
    constant.TOD,
    constant.HI,
    constant.CR
)
in_chat_markup.add(*(types.KeyboardButton(text)
                     for text in more_btns_text))
# adds buttons. New rows are formed according to row_width parameter