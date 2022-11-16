
from loader import dp, bot
import constant
from aiogram import types
from utils.misc import db_commands as db
from aiogram.types import CallbackQuery, ContentType, Message, reply_keyboard
from keyboards.inline.reaccept_button.reaccept_cancel import cancel_button
from keyboards.inline.reaccept_button.reopen_button import reopen_keyboard
from keyboards.inline.stop_searching import stop_search



FC = '-846814382'

@dp.message_handler(commands="report"):
async def report(message: types.Message):
    

    
