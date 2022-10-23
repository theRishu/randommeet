from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import CallbackQuery, ContentType, Message, reply_keyboard
from keyboards.inline.help_button import back_keyboard, choice

from loader import dp
import constant 

@dp.message_handler(text=(constant.HI))
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(text="Choose one from the following choices:", reply_markup=choice)


@dp.callback_query_handler(text_contains="commands")
async def show_commands(call: CallbackQuery):
    await call.message.edit_text(f'This are supported commands:{constant.COMMAND_LIST}')

    await call.message.edit_reply_markup(reply_markup=back_keyboard)


@dp.callback_query_handler(text_contains="bot_info")
async def show_bot_info(call: CallbackQuery):
    await call.message.edit_text(constant.BOT_INFO)
    await call.message.edit_reply_markup(reply_markup=back_keyboard)


@dp.callback_query_handler(text_contains="feedback")
async def show_feedback_option(call: CallbackQuery):
    await call.message.edit_text(constant.FEEDBACK)
    await call.message.edit_reply_markup(reply_markup=back_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("You have canceled this operation!", show_alert=True)
    await call.message.edit_text("Operation was cancelled")
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(text_contains="back")
async def show_commands(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=choice)