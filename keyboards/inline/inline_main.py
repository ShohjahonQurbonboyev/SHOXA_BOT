from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn = ["💻 Codlar kanali"]
kanal = InlineKeyboardMarkup(row_width=1)
for button in btn:
    kanal.insert(InlineKeyboardButton(button, url="https://t.me/+_UVLIa2RiGBlYWI6"))