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


@dp.message_handler(text=(constant.TOD))
@dp.message_handler(commands=["play"])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return
    if user.state == "A":
        await message.answer(constant.NOT_MATCHED)
    elif user.state == "B":
        await message.answer(constant.NOT_MATCHED)
    elif user.state == "C":
        match = await db.select_user(user.partner_id)
        if user.partner_id == match.user_id:
            await bot.send_message(
                user.user_id,
                "You selected to play truth or dare game.\nWe are updating your keyboard for better experience.",
                reply_markup=tod_markup,
            )

    await bot.delete_message(user_id, message.message_id)


@dp.message_handler(text=(constant.T))
@dp.message_handler(commands=["truth"])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.state == "A":
        await message.answer(constant.NOT_MATCHED)
    elif user.state == "B":
        await message.answer(constant.NOT_MATCHED)
    elif user.state == "C":
        match = await db.select_user(user.partner_id)
        whattruth = random.choice(truthlist)
        if user.partner_id == match.user_id and user.user_id == match.partner_id:
            await bot.send_message(user.user_id, f"Bot: For Partner\n{whattruth}")
            await bot.send_message(user.partner_id, f"Bot: For Parner\n{whattruth}")
    await bot.delete_message(user_id, message.message_id)


@dp.message_handler(text=(constant.D))
@dp.message_handler(commands=["dare"])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)

    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.state == "A":
        await message.answer(constant.NOT_MATCHED)
    elif user.state == "B":
        await message.answer(constant.NOT_MATCHED)
    elif user.state == "C":
        match = await db.select_user(user.partner_id)
        whatdare = random.choice(darelist)
        if user.partner_id == match.user_id and user.user_id == match.partner_id:
            await bot.send_message(user.user_id, f"Bot: For Partner \n{whatdare}")
            await bot.send_message(user.partner_id, f"Bot: For You\n{whatdare}")
    await bot.delete_message(user_id, message.message_id)


@dp.message_handler(text=("HTC"))
async def htc(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)

    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.state == "A":
        await message.answer(constant.NOT_MATCHED)
    elif user.state == "B":
        await message.answer(constant.NOT_MATCHED)
    elif user.state == "C":
        match = await db.select_user(user.partner_id)
        if user.partner_id == match.user_id and user.user_id == match.partner_id:
            await bot.send_message(user.user_id, f"HOW TO CHAT")
            await bot.send_message(user.partner_id, f"Bot: For You\n{whatdare}")
    await bot.delete_message(user_id, message.message_id)


@dp.message_handler(text=(constant.M))
@dp.message_handler(commands=["mix"])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)

    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.state == "A":
        await message.answer(constant.NOT_MATCHED)
    elif user.state == "B":
        await message.answer(constant.NOT_MATCHED)
    elif user.state == "C":
        match = await db.select_user(user.partner_id)
        mixlist = [
            "Bot: Let me decide for you .. \nWow your got /truth. Please dont be liar.",
            "Bot: Let me decide for you .. \nWow you got /dare. Please be ready.",
        ]

        whatmix = random.choice(mixlist)
        if user.partner_id == match.user_id and user.user_id == match.partner_id:
            await bot.send_message(user.user_id, whatmix)
            await bot.send_message(user.partner_id, whatmix)
    await bot.delete_message(user_id, message.message_id)


@dp.message_handler(text=(constant.CR))
@dp.message_handler(commands=["clear"])
async def send_clrk(message: types.Message):
    user_id = message.from_user.id
    await message.answer("Cleared.", reply_markup=types.ReplyKeyboardRemove())
    await bot.delete_message(user_id, message.message_id)
    await bot.delete_message(user_id, message.message_id + 1)


@dp.message_handler(text=(constant.BNC))
async def deleteprofileyesno(message: types.Message):
    user = await db.select_user(message.from_user.id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.state == "C":
        await message.answer("TOD button Closed", reply_markup=in_chat_markup)
    else:
        await message.answer(constant.NOT_MATCHED)


@dp.message_handler(commands=["stats"])
async def send_welcome(message: types.Message):
    stmt1 = select(User)
    userlist = []
    async with async_session() as session:
        result = await session.execute(stmt1)
        for user in result.scalars():
            userlist.append(user.user_id)

    stmt2 = select(User).where(User.gender == "NA")
    nalist = []
    async with async_session() as session:
        result = await session.execute(stmt2)
        for user in result.scalars():
            nalist.append(user.user_id)

    stmt3 = select(User).where(User.gender == "M")
    mlist = []
    async with async_session() as session:
        result = await session.execute(stmt3)
        for user in result.scalars():
            mlist.append(user.user_id)

    stmt4 = select(User).where(User.gender == "F")
    flist = []
    async with async_session() as session:
        result = await session.execute(stmt4)
        for user in result.scalars():
            flist.append(user.user_id)

    f = len(flist)
    m = len(mlist)
    n = len(nalist)
    u = len(userlist)
    t = len(truthlist)
    d = len(darelist)
    msg = f"**Total user:  {u}**\nTotal Male:  {m}\nTotal Female:  {f}\nTotal NA:  {n}\nTotal Truth:  {t}\nTotal Dare:  {d}"
    await message.reply(msg, parse_mode="MARKDOWN")


@dp.message_handler(commands=("tos"))
async def tos(message: types.Message):
    await message.answer(constant.TOS)

