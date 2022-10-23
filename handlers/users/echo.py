import asyncio

from keyboards.inline.delete_profile_button import delete_profile_markup
import random


import constant
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandStart
from aiogram.types import CallbackQuery, ContentType, Message, reply_keyboard
from aiogram.types.message import ParseMode
from aiogram.utils.exceptions import BotBlocked
from keyboards.inline.help_button import back_keyboard, choice
from keyboards.inline.newchat_button import NEWCHAT_BUTTON
from keyboards.inline.stop_searching import stop_search
from keyboards.inline.start_button import JOIN_BUTTON, keyboard_markup
from keyboards.inline.in_chat import in_chat_markup
from loader import bot, dp
from sqlalchemy import select
from utils.db_api.db import async_session
from utils.db_api.models import User
from utils.misc import db_commands as db
from utils.misc import search
from utils.tod.truth import truthlist
from utils.tod.dare import darelist
from data.config import BROADCAST_CHANNEL as BC



@dp.message_handler(content_types=ContentType.TEXT)
async def text(message: types.Message):

    user_id = message.from_user.id
    user = await db.select_user(user_id)

    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    
    if user.state == 'C':
        match = await db.select_user(user.partner_id)
        try:
            await bot.send_message(match.user_id, message.text)
        except BotBlocked:
            await db.delete_user(match)
        except Exception as e :
            await bot.send_message(BC , str(e))
    elif user.state == "A":
        await message.answer(constant.NOT_MATCHED, reply_markup=keyboard_markup)
    elif user.state == "B":
        await message.answer(constant.NOT_MATCHED , reply_markup=stop_search)
    elif user.state == "D":
        await message.answer(constant.YOU_ARE_BANNED)
    elif user.state == 'L':
        await message.answer(constant.NOT_MATCHED)

            



        