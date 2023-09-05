
import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.main_btn import  main_markup
from states.main_state import mystate, main
from aiogram.types import ReplyKeyboardRemove
from datetime import date, datetime, time






@dp.message_handler(text="📋 Resume", state=main.main_menu)
async def send_resume(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    file_path = 'docs/My RESUME.pdf'
    msg = await message.answer("Iltimos kuting...🕒")
    try:
        with open(file_path, 'rb') as f:
            await bot.send_document(user_id, f, caption=f"Assalomu Aleykum <b>{full_name}</b>\nUshbu fayl Shohjahon tomonidan yaratilgan bo`lib unga resume vazifasini bajaradi.\n\n@this_is_shoxa_bot", reply_markup=main_markup)
    except:
        await message.answer("Resume jonatishda xatolik ⚠️")
    await msg.delete()
    await main.main_menu.set()

