from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, WebAppInfo



contact_button = KeyboardButton("Telefon raqamni Ulashish 📞",request_contact=True)
contact = ReplyKeyboardMarkup(resize_keyboard=True)
contact.add(contact_button)


main_btns = ["📥 Proekt zakaz qilish",
            "📋 Resume",
            "🎵 My beats", 
            "📦 Mening proektlarim", 
            "🎦 Kanallar", 
            "📌 Freelancer", 
            "💻 Binary language"
            ]

main_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for btn in main_btns:
    main_markup.insert(KeyboardButton(btn))
main_markup.add(KeyboardButton("✍️ Taklif yoki shikoyatlar")) 

btns = ["🤖 Telegram Bot", "💢 Web (Backend)", "🔙 Orqaga"]
change_markup =  ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for btn in btns:
    change_markup.insert(KeyboardButton(btn))


back_btn = KeyboardButton("🔙 Orqaga")
back_markup = ReplyKeyboardMarkup(resize_keyboard=True)
back_markup.add(back_btn)


button = ["🤖 Telegram Bot", "💢 Web site", "🧑🏻‍💻 kodlar", "🌐 GitHub", "🔙 Orqaga"]
my_project_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for my_btn in button:
    my_project_markup.insert(KeyboardButton(my_btn))


admin_btn = ["➕ Proekt qo'shish", "👥 Userlar", "🌇 Reklama", "✍️ Xabar jo'natish","🗑 O'chirish", "📤 Chiqish"]
admin_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for admin in admin_btn:
    admin_markup.insert(KeyboardButton(admin))


projects = ["🤖 Telegram Bot", "💢 Web site", "🔙 Orqaga"]
project_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for project in projects:
    project_markup.insert(KeyboardButton(project))


user_btn = ['👥 Foydalanuvchilar soni', '👤 kimlar foydalanadi', '🔙 Orqaga']
usr_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for user in user_btn:
    usr_markup.insert(KeyboardButton(user))


delete_btn = ["❌ Foydalanuvchilar ❌", "❌ Teleram Botlar ❌", "❌ Web sitelar ❌", "🔙 Orqaga"]
delete_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
for btn in delete_btn:
    delete_markup.insert(KeyboardButton(btn))


guruh_buttons = ["Xabar jonatish", "🔙 Orqaga"]
group_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for guruh in guruh_buttons:
    group_markup.insert(KeyboardButton(guruh))


free_btns = ["🏢 Ish joyi kerak", "👥 Hodim kerak"]
freelance_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for btn in free_btns + ["🔙 Orqaga"]:
    freelance_markup.insert(KeyboardButton(btn))


binary_change = ["Text to Binary", "Binary to text", "🔙 Orqaga"]
binary_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for binary in binary_change:
    binary_markup.insert(KeyboardButton(binary))