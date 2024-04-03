#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/MatrixMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/MatrixMusicBot/blob/master/LICENSE >
#
# All rights reserved.
import re
from datetime import datetime

from strings.filters import command
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from MatrixMusic import app
from MatrixMusic.core.call import Yukki
from MatrixMusic.utils import bot_sys_stats
from MatrixMusic.utils.decorators.language import language
import asyncstdlib as a
import asyncio

### Commands
TAG_COMMAND = get_command("TAG_COMMAND")
TAG_COMMAND_STOP = get_command("TAG_COMMAND_STOP")

from pyrogram.errors import FloodWait

chatQueue = []

stopProcess = False


@app.on_message(command(TAG_COMMAND)
    & filters.group
)
async def tag_all(client, message):
    global stopProcess
    try:
        has_permissions = True
        if has_permissions:
            if len(chatQueue) > 5:
                await message.reply(
                    "⛔️ | أنا أعمل بالفعل على الحد الأقصى لعدد الدردشات وهو 5 في الوقت الحالي. يرجى المحاولة مرة أخرى بعد قليل.")
            else:
                if message.chat.id in chatQueue:
                    await message.reply(
                        "🚫 | هناك بالفعل عملية جارية في هذه الدردشة. من فضلك اوقفها لبدء واحدة جديدة.")
                else:
                    chatQueue.append(message.chat.id)
                    if len(message.command) > 1:
                        inputText = message.command[1]
                    elif len(message.command) == 1:
                        inputText = ""
                    membersList = []
                    async for _, v in a.enumerate(await client.get_chat_members(message.chat.id)):
                        if v.user.is_bot == True:
                            pass
                        elif v.user.is_deleted == True:
                            pass
                        else:
                            membersList.append(v.user)
                    i = 0
                    lenMembersList = len(membersList)
                    if stopProcess: stopProcess = False
                    while len(membersList) > 0 and not stopProcess:
                        j = 0
                        text1 = f"{inputText}\n\n"
                        try:
                            while j < 10:
                                user = membersList.pop(0)
                                if user.username == None:
                                    text1 += f"{user.mention} "
                                    j += 1
                                else:
                                    text1 += f"@{user.username} "
                                    j += 1
                            try:
                                await app.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            await asyncio.sleep(1)
                            i += 10
                        except IndexError:
                            try:
                                await app.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            i = i + j
                    if i == lenMembersList:
                        await message.reply(f"✅ **| تم عمل التاك وعددهم الاعضاء {i} **.")
                    else:
                        await message.reply(
                            f"✅ **| تم بنجاح ذكر {i} أعضاء.**")
                    chatQueue.remove(message.chat.id)
        else:
            await message.reply("👮🏻 | عذرآ ، ** يمكن للمشرفين فقط ** تنفيذ هذا الأمر.")
    except FloodWait as e:
        await asyncio.sleep(e.value)


@app.on_message(command(TAG_COMMAND_STOP)
    & filters.group
)
async def tag_all_stop(client, message):
    global stopProcess
    try:
        has_permissions = True
        if has_permissions:
            if not message.chat.id in chatQueue:
                await message.reply("🥲 | لا توجد عملية جارية لإيقافها.")
            else:
                stopProcess = True
                await message.reply("🛑 | تم الايقاف بنجاح.")
        else:
            await message.reply("👮🏻 | عذرآ ، ** يمكن للمشرفين فقط ** تنفيذ هذا الأمر.")
    except FloodWait as e:
        await asyncio.sleep(e.value)

