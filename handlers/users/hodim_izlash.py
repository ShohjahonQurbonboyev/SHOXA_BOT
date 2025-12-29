from aiogram import types
from loader import dp, db, bot
from data.config import ADMINS, VAKANSIYA
from keyboards.default.main_btn import  back_markup, main_markup
from keyboards.inline.inline_main import  resume_change, tasdiq_admin
from states.main_state import main, freelancer, hodim
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.storage import FSMContext




@dp.message_handler(text = "👥 Hodim kerak", state=freelancer.menu)
async def worker(message: types.Message, state: FSMContext):
    tip = message.text
    await message.answer("<b>Hodim topish:</b>\n\nHodim topish boyicha sizga maxsus shablon orqali savollar beriladi hammasiga javob berishingiz kerak bo`ladi !")
    try:
        await state.update_data(data={"tip" : tip})
        await message.answer("🏢 Idora nomi ?", reply_markup=back_markup)
        await hodim.idora.set()

    except:
        await message.answer("Texnik muammo yuzaga keldi iltomos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()



@dp.message_handler(state=hodim.idora)
async def company_name(message: types.Message, state: FSMContext):
    name = message.text
    try:
        await  state.update_data(data={"name" : name})
        await message.answer("<b>📚 Texnologiya:</b>\n\nTalab qilinadigan texnologiyalarni kiriting? ", reply_markup=back_markup)
        await hodim.technology.set()

    except:
        await message.answer("Texnik muammo yuzaga keli iltimos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()


@dp.message_handler(state=hodim.technology)
async def surnamne(message: types.Message, state: FSMContext):
    technologies = message.text
    try:
        await  state.update_data(data={"technologies" : technologies})
        await message.answer("<b>🌐 Hudud:</b>\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.", reply_markup=back_markup)
        await hodim.country.set()
    except:
        await message.answer("Texnik muammo yuzaga keli iltimos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()


@dp.message_handler(state=hodim.country)
async def surnamne(message: types.Message, state: FSMContext):
    country = message.text
    country = country.capitalize()
    await state.update_data(data={"country" : country})
    await message.answer("<b>✍️Mas'ul ism sharifi ?</b>", reply_markup=back_markup)
    await hodim.manager_name.set()



@dp.message_handler(state=hodim.manager_name)
async def surnamne(message: types.Message, state: FSMContext):
    manager_name = message.text
    try:
        manager_name = manager_name.capitalize()
        await  state.update_data(data={"manager_name" : manager_name})
        await message.answer("<b>🕰 Murojaat qilish vaqti:\n\n</b>Qaysi vaqtda murojaat qilish mumkin?\n<i>Masalan, 9:00 - 18:00</i>", reply_markup=back_markup)
        await hodim.time.set()
    except:
        await message.answer("Texnik muammo yuzaga keli iltimos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()



@dp.message_handler(state=hodim.time)
async def surnamne(message: types.Message, state: FSMContext):
    time = message.text
    try:
        await  state.update_data(data={"time" : time})
        await message.answer("<b>Ish vaqti:</b>\n\n<i>Masalan: 9:00 - 18:00</i>", reply_markup=back_markup)
        await hodim.work_time.set()
    except:
        await message.answer("Texnik muammo yuzaga keli iltimos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()


@dp.message_handler(state=hodim.work_time)
async def surnamne(message: types.Message, state: FSMContext):
    work_time = message.text
    try:
        await  state.update_data(data={"work_time" : work_time})
        await message.answer("<b>💰 Maosh:</b>\n\nQancha maosh taklif qilasiz ?", reply_markup=back_markup)
        await hodim.price.set()
    except:
        await message.answer("Texnik muammo yuzaga keli iltimos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()


@dp.message_handler(state=hodim.price)
async def surnamne(message: types.Message, state: FSMContext):
    try:
        price = message.text
        await  state.update_data(data={"price" : price})
        await message.answer("<b>‼️ Qo`shimcha ma`lumotlar ?</b>", reply_markup=ReplyKeyboardRemove() and back_markup)
        await hodim.ex_data.set()
    except:
        await message.answer("Texnik muammo yuzaga keli iltimos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()
        

@dp.message_handler(state=hodim.ex_data)
async def surnamne(message: types.Message, state: FSMContext):
    ex_data = message.text
    telegram = message.from_user.username
    telegram_id = message.from_user.id
    telegram = f"@{telegram}"
    try:    
        if telegram is None:
            await  state.update_data(data={"telegram" : "Username yo`q !"})
        else:
            await  state.update_data(data={"telegram" : telegram})
    except:
        await message.answer("Texnik muammo yuzaga keli iltimos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()

    try:
        data = await state.get_data()
        
        tip = data.get("tip")
        name = data.get('name')
        technologies = data.get('technologies')
        manager_name = data.get("manager_name")
        country = data.get('country')
        time = data.get("time")
        work_time = data.get("work_time")
        price = data.get('price')
        telegram = data.get('telegram')
        await state.update_data(data={"ex_data" : ex_data})
        await state.update_data(data={"telegram_id" : telegram_id})
        
        phone = await db.select_user(telegram_id=telegram_id)
        if phone:
            phone_number = phone["contact"]
    except:
        await message.answer("Texnik muammo yuzaga keli iltimos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()
    await message.answer(f"{tip}:\n\n🏢 Idora: <b>{name}</b>\n📚 Talablar: {technologies}\n✍️ Ma`sul shaxs: {manager_name}\n🌐 Hudud: {country}\n🕰 Murojaat vaqt: {time}\nIsh vaqti: {work_time}\nMaosh: {price}\nQo`shimcha ma`lumotlar {ex_data}\nTelegram: {telegram}\nAloqa uchun: {phone_number}\n\nBizning kanal - @vakans_uzb 👈\n\n\n<b>Malumotlaringiz to`g`rimi ?</b>", reply_markup=ReplyKeyboardRemove() and resume_change)
    await hodim.tasdiq.set()



@dp.callback_query_handler(lambda call: call.data in ["✅ To`g`ri", "❌ Xato"], state=hodim.tasdiq)
async def send(call: types.callback_query, state: FSMContext):
    data_call = call.data
    data = await state.get_data()
    photo = "https://telegra.ph/file/c17e45acef75e918e47cb.jpg"
    if data_call == "✅ To`g`ri":
        tip = data.get("tip")
        name = data.get('name')
        technologies = data.get('technologies')
        manager_name = data.get("manager_name")
        country = data.get('country')
        time = data.get("time")
        work_time = data.get("work_time")
        price = data.get('price')
        ex_data = data.get("ex_data")
        telegram = data.get('telegram')
        telegram_id = data.get("telegram_id")
        phone = await db.select_user(telegram_id=telegram_id)
        if phone:
            phone_number = phone["contact"]

        message_text = f"<b>{tip}:</b>\n\n🏢 Idora: <b>{name}</b>\n📚 Talablar: {technologies}\n✍️ Ma`sul shaxs: {manager_name}\n🌐 Hudud: {country}\n🕰 Murojaat vaqt: {time}\nIsh vaqti: {work_time}\nMaosh: {price}\nQo`shimcha ma`lumotlar: {ex_data}\nTelegram: {telegram}\nAloqa uchun: {phone_number}\n\nBizning kanal - @vakans_uzb 👈"
        await bot.send_photo(photo=photo, chat_id=ADMINS[0], caption=message_text,reply_markup=tasdiq_admin)
        await call.message.delete()
        await call.message.answer(f"sizning ma`lumotlaringiz adminga yuborildi ✅\nAgar admin ma`lumotlaringizni tasdiqlasa 24 soat ichida kanalga joylanadi", reply_markup=main_markup)
        await main.main_menu.set()
    elif data_call == "❌ Xato":
        await call.message.delete()
        await call.message.answer("Malumotlaringiz yo`q qilindi ❌", reply_markup=main_markup)
        await main.main_menu.set()
  


@dp.callback_query_handler(lambda call: call.data in ["✅ Tasdiqlash", "❌ Inkor etish"], state="*")
async def send(call: types.callback_query):
    data_call= call.data
    if data_call == "✅ Tasdiqlash":   
            await bot.copy_message(chat_id=VAKANSIYA, from_chat_id=call.message.chat.id, message_id=call.message.message_id)
            await call.message.delete()
            await call.message.answer(f"Ma`lumotlar kanalga muvoffaqiyatli joylashdi ✅")
            await main.main_menu.set()
    elif data_call == "❌ Inkor etish":
        await call.message.delete()
        await call.message.answer("Malumotlar bekor qilindi ❌", reply_markup=main_markup)
        await main.main_menu.set()