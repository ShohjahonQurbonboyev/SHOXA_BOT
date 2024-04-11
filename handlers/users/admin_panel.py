from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS,  PASSWORD_ADMIN
import pandas as pd
import asyncio
from keyboards.default.main_btn import admin_markup, project_markup, back_markup, usr_markup,  delete_markup, group_markup
from states.main_state import adminstate, adminwebstate, adminusrstate, reklamastate, deletestate
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ReplyKeyboardRemove



@dp.message_handler(state=adminstate.password, user_id = ADMINS)
async def confirm_password(message: types.Message):
    parol = str(message.text)
    try:
        if parol == PASSWORD_ADMIN:
            await message.answer("Admin panelga xush kelibsiz 👋🧑🏻", reply_markup=admin_markup)
            await message.delete()
            await adminstate.admin_menu.set()
        else:
            await message.answer("Parol noto'g'ri ❌")
    except:
        await message.answer("Texnik nosozlik yuz berdi iltimos adminga habar bering !")



@dp.message_handler(text = "➕ Proekt qo'shish", state=adminstate.admin_menu)
async def add_project(message: types.Message):
    await message.answer("Qaysi turdagi proektni qo'shmoqchisiz ?", reply_markup=project_markup)
    await adminstate.change_prject.set()


@dp.message_handler(text = "🤖 Telegram Bot", state=adminstate.change_prject)
async def add_project(message: types.Message, state: FSMContext):
    await message.answer("Telegram botning nomini yozing 👇", reply_markup= ReplyKeyboardRemove() and back_markup)
    await adminstate.name.set()


@dp.message_handler(state=adminstate.name)
async def add_project(message: types.Message, state: FSMContext):
    name = message.text
    try:
        await state.update_data(data={"name" : name})
        await message.answer("Telegram botning usernameni yozing 👇", reply_markup=ReplyKeyboardRemove() and back_markup)
        await adminstate.username.set()
    except:
        await message.answer("Xatolik")

@dp.message_handler(state=adminstate.username)
async def add_project(message: types.Message, state: FSMContext):
    username = message.text
    telegram_bot =await db.select_bot(username=username)
    try:
        await state.update_data(data={"username" : username})
        data = await state.get_data()
        name = data.get('name')
        try:
            telegram_bot = await db.add_bot(
                name=name,
                username=username
            )
        except:
            await message.answer("Telegram bot qo'shishda xatolik")

        await message.answer("Telegram bot muvofaqiyatli qo'shildi ✅", reply_markup=ReplyKeyboardRemove() and admin_markup)
        await adminstate.admin_menu.set()
    except:
        await message.answer("Xatolik")






@dp.message_handler(text = "💢 Web site", state=adminstate.change_prject)
async def add_project(message: types.Message, state: FSMContext):
    await message.answer("Web sitening nomini yozing 👇", reply_markup=ReplyKeyboardRemove() and back_markup)
    await adminwebstate.name.set()


@dp.message_handler(state=adminwebstate.name)
async def add_project(message: types.Message, state: FSMContext):
    name = message.text
    try:
        await state.update_data(data={"name" : name})
        await message.answer("Web sitening Urlni kiriting 👇", reply_markup=ReplyKeyboardRemove() and back_markup)
        await adminwebstate.url.set()
    except:
        await message.answer("Xatolik")


@dp.message_handler(state=adminwebstate.url)
async def add_project(message: types.Message, state: FSMContext):
    url = message.text
    site =await db.select_site(username=url)
    try:
        await state.update_data(data={"username" : url})
        data = await state.get_data()
        name = data.get('name')
        try:
            site = await db.add_sites(
                name=name,
                username=url
            )
        except:
            await message.answer("web site qo'shishda xatolik")

        await message.answer("web site muvofaqiyatli qo'shildi ✅", reply_markup=admin_markup)
        await adminstate.admin_menu.set()
    except:
        await message.answer("Xatolik", reply_markup=admin_markup)
        await adminstate.admin_menu.set()




@dp.message_handler(text = "👥 Userlar", state=adminstate.admin_menu)
async def add_project(message: types.Message):
    await message.answer("Userlar boshqaruv paneli", reply_markup=usr_markup)
    await adminusrstate.change_user.set()


@dp.message_handler(text = "👥 Foydalanuvchilar soni", state=adminusrstate.change_user)
async def add_project(message: types.Message):
    count_users = await db.count_users()
    await message.answer(text=f'Foydalanuvchilar soni: {count_users} ta 😁', reply_markup=usr_markup)


@dp.message_handler(text = "👤 kimlar foydalanadi", state=adminusrstate.change_user)
async def add_project(message: types.Message):
    users = await db.select_all_users()
    name = []
    for user in users:
        name.append(user[1])
    data = {
        "Name": name
    }
    pd.options.display.max_rows = 10000
    df = pd.DataFrame(data)
    if len(df) > 50:
        for x in range(0, len(df), 50):
            await bot.send_message(message.chat.id, df[x:x + 50])
    else:
       await bot.send_message(message.chat.id, df)


@dp.message_handler(text = "🌇 Reklama", state=adminstate.admin_menu)
async def add_project(message: types.Message):
    await message.answer("Reklama bo`limiga hush kelibsiz 🫡", reply_markup=ReplyKeyboardRemove())
    await message.answer("Reklama sifatida yubormoqchgi bolgan matningizni kiriting 👇", reply_markup=back_markup)
    await reklamastate.sorov.set()



@dp.message_handler(state=reklamastate.sorov)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:   
        try: 
            user_id = user[-1]
            await bot.send_message(chat_id=user_id, text=message.text)
            await asyncio.sleep(0.05)
        except:
            for admin in ADMINS:
                await bot.send_message(chat_id=admin, text=f"<b>{user['full_name']}</b> botni blocklagan 🫣")
                
    await message.answer("Reklama muvofaqiyatli tarqatildi ✅", reply_markup=ReplyKeyboardRemove() and admin_markup)
    await adminstate.admin_menu.set()



@dp.message_handler(text = "✍️ Xabar jo'natish", state=adminstate.admin_menu)
async def write(message: types.Message):
    await message.answer(f"Nima deb yozmoqchisiz ?", reply_markup=ReplyKeyboardRemove() and back_markup)
    await adminstate.write.set()


@dp.message_handler(state=adminstate.write)
async def sendmessage(message: types.Message):
    chat_id = message.from_user.id
    message_text = message.text
    if chat_id == int(ADMINS[1]):
        msg_admin1 = await bot.send_message(chat_id=ADMINS[0], text=message_text)
        await message.answer("Xabar jonatildi ✅")

    elif chat_id == int(ADMINS[0]):
        msg = await bot.send_message(chat_id=ADMINS[1], text=message_text)
        await message.answer("Xabar jonatildi ✅")


@dp.message_handler(text = "🗑 O'chirish", state=adminstate.admin_menu)
async def add_project(message: types.Message):
    await message.answer("Qaysini o'chirmoqchisiz ?", reply_markup=delete_markup)
    await deletestate.change_delete.set()


@dp.message_handler(text = "❌ Foydalanuvchilar ❌", state=deletestate.change_delete)
async def add_project(message: types.Message):
    await db.delete_users()
    await message.answer("Baza tozalandi ✅")


@dp.message_handler(text = "❌ Teleram Botlar ❌", state=deletestate.change_delete)
async def add_project(message: types.Message):
    await db.delete_bot()
    await message.answer("Botlar o'chirib tashlandi tozalandi ✅")


@dp.message_handler(text = "❌ Web sitelar ❌", state=deletestate.change_delete)
async def add_project(message: types.Message):
    await db.delete_site()
    await message.answer("web sitelar o'chirib tashlandi ✅")