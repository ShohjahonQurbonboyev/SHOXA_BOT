
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS, USER_CHANNEL, PASSWORD_ADMIN, GURUH
from utils.extra_datas import make_title
import pandas as pd
# from handlers.users.functions import tabrik, salomlashuv
from handlers.users.functions import tabriklar, salomlashuvlar
from keyboards.inline.inline_main import kanal, kino_kanal, tasdiq
from keyboards.default.main_btn import admin_markup, project_markup, back_markup, usr_markup, main_markup, delete_markup
from states.main_state import adminstate, adminwebstate, adminusrstate, reklamastate, main, deletestate
from aiogram.types import ReplyKeyboardRemove



@dp.message_handler(lambda msg: msg.text in tabriklar, state="*")
@dp.message_handler(lambda msg: msg.text in salomlashuvlar , state="*")
async def any_msg(message: types.Message):
    location = "voices/Assalom.wav"
    if message.text in tabriklar:
       await message.answer("Bugun tug`ilgan kunmi ?", reply_markup=tasdiq)
    elif message.text in salomlashuvlar:
        msg = await message.answer("Gapiryabman...🗣")
        with open(location, "rb") as location:
                await message.answer_voice(voice=location)
        await msg.delete()



@dp.callback_query_handler(lambda call: call.data in  ["ha", "yo'q"])
async def yes_or_no(call: types.callback_query):
    tabriknoma = "voices/Tabrik.wav"
    data = call.data
    if data == "ha":
        msg = await call.message.answer("Gapiryabman...🗣")
        with open(tabriknoma, "rb") as tabriknoma:
            await call.message.answer_voice(voice= tabriknoma)
            await msg.delete()
        await call.message.delete()
    elif data == "yo'q":
        await call.message.answer("Ha mayli")
        await call.message.delete()



