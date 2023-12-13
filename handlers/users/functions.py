
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS, USER_CHANNEL, PASSWORD_ADMIN, GURUH
from utils.extra_datas import make_title
import pandas as pd
from keyboards.inline.inline_main import kanal, kino_kanal, tasdiq
from keyboards.default.main_btn import admin_markup, project_markup, back_markup, usr_markup, main_markup, delete_markup
from states.main_state import adminstate, adminwebstate, adminusrstate, reklamastate, main, deletestate
from aiogram.types import ReplyKeyboardRemove


tabriklar = ["Tabriklayman", "Tabrikliman", "tugilgan kuning bilan", "happi birthday", "tabriklaymiz", "Uzoq umir", "Табриклиман", "тугилган кунинг бн"]
salomlashuvlar = ["Assalomu aleykum", "assalomu aleykum", "salom", "привет", "hello, Hello", "Assalom", "assalom","ассалому алейкум", "Ассалому алейкум"]

def tabrik(message):
    for tabrik in tabriklar:
        if  tabrik.lower() in message.text:
            return message
            # return message.answer("Bugun tug`ilgan kunmi ?", reply_markup=tasdiq)



def salomlashuv(salom):
    for salom1 in salomlashuvlar:
        if  salom1.lower() in salom:
            return salom1