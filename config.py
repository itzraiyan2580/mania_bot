import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7320481042:AAGgX0ouoanqS8Z7ksMGAEAlKa8FGaX8E7w")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26684254"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fc836096a68be3a4fcd7594cb3d9326f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002167789493"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6161189904"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://narutouzumaki22551:narutouzumaki22551@cluster0.econe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002026477147"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get('START_MESSAGE', '<b>ʜᴇʟʟᴏ! 👋 {mention}\n\nɪ’ᴍ ᴀ ᴘᴏsᴛ- sʜᴀʀɪɴɢ ʙᴏᴛ ғᴏʀ <a href="https://t.me/anime_mania_0">ᴀɴɪᴍᴇ ᴍᴀɴɪᴀ</a> 🎌\nᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴɪᴍᴇ? ᴊᴜsᴛ ᴄʟɪᴄᴋ ᴛʜᴇ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ʙᴜᴛᴛᴏɴ ᴏɴ ᴀɴʏ ᴘᴏsᴛ 📲\nsᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘʀᴇғᴇʀʀᴇᴅ ʀᴇsᴏʟᴜᴛɪᴏɴ, ᴀɴᴅ ʟᴇᴛ ᴛʜᴇ ᴍᴀɢɪᴄ ʜᴀᴘᴘᴇɴ 💫</b>')
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʙᴀᴋᴀ! ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴍʏ sᴇɴᴘᴀɪ's ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ᴘᴏsᴛs‼️\nᴏɴᴄᴇ ʏᴏᴜ ᴊᴏɪɴ, ʏᴏᴜ'ʟʟ ɢᴇᴛ ᴀᴄᴄᴇss ᴛᴏ ᴛʜᴇ ᴀɴɪᴍᴇ ᴘᴏsᴛs, ᴡɪᴛʜ ᴀʟʟ ᴛʜᴇ ʙᴇsᴛ ᴅᴏᴡɴʟᴏᴀᴅs ᴀɴᴅ ᴜᴘᴅᴀᴛᴇs! 🌟\nᴡʜᴀᴛ ᴀʀᴇ ʏᴏᴜ ᴡᴀɪᴛɪɴɢ ғᴏʀ? ᴊᴏɪɴ ᴜs ɴᴏᴡ⚡</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ʙᴀᴋᴀᴀᴀ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ sᴇɴᴘᴀɪ ✖</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
