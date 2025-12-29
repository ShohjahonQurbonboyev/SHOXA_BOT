from aiogram import types
from loader import dp, db, bot
from data.config import ADMINS, VAKANSIYA
from keyboards.default.main_btn import  freelance_markup, back_markup, main_markup
from keyboards.inline.inline_main import  resume_change, tasdiq_admin
from states.main_state import main, freelancer
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.storage import FSMContext



@dp.message_handler(text = "📌 Freelancer", state=main.main_menu)
async def choose(message: types.Message):
    await message.answer("Siz qaysi xizmatdan foydalanmoqchisiz ?", reply_markup=freelance_markup)
    await freelancer.menu.set()


@dp.message_handler(text = "🏢 Ish joyi kerak", state=freelancer.menu)
async def work(message: types.Message, state: FSMContext):
    tip = message.text
    telegram_id = message.from_user.id
    await message.answer("<b>Ish joyini topish:</b>\n\nIsh joyini topish boyicha sizga maxsus shablon orqali savollar beriladi hammasiga tog`ri javob berishingiz kerak bo`ladi !")
    try:
        await state.update_data(data={"tip" : tip})
        await state.update_data(data={"telegram_id" : telegram_id})
        await message.answer("Ismingiz nima ?", reply_markup=back_markup)
        await freelancer.name.set()

    except:
        await message.answer("Texnik muammo yuzaga keldi iltomos adminga habar bering !", reply_markup=main_markup)
        await state.finish()


@dp.message_handler(state=freelancer.name)
async def surnamne(message: types.Message, state: FSMContext):
    name = message.text
    try:
        if name.isalpha():
            name = name.capitalize()
            await  state.update_data(data={"name" : name})
            await message.answer("Familiyangiz nima ? ", reply_markup=back_markup)
            await freelancer.surname.set()
        else:
            await message.answer("Ismni harflar yordamida kiriting !")
    except:
        await message.answer("Texnik muammo yuzaga keli iltimos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()


@dp.message_handler(state=freelancer.surname)
async def surnamne(message: types.Message, state: FSMContext):
    surname = message.text
    try:
        if surname.isalpha():
            surname = surname.capitalize()
            await  state.update_data(data={"surname" : surname})
            await message.answer("Yoshingiz nechchida ?", reply_markup=back_markup)
            await freelancer.age.set()
        else:
            await message.answer("Familiyani harflar yordamida kiriting !")
    except:
        await message.answer("Texnik muammo yuzaga keli iltimos adminga habar bering !", reply_markup=main_markup)
        await main.main_menu.set()


@dp.message_handler(state=freelancer.age)
async def surnamne(message: types.Message, state: FSMContext):
    age = message.text
    if age.isnumeric():
        age = int(age)
        if age > 14 and age < 50:
            await  state.update_data(data={"age" : age})
            await message.answer("Mutahasisligingiz nima ?", reply_markup=back_markup)
            await freelancer.technologies.set()
        elif age < 14:
            await message.answer("Sizning yoshingiz ish uchun juda kichkinalik qiladi !")
        elif age > 50:
            await message.answer("Sizning yoshingiz ishlash uchun juda kattalik qiladi !")
    else:
        await message.answer("Yoshingizni son korinishida yozing !")


@dp.message_handler(state=freelancer.technologies)
async def surnamne(message: types.Message, state: FSMContext):
    technologies = message.text
    if technologies:
        await  state.update_data(data={"technologies" : technologies})
        await message.answer("Viloyat yoki shaharni yozing ?", reply_markup=back_markup)
        await freelancer.country.set()
    else:
        await message.answer("Iltimos mutahasisligingizni faqat matn ko`rinishida kiriting !\n\n<i>Masalan : python HTML CSS</i>")


@dp.message_handler(state=freelancer.country)
async def surnamne(message: types.Message, state: FSMContext):
    country = message.text
    if country:
        country = country.capitalize()
        await state.update_data(data={"country" : country})
        await message.answer("Qancha maosh sizni qoniqtiradi ?\n<i>Uzbek so`mida hisoblaganda</i>\n\n<i>Masalan: 2000000</i>", reply_markup=back_markup)
        await freelancer.price.set()
    else:
        await message.answer("Iltimos shaharni faqat matn ko`rinishida kiriting !\n\n<i>Masalan : Toshkent</i>")


@dp.message_handler(state=freelancer.price)
async def surnamne(message: types.Message, state: FSMContext):
    price = message.text
    # price = f"{price} So`m"
    if price.isnumeric():
        price = int(price)
        if price >= 1000000:
            price = f"{price} so`m"
            await  state.update_data(data={"price" : price})
            await message.answer("Maqsadingiz ?", reply_markup=ReplyKeyboardRemove() and back_markup)
            await freelancer.maqsad.set()
        elif price < 1000000:
            await message.answer("Bu oylik maosh uchun juda kichik summa kiritadigan summangiz 1 million so`mdan kam bo`lmasligi kerak !")
    else:
        await message.answer("Iltimos maoshni faqat son ko`rinishida va uzbek so`mida kiriting !\n\n<i>Masalan : 2000000</i>")
    
    
@dp.message_handler(state=freelancer.maqsad)
async def surnamne(message: types.Message, state: FSMContext):
    maqsad = message.text
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

    data = await state.get_data()
    await  state.update_data(data={"maqsad" : maqsad})
    tip = data.get("tip")
    name = data.get('name')
    surnamne = data.get('surname')
    age = data.get('age')
    technologies = data.get('technologies')
    country = data.get('country')
    price = data.get('price')
    telegram = data.get('telegram')
    phone = await db.select_user(telegram_id=telegram_id)
    if phone:
        phone_number = phone["contact"]
    await message.answer(f"{tip}:\n\n👨‍💼 Xodim: <b>{name} {surnamne}</b>\n🕑Yosh: {age}\n📚 Mutahasisligi: {technologies}\n🌐 Hudud: {country}\n💰 Ish haqqi: {price}\n🇺🇿 Telegram: {telegram}\n📞 Aloqa uchun: {phone_number}\n🔎 Maqsadim: {maqsad}\n\nBizning kanal - @vakans_uzb 👈\n\n\n<b>Malumotlaringiz to`g`rimi ?</b>", reply_markup=ReplyKeyboardRemove() and resume_change)
    await freelancer.tasdiq.set()


@dp.callback_query_handler(lambda call: call.data in ["✅ To`g`ri", "❌ Xato"], state=freelancer.tasdiq)
async def send(call: types.callback_query, state: FSMContext):
    data_call = call.data
    data = await state.get_data()
    photo = "https://www.iitg.ac.in/stud/d.himadree/assets/images/resume2.jpg"
    if data_call == "✅ To`g`ri":
        maqsad = data.get("maqsad")
        tip = data.get("tip")
        name = data.get('name')
        surnamne = data.get('surname')
        age = data.get('age')
        technologies = data.get('technologies')
        country = data.get('country')
        price = data.get('price')
        telegram = data.get('telegram')
        telegram_id = data.get("telegram_id")
        phone = await db.select_user(telegram_id=telegram_id)
        if phone:
            phone_number = phone["contact"]

        message_text = f"<b>{tip}:</b>\n\n👨‍💼 Xodim: <b>{name} {surnamne}</b>\n🕑Yosh: {age}\n📚 Mutahasisligi: {technologies}\n🌐 Hudud: {country}\n💰 Ish haqqi: {price}\n🇺🇿 Telegram: {telegram}\n📞 Aloqa uchun: {phone_number}\n🔎 Maqsadim: {maqsad}\n\nBizning kanal - @vakans_uzb 👈"
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

