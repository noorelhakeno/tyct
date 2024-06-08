import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/79a87da92fdeeef5b8c7f.mp4",
        caption=f"""✧❅▰▰ميـوزك العــالم▰▰❅✧
        Whoever humbles #himself to god will be #exalted
        ✧❅▰▰ميـوزك العــالم▰▰❅✧""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✧❅¹مــطور❅✧", url=f"https://t.me/nor_o"), 
                 InlineKeyboardButton(
                   "✧❅²مــطور❅✧",       url=f"https://t.me/N_7_K"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "❅✧قـناه السـورس✧❅", url=f"https://t.me/vzo_a"), 
                   
             ],[ 
                  InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك⚡",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["المطور نور"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("NOR_O")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس\n\n‍ ¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦bio :{usr.bio}\n\nســورس ميــوزك العـالم", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["" , "نور","مبرمج السورس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("NOR_O")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس.\n\n¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦boi :{usr.bio}\n\nسـورس مـيوزك العـالم", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



@app.on_message(
    command(["مطور السورس" , "الحاكم","احمد"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("N_7_K")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مبرمج السورس.\n\n¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦bio :{usr.bio}\n\nسـورس مـيوزك الـعالم", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



