from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import USER_CHANNEL
from utils.extra_datas import make_title
from keyboards.default.main_btn import contact, main_markup
from states.main_state import phonestate, main
from aiogram.dispatcher.storage import FSMContext





@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    try:
        await state.finish()
        full_name = message.from_user.full_name
        user = await db.select_user(telegram_id=message.from_user.id)
        if user is None:
            await message.answer(f"Assalomu Aleykum \nBotga hush kelibsiz {full_name} 👋🤓")
            await message.answer("Botdan foydalanish uchun telefon raqamingizni ulashishingiz zarur !\n<i>\"Malumotlaringiz 100% maxfiy saqlanishiga kafolat beramiz !\"</i>", reply_markup=contact)
            await phonestate.phone.set()
        else:
            await message.answer("Siz Asosiy menudasiz 🏠",reply_markup= main_markup)
            await main.main_menu.set()
    except Exception as ex:
        await message.answer(f"Error : {ex}")


@dp.message_handler(content_types=['contact'], state=phonestate.phone)
async def get_phone(message: types.Message):
    username = message.from_user.username
    telegram_id = message.from_user.id
    contact = message.contact.phone_number
    full_name = message.from_user.full_name
    audio = "voices/salom.wav"
    user = await db.select_user(telegram_id=message.from_user.id)
    if user is None:
        user = await db.add_user(
                telegram_id=message.from_user.id,
                full_name=full_name,
                username=message.from_user.username,
                contact=contact
            )
        await bot.send_message(chat_id=USER_CHANNEL, text=f"<b>Foydalanuvchi ma\'lumotlari:</b>\n\n<b>Full_Name:</b> {full_name}\n<b>Telegram_ID:</b> {telegram_id}\n<b>Username:</b> @{username}\n<b>Telefon_raqam:</b> {contact}")
        await message.delete()
        await message.answer("Ma`lumotlaringiz saqlandi botdan foydalanishingiz mumkin 😌")
        try:
            msg = await message.answer('Iltimos kuting...⏱')
            with open(audio, "rb") as audio:
                await message.answer_voice(voice= audio)
                await msg.delete()
        except:
            await message.answer("Texnik xatolik yuzaga keldi iltimos adminga xabar bering ?")
        await message.answer("Siz Asosiy menudasiz 🏠", reply_markup=main_markup)
        await main.main_menu.set()


@dp.message_handler(text='/version', state="*")
async def version(message: types.Message):
    await message.answer(f"<b>Bot Versions</b>\n\n1.5.2 - Version")