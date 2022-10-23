from loader import dp, bot

import constant

from aiogram import types

from utils.misc import db_commands as db
from aiogram.types import CallbackQuery, ContentType, Message, reply_keyboard
from keyboards.inline.reaccept_button.reaccept_cancel import cancel_button
from keyboards.inline.reaccept_button.reopen_button import reopen_keyboard
from keyboards.inline.stop_searching import stop_search
from data.config import BROADCAST_CHANNEL as BC


@dp.message_handler(commands="reopen")
async def send_welcome(message: types.Message):
    user_id = message.from_user.id

    user = await db.select_user(user_id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    try:
        if user.state == "A":
            if user.last_partner_id != None:
                await message.answer(
                    text=constant.WAIT_REACCEPT, reply_markup=cancel_button
                )
                try:
                    await bot.send_message(
                        user.last_partner_id,
                        constant.PARTNER_REQUESTED,
                        reply_markup=reopen_keyboard,
                    )

                    await db.update_ro_id(user.last_partner_id, user.user_id)
                    await bot.send_message(
                        user.user_id,
                        "The request to reopen chat was successfully send. Please wait ",
                        reply_markup=stop_search,
                    )
                    await db.update_state(user.user_id, "L")
                except Exception as e:
                    await message.answer(str(e))
            elif user.last_partner == 0:
                await message.answer(text=constant.NO_PREVIOUS_PARTNER)

            else:
                await message.answer("3")

        elif user.state == "B":
            await message.answer(text=constant.CANT_SEND_REACCEPT_REQUEST)

        elif user.state == "C":
            await message.answer(constant.CANT_SEND_REACCEPT_REQUEST)
            await db.update_ro_id(user.last_partner_id, user.user_id)

        elif user.state == "D":
            await message.answer(constant.YOU_ARE_BANNED)

        else:
            await message.answer(constant.ALREADY_REACCEPT, reply_markup=cancel_button)

    except Exception as e:
        await bot.send_message(BC, f"Exception at REOPEN {str(e)}")


@dp.callback_query_handler(text_contains="rno")
async def show_age_buttons(call: CallbackQuery):
    await call.message.edit_text("You declined to reopen chat.")
    user = await db.select_user(call.from_user.id)
    match = await db.select_user(user.ro_id)
    try:
        if match.state == "A" and match.ro_id != None:
            await bot.message(user.ro_id, "Your partner declined the reopen request.")
            await db.update_ro_id(match.user_id, None)
        else:
            pass

    except Exception as e:
        await bot.send_message(BC, f"Exception at RNO {str(e)}")


@dp.callback_query_handler(text_contains="ryes")
async def show_age_buttons(call: CallbackQuery):
    await call.message.edit_text("You accepted to reopen the chat.")
    user = await db.select_user(call.from_user.id)
    match = await db.select_user(user.ro_id)
    try:
        if match.state == "A" and match.ro_id != None:
            await bot.message(user.ro_id, "Your partner declined the reopen request.")
            await db.update_ro_id(match.user_id, None)
        else:
            pass
    except Exception as e:
        await bot.send_message(BC, f"Exception at RNO {str(e)}")


@dp.callback_query_handler(text_contains="stoprequest")
async def show_age_buttons(call: CallbackQuery):
    await call.message.edit_text("Operation cancelled")
    user = db.select_user(call.from_user.id)
    await  db.update_after_stop_request(user.user_id , user.last_partner_id)
    
    