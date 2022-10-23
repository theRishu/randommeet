from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("nextchat", "get matched with another user"),
            types.BotCommand("newchat", "start a newchat"),
            types.BotCommand("leavechat", "leave a chat"),
            types.BotCommand("play", "start playing tod"),
             types.BotCommand("clear", "removes the button"),
          
          
            types.BotCommand("mix", "help to select from truth or dare"),
            types.BotCommand("shareprofile", "share your profile link to partner"),
            types.BotCommand("help", "will show help message"),
            types.BotCommand("settings", "check your settings."),
            types.BotCommand("myprofile", "check your profile"),
            types.BotCommand("deleteprofile", "delete your profile"),
            types.BotCommand("getlink", "get your vip referral link"), 
            types.BotCommand("truth", "send random truth to partner"),
            types.BotCommand("dare", "send random dare to partner"),

        ]
    )