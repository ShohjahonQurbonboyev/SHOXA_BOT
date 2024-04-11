from aiogram import types
from loader import dp, bot
from data.config import SPEECH_TO_TEXT_API_KEY
from keyboards.default.main_btn import back_markup
from states.main_state import main, gemini
from aiogram.types import ReplyKeyboardRemove
from handlers.users.functions import gemini_ai
from gtts import gTTS
import os
import assemblyai as aai






@dp.message_handler(text="🤖 GEMINI AI", state=main.main_menu)
async def gemini_start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Assalomu aleykum {full_name} siz Google tomonidan yaratilgan Sun'iy Intellekt bilan suhbatdasiz va u siz bilan faqat ingliz tilida gaplasha oladi sizga qanday yordam kerakligini ingliz tilida yozing yoki gapiring ?", reply_markup= ReplyKeyboardRemove() and back_markup)
    await gemini.gemini_chat.set()



@dp.message_handler(content_types=["text"], state=gemini.gemini_chat)
async def gemini_chat(message: types.Message):
    audio = "voices/error gemini voice.wav"
    path = "voices/response.mp3" 
    try:
        # Inform user about processing the answer
        msg = await message.answer("Javob tayyorlanmoqda...")

        # Get response from Gemini AI
        response = gemini_ai(text=message.text)
            
        # Generate audio of the response
        tts = gTTS(text=response, lang='en')  # Corrected: use 'text' parameter
        tts.save("response.mp3")
            
        # Send audio message to the user
        await message.answer_voice(voice=open("response.mp3", "rb"))
        await message.answer(response)
        await msg.delete()

        # Delete the temporary audio file
        os.remove("response.mp3")  # Added: delete the temporary file

    except Exception as ex:
        # Handle different exception types
        if IndexError:
            await message.answer(f"Kechirasiz Men sizning savolngizga tushunmadim")
            with open(audio, "rb") as audio:
                await message.answer_voice(voice= audio)
                await msg.delete()
        else:
            await message.answer(f'Xatolik yuz berdi: {ex}\nIltimos adminga xabar bering !')
            await msg.delete()


@dp.message_handler(content_types=["voice"], state=gemini.gemini_chat)
async def gemini_chat(message: types.Message):
    audio = "voices/error gemini voice.wav"
    try:
        msg = await message.answer("Javob tayyorlanmoqda...")
        # Faylni ".ogg" formatidan ".mp3" ga o'zgartiramiz
        voice_file = f"voices/user_voice.mp3"
        await message.voice.download(voice_file)

        # Speech to Text API sozlamalarni o'rnatish
        aai.settings.api_key = SPEECH_TO_TEXT_API_KEY
        transcriber = aai.Transcriber()

        # Ovozni matnga o'girish
        transcript = transcriber.transcribe(voice_file)

        # Get response from Gemini AI
        response = gemini_ai(text=transcript.text)

            
        # Generate audio of the response
        tts = gTTS(text=response, lang='en')  # Corrected: use 'text' parameter
        tts.save("response.mp3")
            
        # Send audio message to the user
        await message.answer_voice(voice=open("response.mp3", "rb"))
        await message.answer(response)
        await msg.delete()

        # Faylni o'chiramiz
        os.remove(voice_file)

    except Exception as ex:
        # Handle different exception types
        if IndexError:
            await message.answer(f"Kechirasiz Men sizning savolngizga tushunmadim")
            with open(audio, "rb") as audio:
                await message.answer_voice(voice= audio)
                await msg.delete()
            if voice_file:
                os.remove(voice_file)
        else:
            await message.answer(f'Xatolik yuz berdi: {ex}\nIltimos adminga xabar bering !')
            await msg.delete()
            if  voice_file:
                os.remove(voice_file)
