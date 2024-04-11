
from aiogram import types
import asyncio
from data.config import ADMINS, SHIKOYATLAR
from loader import dp, bot
from states.main_state import  main,  adminstate, shikoyatstate, send_msg
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.main_btn import  main_markup, back_markup
from aiogram.dispatcher.storage import FSMContext
from handlers.users.functions import count_time




@dp.message_handler(text='/admin', user_id = ADMINS, state="*")
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



@dp.message_handler(text="xabar", state="*", user_id = ADMINS)
async def xabar(message: types.Message, state: FSMContext):
    await message.answer("Nima demoqchisiz ?", reply_markup=back_markup)
    await send_msg.number_msg.set()


@dp.message_handler(state=send_msg.number_msg)
async def xabar(message: types.Message, state: FSMContext):
    await state.update_data(data={"xabar" : message.text})
    await message.answer("Nechta xabar jo'natilsin ?", reply_markup=back_markup)
    await send_msg.xabar.set()


@dp.message_handler(state=send_msg.xabar)
async def sending_msg(message: types.Message, state: FSMContext):
    data = await state.get_data()
    xabar_msg = data.get('xabar')
    message_text = int(message.text)
    counting = count_time(number=message_text)


    if int(message_text) > 300:
        await message.answer("Siz bir urunishni o'zida 200 tadan ortiq xabar jonata olmaysiz")
    else:
        msg = 0
        await message.answer(f"Xabar jonatish boshlandi\nXabar {counting[0]} soat {counting[1]} daqiqa va {counting[2]} soniyada jo'natib bo'linadi")
        try:
            if message.from_user.id == int(ADMINS[0]):
                son  = await bot.send_message(chat_id=ADMINS[0], text=msg)
                while True:
                    if msg == int(message_text):
                        break
                    else:
                        await bot.send_message(chat_id=ADMINS[1], text=xabar_msg)
                        msg += 1
                        await asyncio.sleep(0.8)
                        await son.edit_text(msg)
                await son.delete()
                await bot.send_message(chat_id=ADMINS[0], text=f"{msg} ta xabar muvoffaqiyatli jonatildi ✅", reply_markup=main_markup)
                await main.main_menu.set()
            elif message.from_user.id == int(ADMINS[1]):
                son  = await bot.send_message(chat_id=ADMINS[1], text=msg)
                while True:
                    if msg == int(message_text):
                        break
                    else:
                        await bot.send_message(chat_id=ADMINS[0], text=xabar_msg)
                        msg += 1
                        await asyncio.sleep(0.8)
                        await son.edit_text(msg)
                await son.delete()
                await bot.send_message(chat_id=ADMINS[1], text=f"{msg} ta xabar muvoffaqiyatli jonatildi ✅", reply_markup=main_markup)
                await main.main_menu.set()

        except Exception as ex:
            ex = str(ex)
            await bot.send_message(chat_id=ADMINS[0], text=f"{msg} ta xabar jonatildi va xatolik yuz berdi ?", reply_markup=main_markup)
            await main.main_menu.set()
