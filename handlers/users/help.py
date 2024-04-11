from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state= "*")
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni qayta ishga tushirish",
            "/help - Yordam",
            "/admin - Admin panel",
            "/version - Versiya")
    await message.answer("\n".join(text))
