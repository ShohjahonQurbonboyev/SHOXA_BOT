import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.main_btn import  main_markup, change_markup, back_markup, admin_markup, project_markup, group_markup
from states.main_state import shikoyatstate, main, changestate, reklamastate, myprojects, adminstate, adminwebstate, deletestate,adminusrstate
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.storage import FSMContext




@dp.message_handler(text ="📤 Chiqish", state=adminstate.admin_menu)
async def main_redirect(message: types.Message):
    await message.answer("Siz Asosiy menuga qaytdingiz 🏚", reply_markup= main_markup)
    await main.main_menu.set()




@dp.message_handler(text ="🔙 Orqaga", state=changestate.change)
async def main_redirect(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup= main_markup)
    await main.main_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state=changestate.bot)
async def change_redirect(message: types.Message):
    await message.answer("Qanday proekt zakaz qilmoqchisiz ?", reply_markup=change_markup)
    await changestate.change.set()



@dp.message_handler(text ="🔙 Orqaga", state=changestate.web)
async def bot_redirect(message: types.Message):
    await message.answer("Qanday proekt zakaz qilmoqchisiz ?", reply_markup=change_markup)
    await changestate.change.set()


@dp.message_handler(text ="🔙 Orqaga", state=reklamastate.sorov)
async def reklama_back(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup=admin_markup)
    await adminstate.admin_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state = myprojects.change)
async def change_back(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup=main_markup)
    await main.main_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminstate.password)
async def change_back(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup=main_markup)
    await main.main_menu.set()



@dp.message_handler(text ="🔙 Orqaga", state = adminstate.change_prject)
async def change_back(message: types.Message):
    await message.answer("Siz admin menusidasiz !", reply_markup=admin_markup)
    await adminstate.admin_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminstate.name)
async def change_back(message: types.Message):
    await message.answer("Qaysi turdagi proektni qo'shmoqchisiz ?", reply_markup=project_markup)
    await adminstate.change_prject.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminstate.username)
async def change_back(message: types.Message):
    await message.answer("Telegram botning nomini yozing 👇", reply_markup=back_markup)
    await adminstate.name.set()



@dp.message_handler(text ="🔙 Orqaga", state = adminwebstate.name)
async def change_back(message: types.Message):
    await message.answer("Qaysi turdagi proektni qo'shmoqchisiz ?", reply_markup=project_markup)
    await adminstate.change_prject.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminwebstate.url)
async def change_back(message: types.Message):
    await message.answer("Web sitening nomini yozing 👇", reply_markup=back_markup)
    await adminwebstate.name.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminusrstate.change_user)
async def change_back(message: types.Message):
    await message.answer("Siz admin menusidasiz !", reply_markup=admin_markup)
    await adminstate.admin_menu.set()



@dp.message_handler(text ="🔙 Orqaga", state = deletestate.change_delete)
async def change_back(message: types.Message):
    await message.answer("Siz admin menusidasiz !", reply_markup=admin_markup)
    await adminstate.admin_menu.set()



@dp.message_handler(text ="🔙 Orqaga", state = shikoyatstate.shikoyat)
async def change_back(message: types.Message):
    await message.answer("Siz admin menusidasiz !", reply_markup=main_markup)
    await main.main_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminstate.write_group)
async def change_back(message: types.Message):
    await message.answer("Siz admin menusidasiz !", reply_markup=admin_markup)
    await adminstate.admin_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminstate.write)
async def change_back(message: types.Message):
    await message.answer("Qsysi guruhga yozmoqchisiz ?", reply_markup=group_markup)
    await adminstate.write_group.set()