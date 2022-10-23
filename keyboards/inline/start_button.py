import constant
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
from data.config import TG_CHANNEL
from aiogram import types


DONATE_US_URL = "https://paypal.me/theRishuPandey"
BOT_SUPPORT_URL = "https://t.me/RandomMode_Bot"


JOIN_BUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📢  Join our channel", url=TG_CHANNEL)],
        [
            InlineKeyboardButton(text="Ask support", url=BOT_SUPPORT_URL),
            InlineKeyboardButton(text="Donate us", url=DONATE_US_URL),
        ],
    ]
)


keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btns_text = constant.NC
keyboard_markup.row(btns_text)
more_btns_text = (constant.ST, constant.HI)
keyboard_markup.add(*(KeyboardButton(text) for text in more_btns_text))
