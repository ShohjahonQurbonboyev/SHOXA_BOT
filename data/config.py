from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot Token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
USER_CHANNEL = env.str("USER_CHANNEL") # Userlar kanali
PROJECT_CHANNEL = env.str("PROJECT_CHANNEL") #Zakaz proyektlar kanali
CODE_CHANNEL = env.str("CODE_CHANNEL") #codlar kanali
PASSWORD_ADMIN = env.str("PASSWORD_ADMIN") #Admin panel kod
SHIKOYATLAR = env.str("SHIKOYATLAR")    
VAKANSIYA = env.str("VAKANSIYA")  #Telegram vakansiya kanali
LINK_GROUP = env.str("LINK_GROUP")



DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
