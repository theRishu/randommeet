@dp.message_handler(Command("ban"))
async def ban(message: types.Message):
    id = int(message.text.split()[1])
    reason1 = message.text.split()[2]
    reason2 = message.text.split()[3]

    user = await db.select_user(id)
    await db.update_after_leavechat(user.partner_id, user.user_id)
    try:
        await bot.send_message(user.partner_id, constant.PARTNER_LEAVED, reply_markup=keyboard_markup)
    except Exception as e:
        print(str(e))
    await db.update_state(id, 'D')
    await bot.send_message(id, f'You were banned from using bot cause of {reason1} {reason2} and disconnected  from chat .\nIf you think you were banned by mistake contact @RandomMode_bot', reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Banned Successfully.")


@dp.message_handler(Command("unban"))
async def ban(message: types.Message):
    id = int(message.text.split()[1])
    await db.update_state(id, 'A')
    await bot.send_message(id, f'You got a second chance. Please use it correctly')
    await message.answer("Unbanned Successfully.")@dp.message_handler(Command("ban"))
    
    
async def ban(message: types.Message):
    id = int(message.text.split()[1])
    reason1 = message.text.split()[2]
    reason2 = message.text.split()[3]

    user = await db.select_user(id)
    await db.update_after_leavechat(user.partner_id, user.user_id)
    try:
        await bot.send_message(user.partner_id, constant.PARTNER_LEAVED, reply_markup=keyboard_markup)
    except Exception as e:
        print(str(e))
    await db.update_state(id, 'D')
    await bot.send_message(id, f'You were banned from using bot cause of {reason1} {reason2} and disconnected  from chat .\nIf you think you were banned by mistake contact @RandomMode_bot', reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Banned Successfully.")


@dp.message_handler(Command("unban"))
async def ban(message: types.Message):
    id = int(message.text.split()[1])
    await db.update_state(id, 'A')
    await bot.send_message(id, f'You got a second chance. Please use it correctly')
    await message.answer("Unbanned Successfully.")
