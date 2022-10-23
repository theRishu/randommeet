

from multiprocessing.resource_sharer import stop
import constant
from aiogram import types 

button = types.KeyboardButton(constant.SS)
stop_search = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button)