from aiogram import types
from loader import dp
from utils.misc import db_commands as db

from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

import constant
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



Refer_text = "\nRandomMeetBot \nTelegram Bot to chat anonymously with people around the whole world. \nJoin and lets make friends together"

@dp.message_handler(commands="vip")
async def another_ewchat(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)

    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.total_referral > 2:
        await db.makevip(user.user_id)



    if user.is_vip is True:
        await message.answer(
            "Congratulations! 🥳 You are a VIP user!\nYou can freely choose your partner gender from settings."
        )

    else:
    	MSG = f""" 
To get vip there is two way.
1) You can buy.
Cost per user  2.99 USD
Duration 365 days.
For buying VIP contact @RandomMode_bot

1) Share your invite link.
You have to invite minimum 3 user to unlock vip.
Duration 30 days.
Your link: https://t.me/Randommeetbot?start={user_id}



"""     
    	url = f'https://t.me/share/url?url=https://t.me/Randommeetbot?start={user_id}&text={Refer_text}'
    	studyboi = InlineKeyboardButton('🚀 Refer to your friend', url=url) 
    	SHARE = InlineKeyboardMarkup(resize_keyboard=True).add(studyboi)
    	await message.answer(MSG , reply_markup=SHARE , disable_web_page_preview=True)

















@dp.message_handler(commands="mperm")
async def another_ewchat(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)

    await message.answer(user.mperm)