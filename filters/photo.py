from aiogram.types import ContentType
from loader import dp, bot
from aiogram import types
import constant
from keyboards.inline.ask_for_media import ask_for_perm

@dp.message_handler(content_types=ContentType.PHOTO)
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
        print(photo)
        if user.mperm == True:
            await bot.send_photo(user.partner_id, message.photo[-1].file_id , caption=message.caption)
        else:
            await message.answer("Your partner has disabled media.")
            await bot.send_message(user.partner_id ,constant.ASK_FOR_PERMISSION , reply_markup=ask_for_perm)
    else:
        pass

        
     
