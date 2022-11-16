import asyncio

from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.tod_markup import tod_markup
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
from keyboards.inline.setting_button.bts import bts_keyboard
from keyboards.inline.setting_button.partner_gender import partgen_keyboard
from keyboards.inline.setting_button.self_gender import gender_keyboard
from keyboards.inline.setting_button.setting_choice import setting_choice
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


@dp.message_handler(Command("ban"))
async def ban(message: types.Message):
    id = int(message.text.split()[1])
    reason1 = message.text.split()[2]
    reason2 = message.text.split()[3]

    user = await db.select_user(id)
    await db.update_after_leavechat(user.partner_id, user.user_id)
    try:
        await bot.send_message(user.partner_id, constant.PARTNER_LEAVED, reply_markup=keyboard_markup)
    except Exception as e:
        print(str(e))
    await db.update_state(id, 'D')
    await bot.send_message(id, f'You were banned from using bot cause of {reason1} {reason2} and disconnected  from chat .\nIf you think you were banned by mistake contact @RandomMode_bot', reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Banned Successfully.")
    
    
    
    

@dp.message_handler(Command("cban"))
async def ban(message: types.Message):
    user_id = message.from_user.id

    user = await db.select_user(user_id)

    await db.update_after_leavechat(user.partner_id, user.user_id)
    try:
        await bot.send_message(user_id, constant.PARTNER_LEAVED, reply_markup=keyboard_markup)
    except Exception as e:
        print(str(e))
    await db.update_state(user.partner_id,'D')
    await bot.send_message(id, f'You were banned from using bot cause of {reason1} {reason2} and disconnected  from chat.\nIf you think you were banned by mistake contact @RandomMode_bot', reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Banned Successfully.")


@dp.message_handler(Command("unban"))
async def ban(message: types.Message):
    id = int(message.text.split()[1])
    await db.update_state(id, 'A')
    await bot.send_message(id, f'You got a second chance. Please use it correctly')
    await message.answer("Unbanned Successfully.")

@dp.message_handler(Command("cp"))
async def update_rate_by_admin(message: types.Message):
    try:
       id = int(message.text.split()[1])
       desired_partner = int(message.text.split()[2])
       partner = await db.select_user(desired_partner)
       await db.update_after_leavechat(partner.partner_id, partner.user_id)
       await bot.send_message(partner.partner_id, constant.PARTNER_LEAVED, reply_markup=keyboard_markup)
       await db.update_after_match(desired_partner, id)

      
    except Exception as e:
        await bot.answer(str(e))
