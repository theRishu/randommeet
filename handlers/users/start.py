from logging import exception
import constant
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import bot, dp

from utils.misc import db_commands as db

from keyboards.inline.start_button import JOIN_BUTTON, keyboard_markup
from keyboards.inline.help_button import back_keyboard, choice
from keyboards.inline.stop_searching import stop_search
from keyboards.inline.in_chat import in_chat_markup

from utils.misc import search
from data.config import BROADCAST_CHANNEL as BC
from handlers.users.bc import BUTTON , check

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        result = await db.select_user(user_id)
        if not result:
            text = message.get_args()
            if text != "" and text.isdigit():
                code = int(message.get_args())
                await db.update_total_referral(code)
                await db.add_user(user_id)
                await message.answer(constant.START_TEXT, reply_markup=JOIN_BUTTON)
                await message.answer(constant.WELCOME, reply_markup=keyboard_markup)

                await bot.send_message(
                    BC, f"#WELCOME \nName: {message.from_user.full_name} \n ID : <code>{user_id} </code>"
                )
                try:
                    await bot.send_message(code, constant.JOINED_FROM_LINK)
                except Exception as e:
                    print(f"LINE 40 {str(e)}")
            else:
                await db.add_user(user_id)
                await message.answer(constant.WELCOME, reply_markup=keyboard_markup)
                await message.answer(constant.START_TEXT, )

                await bot.send_message(
                    BC, f"#WELCOME \nName : {message.from_user.full_name} \nID : <code>{user_id} </code>"
                )
        else:
            if result.state == "A":
                await message.answer(constant.START_TEXT, )
            if result.state == "B":
                await message.answer(constant.START_TEXT, )
            if result.state == "C":
                await message.answer(constant.START_TEXT, )
            if result.state == "D":
                await message.answer(constant.YOU_ARE_BANNED)

    except Exception as e:
        await bot.send_message(BC, f"WHOLE EXCEPTION ERROR IN NEWCHAT {str(e)}")


@dp.message_handler(text=constant.NC)
@dp.message_handler(commands="newchat")
async def new_chat(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.state in ["A", "E"]:
        if await check(user.user_id) == False:
                await bot.send_message(user.user_id , "Look like you had not joined the channel.Please join our official channel." , reply_markup = BUTTON )
                
        await bot.send_message(user.user_id, constant.WAITING, reply_markup=stop_search)
        await db.update_state(user.user_id, "B")

        found_user = await search.find_match_user(user_id)

        if found_user is not None:
            match = await db.select_user(found_user)
            try:
                await db.update_after_match(user_id, found_user)
                await bot.send_message(
                    found_user,
                    f"{constant.MATCHED}\nPartner Details\nRating: {user.rating}\nVIP user: {user.is_vip} \nGender: {user.gender}",
                    reply_markup=in_chat_markup,
                )

                await bot.send_message(
                    user_id,
                    f"{constant.MATCHED}\nPartner Details\nRating: {match.rating}\nVIP user: {match.is_vip} \nGender: {match.gender}",
                    reply_markup=in_chat_markup,
                )

               

            except Exception as e:
                await db.delete_user(found_user)
                await bot.send_message(BC, f"Error in next chat {str(e)}")
            return

    elif user.state == 'B':
        await message.answer(constant.AlREADY_WAITING, reply_markup=stop_search)

    elif user.state == "C":
        await message.answer(constant.IN_CHAT, reply_markup=in_chat_markup)

    else:
        pass


@dp.message_handler(text=(constant.LC))
@dp.message_handler(Command("leavechat"))
async def leavechat(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.state == "C":
        await db.update_after_leavechat(user.user_id, user.partner_id)
        await bot.send_message(
            user.user_id, constant.USER_LEAVED, reply_markup=keyboard_markup
        )
        try:
            await bot.send_message(
                user.partner_id, constant.PARTNER_LEAVED, reply_markup=keyboard_markup
            )
        except Exception as e:
            await bot.send_message(BC, str(e))

    elif user.state == "D":
        await message.answer(constant.YOU_ARE_BANNED)

    elif user.state == "L":
        pass

    elif user.state == "A":
        await message.answer(constant.NOT_MATCHED, reply_markup=keyboard_markup)
    else:

        await message.answer(constant.NOT_MATCHED, reply_markup=stop_search)


@dp.message_handler(Command("myprofile"))
async def show_profile(message: types.Message):
    user = await db.select_user(message.from_user.id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return
    await message.answer(
        f"Your profile:\n\nYour Gender {user.gender}\nYour Partner Gender {user.partner_gender}\nYour ratings **{user.rating}**\nVIP: {user.is_vip} \nTotal referral: {user.total_referral} ",
    )


@dp.message_handler(text=(constant.SS))
@dp.message_handler(Command("stopsearching"))
async def stop_searching(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)
    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return
    if user.state == "B":
        await db.update_state(message.from_user.id, "A")
        await message.answer(constant.STOP_SEARCHING, reply_markup=keyboard_markup)

    elif user.state == "A":
        await message.answer(constant.NOT_MATCHED, reply_markup=keyboard_markup)
    elif user.state == "C":
        await message.answer(constant.IN_CHAT, reply_markup=in_chat_markup)

    elif user.state == "D":
        await message.answer(constant.YOU_ARE_BANNED)


@dp.message_handler(text=(constant.CR))
@dp.message_handler(commands=["clear"])
async def send_clrk(message: types.Message):
    user_id = message.from_user.id
    await message.answer("Cleared.", reply_markup=types.ReplyKeyboardRemove())
    await bot.delete_message(user_id, message.message_id)
    await bot.delete_message(user_id, message.message_id + 1)
