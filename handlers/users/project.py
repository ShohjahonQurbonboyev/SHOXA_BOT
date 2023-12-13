import asyncio
from aiogram import types
from data.config import ADMINS, PROJECT_CHANNEL, CODE_CHANNEL
from loader import dp, db, bot
from keyboards.default.main_btn import  main_markup, change_markup, back_markup, my_project_markup
from keyboards.inline.inline_main import kanal, kino_kanal
from states.main_state import mystate, main, changestate, myprojects
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.storage import FSMContext



@dp.message_handler(text="📥 Proekt zakaz qilish", state=main.main_menu)
async def get_project(message: types.Message):
    await message.answer("Qanday proekt zakaz qilmoqchisiz ?", reply_markup=change_markup)
    await changestate.change.set()



@dp.message_handler(text="🤖 Telegram Bot", state=changestate.change)
async def bot_project(message: types.Message):
    await message.answer("Siz hohlagan Telegram bot qanday bo'lishi kerak ?\nBatafsil tushuntirib yozing 👇", reply_markup=ReplyKeyboardRemove() and back_markup)
    await changestate.bot.set()


@dp.message_handler(state=changestate.bot)
async def get_bot_project(message: types.Message):
    xabar = message.text
    telegram_id = message.from_user.id
    user =  await db.select_user(telegram_id=telegram_id)
    username = message.from_user.username
    try:
        full_name = message.from_user.full_name
        await bot.send_message(chat_id=PROJECT_CHANNEL, text=f"<b>Full_name:</b> {full_name}\n<b>Phone_number:</b> {user[-2]}\n<b>Username:</b> @{username}\n\n<b>Zakaz:</b> Telegram Bot\n<b>Talablar:</b>\n{xabar}")
        await message.answer(f"Xurmatli {full_name} sizning xabaringiz adminga yuborildi tez orada siz bilan bo'glanishadi", reply_markup=ReplyKeyboardRemove() and main_markup)
        await main.main_menu.set()
    except:
        await message.answer("Kechirasiz Xabar jonatishda xatolik yuz berdi", reply_markup=ReplyKeyboardRemove() and main_markup)
        await main.main_menu.set()



@dp.message_handler(text="💢 Web (Backend)", state=changestate.change)
async def web_project(message: types.Message):
    await message.answer("Siz hohlagan Web sayt qanday bo'lishi kerak ?\nBatafsil tushuntirib yozing 👇", reply_markup=ReplyKeyboardRemove() and back_markup)
    await changestate.web.set()


@dp.message_handler(state=changestate.web)
async def get_bot_project(message: types.Message):
    xabar = message.text
    telegram_id = message.from_user.id
    user =  await db.select_user(telegram_id=telegram_id)
    username = message.from_user.username
    try:
        full_name = message.from_user.full_name
        await bot.send_message(chat_id=PROJECT_CHANNEL, text=f"<b>Full_name:</b> {full_name}\n<b>Phone_number:</b> {user[-2]}\n<b>Username:</b> @{username}\n\n<b>Zakaz:</b> Web Sayt\n<b>Talablar:</b>\n{xabar}")
        await message.answer(f"Xurmatli {full_name} sizning xabaringiz adminga yuborildi tez orada siz bilan bo'glanishadi", reply_markup=ReplyKeyboardRemove() and main_markup)
        await main.main_menu.set()
    except:
        await message.answer("Kechirasiz Xabar jonatishda xatolik yuz berdi", reply_markup=ReplyKeyboardRemove() and main_markup)
        await main.main_menu.set()




@dp.message_handler(text="📦 Mening proektlarim", state=main.main_menu)
async def my_projects(message: types.Message):
    await message.answer("Qanday turdagi proekt kerak ?", reply_markup=my_project_markup)
    await myprojects.change.set()



@dp.message_handler(text="🤖 Telegram Bot", state=myprojects.change)
async def my_projects_bot(message: types.Message):
    try:
        await db.create_table_bot()
        bots = await db.select_all_bots()
        
        if not bots:
            await message.answer("Xozircha Telegram botlar mavjud emas ⛔️", reply_markup=my_project_markup)
        else:
            await message.answer("<b>Mening Telegram botlarim:</b>", reply_markup=my_project_markup)
            for bot in bots:
                await message.answer(f"@{bot[2]}")
    except Exception as e:
        await message.answer(f"Xatolik yuz berdi: {e}")
        


@dp.message_handler(text="💢 Web site", state=myprojects.change)
async def my_projects_site(message: types.Message):
    try:
        await db.create_table_site()
        sites = await db.select_all_sites()
        
        if not sites:
            await message.answer("Xozircha Websitelar mavjud emas ⛔️", reply_markup=my_project_markup)
        else:
            await message.answer("<b>Mening WebSite larim:</b>", reply_markup=my_project_markup)
            for site in sites:
                await message.answer(f"{site[2]}")
    except Exception as e:
        await message.answer(f"Xatolik yuz berdi: {e}")


@dp.message_handler(text="🧑🏻‍💻 kodlar", state=myprojects.change)
async def my_projects_channel(message: types.Message):  
    picture ="https://i.pinimg.com/originals/1c/54/f7/1c54f7b06d7723c21afc5035bf88a5ef.png"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=picture, caption=f"<b>Mening yozgan barcha kodlarim shu kanalga joylab boriladi agar sizga opensource codlar maqul bo'lsa yoki codlardan faol foydalanib bormoqchi bolsangiz kanalga obuna bo'lishni unutmang !</b>", reply_markup=kanal)
    await message.answer("Biz sizni hechqanday noqonuniy ishlarga undamaymiz kanaldan faqat ilim olish maqsadida foydalaning siz qilgan ishlarga biz javob bermaymiz ‼️", reply_markup=my_project_markup)
    



@dp.message_handler(text="🌐 GitHub", state=myprojects.change)
async def my_codes_github(message: types.Message):  
    url="https://github.com/SHOXAonion"
    user_id = message.from_user.id
    photo = "pictures/github.png"
    msg = await message.answer("Iltimos kuting...🕒")
    try:
        with open(photo, 'rb') as photo:
            await message.answer_photo(photo=photo, caption=f"Bu mening GitHub sahifam:\n{url}", reply_markup=my_project_markup)
            await msg.delete()
    except:
        await message.answer("Rasm jo'natishda xatolik ⚠️")



@dp.message_handler(text = "🎦 Kanallar", state=main.main_menu)
async def movie(message: types.Message):
    photo_url = "pictures/cinema.jpg"
    try: 
        with open(photo_url, "rb") as photo_url:
            await message.answer_photo( photo=photo_url, caption = "<b>Virtual cinema</b>\n bu kanalda qiziqarli kinolar toplami mavjud kirish uchun pastdagi tugmani bosing ! 👇", reply_markup=kino_kanal)
    except:
        await message.answer("Texnik nosozlik yuz berdi iltomos adminga xabar bering !")
    

@dp.message_handler(text = "🛍 Online shop", state=main.main_menu)
async def online_shop(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f"Xurmatli {name} !\nBu xizmatimiz dasturchilarimiz tomonidan ishlab chiqilmoqda tez orada bu xizmatimiz ham qo`shiladi 😇")