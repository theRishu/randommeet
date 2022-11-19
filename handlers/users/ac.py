import types
from aiogram import types
from loader import dp, bot
import constant
from utils.misc import db_commands as db
from keyboards.inline.in_chat import in_chat_markup
from utils.misc import search

from keyboards.inline.start_button import keyboard_markup
from keyboards.inline.stop_searching import stop_search
from data.config import BROADCAST_CHANNEL as BC


@dp.message_handler(commands="nextchat")
@dp.message_handler(text=constant.AC)
async def another_chatnewchat(message: types.Message):
    user_id = message.from_user.id
    user = await db.select_user(user_id)

    if not user:
        await message.answer(constant.NOT_REGISTERED)
        return

    if user.state in ["A", "B", "C", "E"]:

        if user.partner_id != None:
            await db.update_after_leavechat(user_id, user.partner_id)
            try:
                await bot.send_message(
                    user.partner_id,
                    constant.PARTNER_LEAVED,
                    reply_markup=keyboard_markup,
                )
            except Exception as e:
                await bot.send_message(BC, str(e))

        await bot.send_message(
            user.user_id, constant.LEFT_WAITING, reply_markup=stop_search
        )


        await db.update_state(user.user_id, "B")
        found_user = await search.find_match_user(user_id)

        if found_user != None:
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

    else:
        pass
        """
        
        
        












        await db.update_state(user_id, "B")
        await message.answer(constant.NOT_MATCHED, reply_markup=keyboard_markup)
        found_user = await search.find_match_user(user_id)
        if found_user != None:
            match = await db.select_user(found_user)
            await bot.send_message(
                user_id,
                f"{constant.MATCHED}\nPartner Details\nRating: {match.rating}\nVIP user: {match.is_vip} \nGender: {match.gender}",
                reply_markup=in_chat_markup,
            )

            await db.update_after_match(user_id, found_user)
            await db.update_after_match(found_user, user_id)
            try:
                await bot.send_message(
                    found_user,
                    f"{constant.MATCHED}\nPartner Details\nRating: {user.rating}\nVIP user: {user.is_vip} \nGender: {user.gender}",
                    reply_markup=in_chat_markup,
                )
            except Exception as e:
                print(f"{str(e)} \n{found_user} deleted")
                await db.delete_user(found_user)

        await bot.send_message(
            user.user_id, constant.MATCHED, reply_markup=keyboard_markup
        )
        await bot.send_message(
            user.partner_id, constant.PARTNER_LEAVED, reply_markup=keyboard_markup
        )
    elif user.state == "D":
        await message.answer(constant.YOU_ARE_BANNED)
    
    elif user.state == "B":
        await message.answer("state b ")

    elif user.state == "C":
        await bot.send_message(user.user_id , "Hello", reply_markup=stop_search)

    else:
        pass

       
        try:
            MSG = "You left the chat. \n Waiting for user...🔍"
            await bot.send_message(user.user_id , MSG, reply_markup=stop_search)
           
           
            await db.update_after_anotherchat(user.user_id, user.partner_id)
            await db.update_after_leavechat(user.partner_id, user.user_id)
            try:
                await bot.send_message(
                    user.partner_id,
                    constant.PARTNER_LEAVED,
                    reply_markup=keyboard_markup,
                )
            except Exception as e:
                await message.answer(str(e))

            await bot.answer(" line 67")

            await db.update_state(user_id, "B")

            found_user = await search.find_match_user(user_id)
            if found_user != None:
                match = await db.select_user(found_user)
                await bot.send_message(
                    user_id,
                    f"{constant.MATCHED}\nPartner Details\nRating: {match.rating}\nVIP user: {match.is_vip} \nGender: {match.gender}",
                    reply_markup=in_chat_markup,
                )

            await db.update_after_match(user_id, found_user)
            await db.update_after_match(found_user, user_id)
            try:
                await bot.send_message(
                    found_user,
                    f"{constant.MATCHED}\nPartner Details\nRating: {user.rating}\nVIP user: {user.is_vip} \nGender: {user.gender}",
                    reply_markup=in_chat_markup,
                )
            except Exception as e:
                print(f"{str(e)} \n{found_user} deleted")
                await db.delete_user(found_user)

            await bot.send_message(
                user.user_id, constant.MATCHED, reply_markup=keyboard_markup
            )
            await bot.send_message(
                user.partner_id, constant.PARTNER_LEAVED, reply_markup=keyboard_markup
            )
        except Exception as e:
            await message.answer(str(e))
    
    else:
        await message.answer(constant.L_WANT_TO_CHAT)
"""
