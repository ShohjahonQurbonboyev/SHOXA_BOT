
from aiogram import types
from loader import dp, bot
from keyboards.default.main_btn import  main_markup
from states.main_state import  main




@dp.message_handler(text="🎵 My beats", state=main.main_menu)
async def send_resume(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    file_path = 'music/SHOXA - Yolg\'izman.mp3'
    msg = await message.answer("Iltimos kuting...🕒")
    try:
        with open(file_path, 'rb') as f:
            await bot.send_audio(user_id, f, caption=f"Assalomu Aleykum <b>{full_name}</b>\nUshbu musiqa Shohjahon tomonidan ijro etilgan bo`lib unda xayotiy voqeyalar aks ettirilgan.\n\n@this_is_shoxa_bot", reply_markup=main_markup)
    except:
        await message.answer("Musiqa jonatishda xatolik ⚠️")
    await msg.delete()
    await main.main_menu.set()


