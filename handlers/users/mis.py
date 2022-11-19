"""
toprating -
broadcast
clear
spc -
rate -
getlink - 
shareprofile -
makevio

"""
from aiogram import types
from sqlalchemy import select
from utils.db_api.db import async_session
from utils.db_api.models import User
from utils.misc import db_commands as db

from loader import dp , bot
import constant


@dp.message_handler(commands="topratings")
async def show_to_rating(message: types.Message):
    sql = select(User).order_by(User.rating.desc()).limit(5)
    text_template = "List of 5 top ratings:\n\n{scores}"
    async with async_session() as session:
        top_ratings_request = await session.execute(sql)
        ratings = top_ratings_request.scalars()

    score_entries = [
        f"{index+1} <b>{item.rating}</b>" for index, item in enumerate(ratings)]
    score_entries_text = "\n".join(score_entries).replace(
        f"{message.from_user.id}", f"{message.from_user.id} (it's you!)")
    await message.answer(text_template.format(scores=score_entries_text), parse_mode="HTML")


@dp.message_handler(commands="getlink")
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    bot_username = (await bot.me).username

    await message.reply(
        f"{constant.SHARE_LINK}"
        f"Here is your invite link :\nhttps://t.me/{bot_username}?start={user_id}"
    )


@dp.message_handler(commands="rate")
async def cmd_start(message: types.Message):
    user = await db.select_user(message.chat.id)
    if not user:
        message.answer(":)")
        return
    if user.state == 'C':
        await db.update_rate(user.partner_id, 5)
        await db.update_rate(user.user_id, -2)
        await bot.send_message(
            user.user_id, "You gives someone +5 rating and your rating was decreased by -2")
        await bot.send_message(user.partner_id, "Partner gifted you +5 rating.")
    else:
        message.answer(constant.NOT_MATCHED)


@dp.message_handler(commands='spc')
async def spc(message: types.Message):
    user = await db.select_user(message.from_user.id)
    await message.answer(f"""
    \nID: {user.user_id}
    \ngender: {user.gender}
    \npartner_gender: {user.partner_gender}
    \nis_vip: {user.is_vip}
    \nage: {user.age}
    \ntotal_referral: {user.total_referral}
    \nrating: {user.rating}
    \ncountry:  {user.country}
    \ncode:  {user.code}
    \nstate:  {user.state}
    \npartner_id:  {user.partner_id}
    \nlast_partner_id:  {user.last_partner_id}
    """)

@dp.message_handler(commands="shareprofile")
async def shareusername(message: types.message):
    user_id = message.from_user.id
    result = await db.select_user(user_id)
    if not result:
        await message.answer(constant.NOT_REGISTERED)
        return
    if result.state == 'A':
        await message.answer(constant.NOT_MATCHED, reply_markup=NEWCHAT_BUTTON)
    elif result.state == 'B':
        await message.answer(constant.NOT_MATCHED, reply_markup=NEWCHAT_BUTTON)
    elif result.state == 'C':

        await bot.send_message(result.partner_id, f'You partner wanted to share their profile with you Here is their  [PROFILE LINK](tg://user?id={result.user_id})',  parse_mode="MARKDOWNV2")
        await bot.send_message(BC, f'#SHAREPROFILE \nThe #{message.from_user.full_name} shared his [PROFILE LINK](tg://user?id={result.user_id})',  parse_mode="MARKDOWN")
        await message.answer("You shared your profile link.")

@dp.message_handler(commands = "myratings")
async def myratings(message: types.Message):
    try:
        user = db.select_user(message.from_user.id)
        await message.answer(f'Your total ratings :**{user.rating}** \n{constant.GET_MORE_RATINGS}')

    except Exception as e:
        print(str(e))


@dp.message_handler(commands = "onlineuser")
async def myratings(message: types.Message):
    stmt = select(User).where(User.state == 'B')
    userlist = []
    async with async_session() as session:
        result = await session.execute(stmt)
        for user in result.scalars():
            userlist.append(user.user_id)
    await message.answer(str(userlist))
    
    
    
@dp.message_handler(commands="mv")
async def update_rate_by_admin(message: types.Message):
    id = int(message.text.split()[1])
    await db.makevip(id)
    await bot.send_message(id, "You are vip now.")
    await message.answer("Done Successfully.")
    
    
    
    
    
    
    
@dp.message_handler(commands="cgm")
async def cmd_start(message: types.Message):
    user = await db.select_user(message.chat.id)
    try:
        await db.update_gender(user.partner_id, 'M')
    except Exception as e:
        await  message.answer("Partner gender changed to M")



@dp.message_handler(commands="cgf")
async def cmd_start(message: types.Message):
    user = await db.select_user(message.chat.id)
    try:
        await db.update_gender(user.partner_id, 'F')
    except Exception as e:
        await  message.answer("Partner gender changed to F")


