from aiogram import types
from loader import dp, db, bot
from data.config import ADMINS


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni qayta ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("admin","Admin panel"),
            types.BotCommand("version","Versiya"),
        ]
    )