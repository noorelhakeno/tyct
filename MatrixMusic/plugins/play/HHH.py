import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from pyrogram import filters, Client
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from MatrixMusic import app

#استارت
@app.on_message(
    filters.command(["الاوامر"],""))
async def italy(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/79a87da92fdeeef5b8c7f.mp4",
        caption=f"""✅ **مرحبا بك عزيزي** {message.from_user.mention}
     

❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰▰
 اليك قائمة اوامر سورس ميوزك العالم
لـعـرض كـيـبـورد الأعــضــاء 
»»»»»»  /nour  ««nour«« 

么 ← اوامـر الـمـجـمـوعـات .
么 ← اوامـر الـقـنـوات .
么 ← اوامـر الـبـوت .
么 ← مميزات السورس .
▰▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "✧مـجـمـوعـات✧", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "❅قـنـوات❅", callback_data=f"italycha"),
                ],[
                InlineKeyboardButton(
                        "❅✧الـبـوت✧❅", callback_data=f"italybot"),
                ],[
                InlineKeyboardButton(
                        "◁ السورس ▷", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "❅✧ مـيوزك الــعالم✧❅", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر المجموعه
@app.on_callback_query(filters.regex("italygro"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر المجموعات ♬**
❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰

么 ← لتشغيل اغنيه اكتب : تشغيل او شغل
么 ← لتشغيل فيديو اكتب : فيديو 
么 ← لأنهاء الاغنيه اكتب : ايقاف او انهاء 
么 ←لتخطي الاغنيه اكتب : تخطي .**
么 ←اذا حدث خطأ او اعادة التشغيل اكتب 
▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅:** /restart .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "❅✧الـقـنـوات❅✧", callback_data=f"italycha"),
                    InlineKeyboardButton(
                        "✧❅الـبـوت❅✧", callback_data=f"italybot"),
                ],[
                InlineKeyboardButton(
                        "✧❅السورس❅✧", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "✧❅ميــوزك الـعالم❅✧", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر القناه
@app.on_callback_query(filters.regex("italycha"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر الـقـنـوات ♬**
❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰
么 ←لتشغيل اغنيه اكتب : تشغيل او شغل 
么 ←لتشغيل فيديو اكتب : فيديو 
么 ← لأنهاء الاغنيه اكتب : ايقاف او انهاء 
么 ← لتخطي الاغنيه اكتب : تخطي 
么 ←اذا حدث خطأ او اعادة التشغيل اكتب 
▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅:** /restart .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "✧❅الـمـجـمـوعـات❅✧", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "❅✧الـبـوت✧❅", callback_data=f"italybot"),
                ],[
                InlineKeyboardButton(
                        "❅✧السورس✧❅", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "✧❅ميــوزك الـعالم✧❅", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر البوت
@app.on_callback_query(filters.regex("italybot"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر الـبـوت ♬**
❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰

么عمل اذاعه في البوت قم برد علي الاذاعه واكتب : اذاعه 
么عرض احصائيات البوت اكتب : الاحصائيات 
么عرض سرعه البوت اكتب : بينج 
么للتحكم في لغه البوت اكتب : اللغه 
么للتحكم في وضع التشغيل اكتب : الاعدادات 
么اوامر الحظر والرفع في كيبورد المطور 
▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "❅✧الـمـجـمـوعـات✧❅", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "✧❅الـقـنـوات❅✧", callback_data=f"italycha"),
                ],[
                InlineKeyboardButton(
                        "❅✧السورس✧❅", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "✧❅ميــوزك الـعالم✧❅", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر مميزات السورس
@app.on_callback_query(filters.regex("italysou"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر سورس حـسـام ♬**
   المس الامر لنسخ والاستخدام
❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰
- لعرض كليشه السورس اكتب : سورس .
- لعرض مين في الكول اليك الامر  : مين في الكول .
- لزخرفه عربي او انجلش اكتب  : فه واسم الزخرفه مثال زخرفه hossam . .
- لعرض بوت الحذف اكتب   : بوت حذف .
- لعمل كت او تويت اليك الامر  : كت او تويت .
- لعرض مطور البوت اكتب : المطور .
- لعرض اسم البوت اكتب : بوت .
- لعرض الايدي الخاص بك في الجروب او البرايفت اكتب : ا او ايدي .
- لصناعة رابط تليجراف ارسل الصوره برد عليه : تليجراف .
- لعرض لينك الجروب ارسل : لينك او رابط .
- لطباعة صوره علي التريمنال ارسل الرساله انجليزي برد عليه : طباعه .
- لترجمة نص مثال : /tr ar hossam
- لتحويل ملصق الي صورة قم برد علي الملصق : pict .
- لتحويل الصوره الي ملصق قم برد علي الملصق : stik .
- لعرض كود الملصق قم برد علي الملصق : code .
- لعرض اسمك اكتب : اسمي .
- لمعرفة معلومات شخص قم برد عليه : كشف .
- لعمل تاك للاعضاء استخدم امر : تاك .
**- لايقاف تاك للاعضاء استخدم امر
 الاغنيه اكتب : تخطي .**
么 ←اذا حدث خطأ او اعادة التشغيل اكتب 
▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅:** `/cancel` .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "✧❅الـمـجـمـوعـات✧❅", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "❅✧الـقـنـوات✧❅", callback_data=f"italycha"),
                ],[
                InlineKeyboardButton(
                        "✧❅الـبـوت❅✧", callback_data=f"italybot"),
                ],[
                    InlineKeyboardButton(
                        "✧❅مــيوزك الــعالم❅✧", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك المطورين
@app.on_callback_query(filters.regex("italydev"))
async def ayamr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""[♡] قناه الدعم للمطورين  @cr_nox
[♡]جروب الدعم للمطورين @vzo_a
[♡]قناه السورس @cr_nox""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❅✧مــطور الســورس✧❅", url=f"https://t.me/nor_o"), 
                ],[               
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
