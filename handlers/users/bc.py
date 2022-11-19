from aiogram import types
from sqlalchemy import select
from loader import dp, bot
from utils.db_api.db import async_session
from utils.db_api.models import User
from utils.misc import db_commands as db
from aiogram.utils.exceptions import BotBlocked


async def check(user_id):
    result = await bot.get_chat_member("@RandomMode", user_id)

    if result["status"] in ["member", "creator", "administrator"]:

        return True
    else:
        return False


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

    else:
        await message.answer("You are not admin.")
