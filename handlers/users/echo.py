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

    if user.state == "C":
        match = await db.select_user(user.partner_id)
        if user.partner_id == match.user_id and user.user_id == match.partner_id:
            try:
                if message.reply_to_message is None:
                    await bot.send_message(user.partner_id, message.text)
                elif message.from_user.id != message.reply_to_message.from_user.id:
                    await bot.send_message(
                        user.partner_id,
                        reply_to_message_id=message.reply_to_message.message_id - 1,
                    )
                elif message.from_user == message.reply_to_message.from_user.id:
                    await bot.send_message(
                        user.partner_id,
                        reply_to_message_id=message.reply_to_message.message_id + 1,
                    )
                else:
                    print("chutiyapa")
                    await bot.send_message(user.partner_id, message.text)

                # message.from_user.id == message.reply_to_message.from_user.id:

            except BotBlocked:
                await db.update_after_leavechat(user.user_id, user.partner_id)
                await db.update_after_leavechat(user.partner_id, user.user_id)
                await bot.send_message(
                    user.user_id, constant.PARTNER_LEAVED, reply_markup=keyboard_markup
                )
                await db.delete_user(user.partner_id)

        else:
            pass

    elif user.state == "A":
        await message.answer(constant.NOT_MATCHED, reply_markup=keyboard_markup)
    elif user.state == "B":
        await message.answer(constant.NOT_MATCHED, reply_markup=stop_search)
    elif user.state == "D":
        await message.answer(constant.YOU_ARE_BANNED)
    elif user.state == "L":
        await message.answer(constant.NOT_MATCHED)

    else:
        pass

        
