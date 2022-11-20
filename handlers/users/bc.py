from aiogram import types
from sqlalchemy import select
from loader import dp, bot
from utils.db_api.db import async_session
from utils.db_api.models import User
from utils.misc import db_commands as db
from aiogram.utils.exceptions import BotBlocked
from keyboards.inline.setting_button.self_gender import gender_keyboard

from aiogram.types import CallbackQuery, ContentType, Message, reply_keyboard
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

import constant
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup



from aiogram import types


async def check(user_id):
    result = await bot.get_chat_member("@RandomMode", user_id)
    if result["status"] in ["member", "creator", "administrator"]:
        return True
    else:
        return False




TG_CHANNEL =  'https://t.me/RandomMode'
BUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="👉Click here to join 👈" , url=TG_CHANNEL)],
        
])






@dp.message_handler(commands=("broadcast"))
async def broadcast(message: types.Message):
    if message.from_user.id == 1460123566 and message.text != "":
        BROADCAST_TEXT = message.text[10:]
        stmt = select(User)
        async with async_session() as session:
            result = await session.execute(stmt)
        for user in result.scalars():
            try:
                if user.state == "A":
                    
                    await bot.send_message(
                        user.user_id, f"🤖 Bot ( @RandomMode Broadcast) :{ BROADCAST_TEXT}"
                    )
                elif user.state == "B" or "C":
                    await bot.send_message(
                        user.user_id, f"🤖 Bot ( @RandomMode Broadcast) :{ BROADCAST_TEXT}"
                    )
                elif user.state == "D":
                    await bot.send_message(
                        user.user_id, f"🤖 Bot ( @RandomMode Broadcast) :{ BROADCAST_TEXT}"
                    )
                elif user.state == "E":
                    await db.delete_user(user.user_id)

                else:
                    pass

            except BotBlocked:
                await bot.send_message(1460123566, "Bot Blocked")
                await db.delete_user(user.user_id)
            except Exception as e:
                # await db.delete_user(user.user_id)
                await db.delete_user(user.user_id)

        await message.answer("Broadcast completed:")

    else:
        await message.answer("You are not admin.")

    




@dp.message_handler(commands=("gendercast"))
async def broadcast(message: types.Message):
    if message.from_user.id == 1460123566 :
        stmt = select(User)
        async with async_session() as session:
            result = await session.execute(stmt)
        for user in result.scalars():
            try:
                if user.gender == "M":
                    pass

                if user.gender =="F":
                    pass 

                if user.gender =='NA':
                    await bot.send_message(user.user_id, "Look like you have not selected the gender please Choose your gender:", reply_markup = gender_keyboard)

            except Exception as e:
                pass

        await message.answer('Gendercast Completed.')

    else:
        await message.answer("You are not admin")




@dp.message_handler(commands=('joinchannel'))
async def broadcast(message: types.Message):
    
    if message.from_user.id == 1460123566 :
        stmt = select(User)
        async with async_session() as session:
            result = await session.execute(stmt)
        for user in result.scalars():
            
            try:
                if await check(user.user_id) == False:
                    await bot.send_message(user.user_id , "📢 Please join our official channel." , reply_markup = BUTTON )
                else:
                    pass 

            except Exception as e:
                pass
        await message.answer('Joinchannel Broadcast Completed.')
        

