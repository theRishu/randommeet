from aiogram.types import ContentType
from loader import dp, bot
from aiogram import types
from utils.misc import db_commands as db
import constant


@dp.message_handler(content_types=ContentType.AUDIO)
async def audio(message: types.Message):
    user_id = message.from_user.id

    user = await db.select_user(user_id)
    if not user:
        return

    if user.state == 'A':
        await message.answer(constant.NOT_MATCHED)
    elif user.state == 'B':
        await message.answer(constant.NOT_MATCHED)
    elif user.state == 'C':
        await bot.send_audio(user.partner_id, message.audio.file_id, caption=message.caption)
    else:
        pass