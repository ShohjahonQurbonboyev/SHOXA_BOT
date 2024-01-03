
from aiogram import types
from loader import dp
from keyboards.inline.inline_main import  tasdiq




@dp.message_handler(state="*")
async def any_msg(message: types.Message):
    tabriklar = ["Tabriklayman", "Tabrikliman", "tabrikliman", "tabriklayman","tugilgan kuning bilan", "happi birthday", "tabriklaymiz", "Uzoq umir", "Табриклиман", "Табриклайман", "тугилган кунинг бн"]
    for tabrik in tabriklar:
        if tabrik.lower() in message.text:
            await message.answer("Bugun tug`ilgan kunmi ?", reply_markup=tasdiq)


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



