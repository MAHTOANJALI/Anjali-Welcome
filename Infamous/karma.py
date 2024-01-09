# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://te.legra.ph/file/f3c2ae32308fbc89f570b.jpg",
    "https://te.legra.ph/file/9270f2b5dc9207aebc12d.jpg",
    "https://te.legra.ph/file/184c312979e174a9640f4.jpg",
    "https://te.legra.ph/file/8a601822cf2d6b20633c1.jpg",
    "https://te.legra.ph/file/6f9b0d4201f4495796967.jpg",
    "https://te.legra.ph/file/d20ed1c02afca8d52168d.jpg",
    "https://te.legra.ph/file/f731c9f8b8fd1334a600a.jpg",
]

HEY_IMG = "https://te.legra.ph/file/ede897f84d395c273bb02.jpg"

ALIVE_ANIMATION = [
    "https://te.legra.ph/file/7ebd850524f808cd42ce1.mp4",
    "https://te.legra.ph/file/493767a7d0bd50d73b7a4.mp4",
    "https://te.legra.ph/file/551dfedb38e70c41da2e4.mp4",
    "https://te.legra.ph/file/fbb19a9565cc91e6ca983.mp4",
    "https://te.legra.ph/file/d701583acde71c051cd04.mp4",
    "https://te.legra.ph/file/f8814d64bd74ad4f5bbf1.mp4",
    "https://te.legra.ph/file/2f693930cf8c4131c55f0.mp4",
    "https://te.legra.ph/file/e77676261381ec4b1da31.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ ᴀɴᴊᴀʟɪ, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/+fztuVtP1frMwYTk1"),
        ib(text="SUPPORT", url="https://t.me/MAHTOxOFFICIAL"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yae-Miko* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
