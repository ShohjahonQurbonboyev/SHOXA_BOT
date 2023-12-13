import asyncio
from aiogram import types
from data.config import ADMINS, SHIKOYATLAR
from loader import dp, db, bot
import pandas as pd
from states.main_state import  main,  adminstate, shikoyatstate
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.main_btn import  main_markup, change_markup, back_markup



@dp.message_handler(text='/admin', user_id=ADMINS, state="*")
async def enter_admin(message: types.Message):
    await message.answer("Parolni tering 🙈", reply_markup= ReplyKeyboardRemove() and back_markup)
    await adminstate.password.set()




@dp.message_handler(text='✍️ Taklif yoki shikoyatlar', state=main.main_menu)
async def taklif(message: types.Message):
    await message.answer("Taklif yoki shikoyatingizni yozing 👇", reply_markup=ReplyKeyboardRemove() and back_markup)
    await shikoyatstate.shikoyat.set()



@dp.message_handler(state=shikoyatstate.shikoyat)
async def shikoyatlar(message: types.Message):
        user_id = message.from_user.id
        fullname = message.from_user.full_name
        username = message.from_user.username
        shikoyat = message.text
        await bot.send_message(chat_id=SHIKOYATLAR, text=f"<b>To'liq ismi : {fullname}\n</b><b>Kimdan :</b> {username}\n\nShikoyat :👉 {shikoyat}")
        await message.answer(f"Taklifingiz adminga yuborildi tez orada siz bilan bog'lanishadi yoki kamchilik bo'lgan bo'lsa tuzatilib qo'yiladi \n<b>ETIBORINGIZ UCHUN RAXMAT !</b>", reply_markup=ReplyKeyboardRemove() and main_markup)
        await main.main_menu.set()