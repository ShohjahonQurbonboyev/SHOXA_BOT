from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn = ["💻 Codlar kanali"]
kanal = InlineKeyboardMarkup(row_width=1)
for button in btn:
    kanal.insert(InlineKeyboardButton(button, url="https://t.me/+_UVLIa2RiGBlYWI6"))


button_name = ["🎬 Kinolar"]
kino_kanal = InlineKeyboardMarkup(row_width=1)
for buttonk in button_name:
    kino_kanal.insert(InlineKeyboardButton(buttonk, url="https://t.me/virtual_cinema0512"))

buttn = ["ha", "yo'q"]
tasdiq =InlineKeyboardMarkup(row_width=2)
for butn in buttn:
    tasdiq.insert(InlineKeyboardButton(butn, callback_data=butn))