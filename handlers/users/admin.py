import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from states.main_state import mystate, main, changestate, reklamastate, adminstate
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.main_btn import  main_markup, change_markup, back_markup



@dp.message_handler(text='/admin', user_id=ADMINS, state="*")
async def enter_admin(message: types.Message):
    await message.answer("Parolni tering 🙈", reply_markup= ReplyKeyboardRemove() and back_markup)
    await adminstate.password.set()







