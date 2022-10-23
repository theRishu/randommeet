from aiogram.types import ContentType
from loader import dp, bot
from aiogram import types
from utils.misc import db_commands as db
import constant


@dp.message_handler(content_types=ContentType.VIDEO)
async def video(message: types.Message):
    user_id = message.from_user.id

    user = await db.select_user(user_id)
    if not user:
        # await message.answer(constant.NOT_REGISTERED)
        return

    if user.state == 'A':
        await message.answer(constant.NOT_MATCHED)
    elif user.state == 'B':
        await message.answer(constant.NOT_MATCHED)
    elif user.state == 'C':
        await bot.send_video(user.partner_id, message.video.file_id, caption=message.caption)
    else:
        pass
