from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn = ["💻 Codlar kanali"]
kanal = InlineKeyboardMarkup(row_width=1)
for button in btn:
    kanal.insert(InlineKeyboardButton(button, url="https://t.me/Shoxa_coding"))



kino_kanal = InlineKeyboardMarkup(row_width=2)
kino_kanal.add(InlineKeyboardButton("🧾 Vakansiyalar", url="https://t.me/+GJf4CJrE7603NTky")),


github = InlineKeyboardMarkup(row_width=1)
github.add(InlineKeyboardButton('Github', url='https://github.com/ShohjahonQurbonboyev'))



buttn = ["ha", "yo'q"]
tasdiq =InlineKeyboardMarkup(row_width=2)
for butn in buttn:
    tasdiq.insert(InlineKeyboardButton(butn, callback_data=butn))



tugma_tasdiq = ["✅ To`g`ri", "❌ Xato"]
resume_change =InlineKeyboardMarkup(row_width=2)
for tugmalar in tugma_tasdiq:
    resume_change.insert(InlineKeyboardButton(tugmalar, callback_data=tugmalar))



admin_tasdiq = ["✅ Tasdiqlash", "❌ Inkor etish"]
tasdiq_admin =InlineKeyboardMarkup(row_width=2)
for tugma in admin_tasdiq:
    tasdiq_admin.insert(InlineKeyboardButton(tugma, callback_data=tugma))

resume_tasdiq_btn = ["Resume jo'natish", "Inkor etish"]
resume_tasdiq = InlineKeyboardMarkup(row_width=2)
for resume in resume_tasdiq_btn:
    resume_tasdiq.insert(InlineKeyboardButton(resume, callback_data=resume))



