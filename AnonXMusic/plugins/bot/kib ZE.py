# سورس زد إي @UI_XB 

import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



REPLY_MESSAGE = "**صلي علي اشرف خلق الله 🥹✨**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
    ],
    [
        ("افتار شباب"),
        ("افتار بنات")
    ],
    [
        ("استوريهات. 🥹")
    ],
    [
        ("النقشبندي"),
        ("قران")
    ],
    [
        ("فيلمك. 🎥")
    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("غنيلي. 🎙")
    ],
    [
        ("صوره"),
        ("انميي")
    ],
    [
        ("متحركه. 🎬")
    ],
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("الالعاب. 🔱")
    ],
    [
        ("نكته"),
        ("كتبات")
    ],
    [
        ("اذكار. 💎")
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
        ("يـوتيوب. 📽")
        
    ],
    [
        ("لو خيروك"),
        ("انصحني")
    ],
    [
        ("بوت حذف")
        
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
       ("انصحني. 🥲")
        
    ],
    [
        ("اخفاء الازرار . 🕷")
    ]
]

@app.on_message(filters.regex("^/RE"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("^اخفاء الازرار . 🕷$"))
async def down(client, message):
          m = await message.reply(" **- تم اخفاء الازرار بنجاح . 🔱\n\n- لاظهار كيب الارشادات /SENZIR   \n. 🕷**\n\n- لاظهار كيب الاعضاء والتسليه  /RE  \n. 🕷**", reply_markup= ReplyKeyboardRemove(selective=True))



@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/723228da7d6f71c929db4.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝗦َِ𝗼َِ𝗨َِ𝗿َِ𝗖َِ𝗲 َِ𝗥َِ𝗲َِ𝗙َِ𝘇🔱", url=f"https://t.me/def_Zoka"),
            ]
         ]
     )
  )

