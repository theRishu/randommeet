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

from utils.db_api.models import User
from utils.misc import db_commands as db


@dp.message_handler(text=(constant.ST))
@dp.message_handler(Command("settings"))
async def show_setting(message):
    user_id = message.from_user.id
    result = await db.select_user(user_id)
    if result is None:
        await db.add_user(user_id)
        await message.answer(text=" Settings: ", reply_markup=setting_choice)
        return

    elif result.total_referral > 2 and result.is_vip == False:
        await db.makevip(result.user_id)
        await message.answer(
            "Congratulations!🥳 You got a VIP user status now. You need to send /settings command again."
        )

    else:

        await message.answer(text=" Settings: ", reply_markup=setting_choice)


@dp.callback_query_handler(text_contains="age")
async def show_age_buttons(call: CallbackQuery):
    await call.message.edit_text("For choosing your age. Please send /setage:")
    await call.message.edit_reply_markup(reply_markup=bts_keyboard)


@dp.callback_query_handler(text_contains="gender")
async def show_gender_buttons(call: CallbackQuery):
    await call.message.edit_text("Choose your gender:")
    await call.message.edit_reply_markup(reply_markup=gender_keyboard)


@dp.callback_query_handler(text_contains="M")
@dp.callback_query_handler(text_contains="F")
@dp.callback_query_handler(text_contains="NA")
async def set_gender(call: CallbackQuery):
    gender_data = call.data
    user_id = call.from_user.id
    if gender_data == "M":
        await call.message.edit_text("Your selected gender:\nMale")
        await call.message.edit_reply_markup(reply_markup=bts_keyboard)
        await db.update_gender(user_id, gender_data)
    elif gender_data == "F":
        await call.message.edit_text("Your selected gender:\nFemale")
        await call.message.edit_reply_markup(reply_markup=bts_keyboard)
        await db.update_gender(user_id, gender_data)
    else:
        await call.message.edit_text("Your gender was selected to anon.")
        await call.message.edit_reply_markup(reply_markup=bts_keyboard)
        await db.update_gender(user_id, "NA")
        await db.update_partner_gender(user_id, "NA")


@dp.callback_query_handler(text_contains="partgen")
async def show_partner_gender_buttons(call: CallbackQuery):
    user_id = call.from_user.id
    user = await db.select_user(user_id)

    if user.is_vip is True:
        if user.gender == "NA":
            await call.message.edit_text(
                "You need to first select your gender to male or female."
            )
            await call.message.edit_reply_markup(reply_markup=bts_keyboard)
        else:
            await call.message.edit_text("Choose your partner gender:")
            await call.message.edit_reply_markup(reply_markup=partgen_keyboard)
    else:
        await call.answer("Only VIP user can select partner gender!", show_alert=True)
        #await call.message.edit_reply_markup(reply_markup=setting_choice)


@dp.callback_query_handler(text_contains="B")
@dp.callback_query_handler(text_contains="G")
@dp.callback_query_handler(text_contains="AL")
async def set_partner_gender(call: CallbackQuery):

    partgen_data = call.data
    user_id = call.from_user.id
    if partgen_data == "B":
        await call.message.edit_text("Your partner gender will be: \nMale")
        await call.message.edit_reply_markup(reply_markup=bts_keyboard)
        await db.update_partner_gender(user_id, "M")
    if partgen_data == "G":
        await call.message.edit_text("Your partner gender will be :\nFemale")
        await call.message.edit_reply_markup(reply_markup=bts_keyboard)
        await db.update_partner_gender(user_id, "F")
    elif partgen_data == "AL":
        await call.message.edit_text("Your partner gender will be random.")
        await call.message.edit_reply_markup(reply_markup=bts_keyboard)
        await db.update_partner_gender(user_id, "NA")


@dp.callback_query_handler(text_contains="age")
async def set_age(call: CallbackQuery):
    await call.message.edit_text("Tell us your age")


@dp.callback_query_handler(text_contains="bts")
async def will_show_setting_option(call: CallbackQuery):
    await call.message.edit_text("Settings:")
    await call.message.edit_reply_markup(reply_markup=setting_choice)


@dp.callback_query_handler(text_contains="vip")
async def set_age(call: types.CallbackQuery):
    user = await db.select_user(call.from_user.id)
    user_id = call.from_user.id
    if user.total_referral > 2:
        await db.makevip(user.user_id)

    bot_username = (await bot.me).username

    if user.is_vip is True:
        await call.message.edit_text(
            "Congratulations! 🥳 You are a VIP user! \nYou can freely choose your partner gender."
        )
        await call.message.edit_reply_markup(reply_markup=bts_keyboard)

    else:
        await call.message.edit_text(
            f"""
To unlock the VIP license you have 2 ways:
1) You can invite users.
Everytime 3 users start this bot using your referral link you will get an  30 days duration VIP license and it will reset after last day of month.
These users should never have started the bot before.
You have to invite minimum 3 user to unlock vip.
Your link: https://t.me/{bot_username}?start={user_id}
2) You can buy.
For Indian user  100 INR
FOR International user  2.99 USD
Duration 365 days.
For buying VIP contact @RandomMode_bot
""",
            disable_web_page_preview=True,
        )
        await call.message.edit_reply_markup(reply_markup=bts_keyboard)
