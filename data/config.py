from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost/postgres"
TG_CHANNEL = "t.me/RandomMode"

BROADCAST_CHANNEL = "-1001864616211"


#1482537711:AAFbFjvkcAjo4fJ41R4Ek4GmctzBXwR7Uwg
# realbot 1482537711:AAFbFjvkcAjo4fJ41R4Ek4GmctzBXwR7Uwg
