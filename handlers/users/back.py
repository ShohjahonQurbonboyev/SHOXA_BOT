
from aiogram import types
from loader import dp
from keyboards.default.main_btn import  main_markup, change_markup, back_markup, admin_markup, project_markup, freelance_markup, binary_markup
from states.main_state import translaterbn, shikoyatstate, main, changestate, reklamastate, myprojects, adminstate, adminwebstate, deletestate,adminusrstate, freelancer, hodim, send_msg





@dp.message_handler(text ="📤 Chiqish", state=adminstate.admin_menu)
async def main_redirect(message: types.Message):
    await message.answer("Siz Asosiy menuga qaytdingiz 🏚", reply_markup= main_markup)
    await main.main_menu.set()




@dp.message_handler(text ="🔙 Orqaga", state=changestate.change)
async def main_redirect(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup= main_markup)
    await main.main_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state=changestate.bot)
async def change_redirect(message: types.Message):
    await message.answer("Qanday proekt zakaz qilmoqchisiz ?", reply_markup=change_markup)
    await changestate.change.set()



@dp.message_handler(text ="🔙 Orqaga", state=changestate.web)
async def bot_redirect(message: types.Message):
    await message.answer("Qanday proekt zakaz qilmoqchisiz ?", reply_markup=change_markup)
    await changestate.change.set()


@dp.message_handler(text ="🔙 Orqaga", state=reklamastate.sorov)
async def reklama_back(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup=admin_markup)
    await adminstate.admin_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state = myprojects.change)
async def change_back(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup=main_markup)
    await main.main_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminstate.password)
async def change_back(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup=main_markup)
    await main.main_menu.set()



@dp.message_handler(text ="🔙 Orqaga", state = adminstate.change_prject)
async def change_back(message: types.Message):
    await message.answer("Siz admin menusidasiz !", reply_markup=admin_markup)
    await adminstate.admin_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminstate.name)
async def change_back(message: types.Message):
    await message.answer("Qaysi turdagi proektni qo'shmoqchisiz ?", reply_markup=project_markup)
    await adminstate.change_prject.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminstate.username)
async def change_back(message: types.Message):
    await message.answer("Telegram botning nomini yozing 👇", reply_markup=back_markup)
    await adminstate.name.set()



@dp.message_handler(text ="🔙 Orqaga", state = adminwebstate.name)
async def change_back(message: types.Message):
    await message.answer("Qaysi turdagi proektni qo'shmoqchisiz ?", reply_markup=project_markup)
    await adminstate.change_prject.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminwebstate.url)
async def change_back(message: types.Message):
    await message.answer("Web sitening nomini yozing 👇", reply_markup=back_markup)
    await adminwebstate.name.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminusrstate.change_user)
async def change_back(message: types.Message):
    await message.answer("Siz admin menusidasiz !", reply_markup=admin_markup)
    await adminstate.admin_menu.set()



@dp.message_handler(text ="🔙 Orqaga", state = deletestate.change_delete)
async def change_back(message: types.Message):
    await message.answer("Siz admin menusidasiz !", reply_markup=admin_markup)
    await adminstate.admin_menu.set()



@dp.message_handler(text ="🔙 Orqaga", state = shikoyatstate.shikoyat)
async def change_back(message: types.Message):
    await message.answer("Siz admin menusidasiz !", reply_markup=main_markup)
    await main.main_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state = adminstate.write)
async def change_back(message: types.Message):
    await message.answer("Siz admin menusidasiz !", reply_markup=admin_markup)
    await adminstate.admin_menu.set()



@dp.message_handler(text ="🔙 Orqaga", state=freelancer.menu)
async def reklama_back(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup=main_markup)
    await main.main_menu.set()


@dp.message_handler(text ="🔙 Orqaga", state=freelancer.name)
async def reklama_back(message: types.Message):
    await message.answer("Siz qaysi xizmatdan foydalanmoqchisiz ?", reply_markup=freelance_markup)
    await freelancer.menu.set()


@dp.message_handler(text ="🔙 Orqaga", state=freelancer.surname)
async def reklama_back(message: types.Message):
    await message.answer("Ismingiz nima ?", reply_markup=back_markup)
    await freelancer.name.set()


@dp.message_handler(text ="🔙 Orqaga", state=freelancer.age)
async def reklama_back(message: types.Message):
    await message.answer("Familiyangiz nima ?", reply_markup=back_markup)
    await freelancer.surname.set()


@dp.message_handler(text ="🔙 Orqaga", state=freelancer.technologies)
async def reklama_back(message: types.Message):
    await message.answer("Yoshingiz nechchida?", reply_markup=back_markup)
    await freelancer.age.set()


@dp.message_handler(text ="🔙 Orqaga", state=freelancer.country)
async def reklama_back(message: types.Message):
    await message.answer("Mutahasisligingiz nima ?", reply_markup=back_markup)
    await freelancer.technologies.set()


@dp.message_handler(text ="🔙 Orqaga", state=freelancer.price)
async def reklama_back(message: types.Message):
    await message.answer("Viloyat yoki shaharni yozing ?", reply_markup=back_markup)
    await freelancer.country.set()


@dp.message_handler(text ="🔙 Orqaga", state=freelancer.maqsad)
async def reklama_back(message: types.Message):
    await message.answer("sizni qancha maosh qoniqtiradi ?", reply_markup=back_markup)
    await freelancer.price.set()


@dp.message_handler(text ="🔙 Orqaga", state=hodim.idora)
async def reklama_back(message: types.Message):
    await message.answer("Siz qaysi xizmatdan foydalanmoqchisiz ?", reply_markup=freelance_markup)
    await freelancer.menu.set()


@dp.message_handler(text ="🔙 Orqaga", state=hodim.technology)
async def reklama_back(message: types.Message):
    await message.answer("🏢 Idora nomi ?", reply_markup=back_markup)
    await hodim.idora.set()


@dp.message_handler(text ="🔙 Orqaga", state=hodim.country)
async def reklama_back(message: types.Message):
    await message.answer("<b>📚 Texnologiya:</b>\n\nTalab qilinadigan texnologiyalarni kiriting? ", reply_markup=back_markup)
    await hodim.technology.set()


@dp.message_handler(text ="🔙 Orqaga", state=hodim.manager_name)
async def reklama_back(message: types.Message):
    await message.answer("<b>🌐 Hudud:</b>\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.", reply_markup=back_markup)
    await hodim.country.set()


@dp.message_handler(text ="🔙 Orqaga", state=hodim.time)
async def reklama_back(message: types.Message):
    await message.answer("<b>✍️Mas'ul ism sharifi ?</b>", reply_markup=back_markup)
    await hodim.manager_name.set()


@dp.message_handler(text ="🔙 Orqaga", state=hodim.work_time)
async def reklama_back(message: types.Message):
    await message.answer("<b>🕰 Murojaat qilish vaqti:\n\n</b>Qaysi vaqtda murojaat qilish mumkin?\n<i>Masalan, 9:00 - 18:00</i>", reply_markup=back_markup)
    await hodim.time.set()


@dp.message_handler(text ="🔙 Orqaga", state=hodim.price)
async def reklama_back(message: types.Message):
    await message.answer("<b>Ish vaqti:</b>\n\n<i>Masalan: 9:00 - 18:00</i>", reply_markup=back_markup)
    await hodim.work_time.set()


@dp.message_handler(text ="🔙 Orqaga", state=hodim.ex_data)
async def reklama_back(message: types.Message):
    await message.answer("<b>💰 Maosh:</b>\n\nQancha maosh taklif qilasiz ?", reply_markup=back_markup)
    await hodim.price.set()



@dp.message_handler(text ="🔙 Orqaga", state=send_msg.number_msg)
async def reklama_back(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup=main_markup)
    await main.main_menu.set()



@dp.message_handler(text ="🔙 Orqaga", state=send_msg.xabar)
async def reklama_back(message: types.Message):
    await message.answer("Nima demoqchisiz ?", reply_markup=back_markup)
    await send_msg.number_msg.set()



@dp.message_handler(text ="🔙 Orqaga", state=translaterbn.translate)
async def reklama_back(message: types.Message):
    await message.answer("Siz Asosiy menudasiz 🏠", reply_markup=main_markup)
    await main.main_menu.set()



@dp.message_handler(text ="🔙 Orqaga", state=translaterbn.to_bn)
async def reklama_back(message: types.Message):
    await message.answer("Tarjima turini tanlang", reply_markup=binary_markup)
    await translaterbn.translate.set()


@dp.message_handler(text ="🔙 Orqaga", state=translaterbn.to_text)
async def reklama_back(message: types.Message):
    await message.answer("Tarjima turini tanlang", reply_markup=binary_markup)
    await translaterbn.translate.set()

