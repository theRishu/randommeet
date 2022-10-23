from aiogram import types
from loader import dp
import constant
from keyboards.inline.delete_profile_button import delete_profile_markup

from utils.misc import db_commands as db


@dp.message_handler(commands="deleteprofile")
async def deleteprofife(message: types.Message):
    user = await db.select_user(message.from_user.id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return
    if user.state == "B":
        await message.answer("You are searching for user. Please stop searching first.")
    elif user.state == "C":
        await message.answer(
            "You are middle in chat. First finish talking then you can only delete your proile."
        )
    elif user.state == "A":
        await message.answer(
            constant.DELETEPROFILETEXT, reply_markup=delete_profile_markup
        )
    elif user.state == "D":
        await message.answer(constant.YOU_ARE_BANNED)

    else:
        pass


@dp.message_handler(text=(constant.DPYES))
async def deleteprofileyes(message: types.Message):
    user = await db.select_user(message.from_user.id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.state == "A":
        await db.delete_user(message.from_user.id)
        await message.answer(
            "We lost  most valuable diamond from our tresures.\nWe are really sorry that we dont meet your expectation.\nIn case if you wanna use this bot again you just need to send /start again.",
            reply_markup=types.ReplyKeyboardRemove(),
        )
    elif user.state == "D":
        await message.answer(
            "If you are such smart you had never got ban!(Insert here some slang)"
        )

    else:
        pass


@dp.message_handler(text=(constant.DPNO))
async def deleteprofileno(message: types.Message):
    user = await db.select_user(message.from_user.id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.state == 'A':
        await message.answer("We respect your choice for not deleting proile. Hope we will fulfill your expectation.", reply_markup=keyboard_markup)

    else:
        await message.answer("This features in not usable now")
