from aiogram import executor


from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

from utils.db_api.db import engine
from utils.db_api.base import Base


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    async with engine.begin() as conn:
        #await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


executor.start_polling(dp, on_startup=on_startup)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

