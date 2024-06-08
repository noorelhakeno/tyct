from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="✧جــروب الدعـم✧", url= "https://t.me/cr_nox"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="✧مطور البوت✧", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="✧جـروب الدعـم✧", url=f"https://t.me/cr_nox"), 
        ],
        [
            
            InlineKeyboardButton(text="✧قـناه الـسورس✧", url=f"https://t.me/vzo_a") , 
        ],
    ]
    return buttons
