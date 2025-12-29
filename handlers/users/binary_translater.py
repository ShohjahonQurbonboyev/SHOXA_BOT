from aiogram import types
from loader import dp
from keyboards.default.main_btn import  binary_markup, back_markup
from states.main_state import main, translaterbn
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(text = "💻 Binary language", state=main.main_menu)
async def translater(message: types.Message):
    await message.answer("Tarjima turini tanlang", reply_markup=binary_markup)
    await translaterbn.translate.set()


@dp.message_handler(text= "Text to Binary", state= translaterbn.translate)
async def translate_to_bn(message: types.Message):
    await message.answer("Sozni kiriting", reply_markup=ReplyKeyboardRemove() and back_markup)
    await translaterbn.to_bn.set()
    

@dp.message_handler(state=translaterbn.to_bn)
async def translate_to_bn(message: types.Message, state: FSMContext):
    text = message.text.strip() 
    if all(char.isalpha() or char.isspace() for char in text): 
        binary_text = ' '.join(format(ord(char), '08b') for char in text)
        formatted_text = f"*{text}*\n```\n{binary_text}\n```"
        await message.answer(formatted_text, parse_mode="MarkdownV2")
    else:
        await message.reply("So'z faqat harflardan iborat bo'lishi kerak. Iltimos, faqat matn kiriting!")



@dp.message_handler(text= "Binary to text", state= translaterbn.translate)
async def translate_to_bn(message: types.Message):
    await message.answer("Sozni kiriting", reply_markup=ReplyKeyboardRemove() and back_markup)
    await translaterbn.to_text.set()


@dp.message_handler(state=translaterbn.to_text)
async def translate_to_text(message: types.Message):
    binary_string = message.text.strip()

    if all(set(b) <= {"0", "1"} for b in binary_string.split()): 
        try:
            text = ''.join(chr(int(b, 2)) for b in binary_string.split())
            await message.answer(text)
        except ValueError:
            await message.reply("Xato! Binary kod noto‘g‘ri formatda kiritilgan.")
    else:
        await message.reply("So'z faqat 0 va 1 dan iborat binary tilida bo'lishi kerak.")
