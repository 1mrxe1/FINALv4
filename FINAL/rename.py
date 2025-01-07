import asyncio
from telethon import events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import pytz 
import FINAL

client = FINAL.client.client
update_tasks = {}
time_formats = {
    "1": "𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎",
    "2": "𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶",
    "3": "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢",
    "4": "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬",
    "5": "𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶",
    "6": "۱۲۳۴۵۶۷۸۹۰",
    "7": "١٢٣٤٥٦٧٨٩٠",
    "8": "₁₂₃₄₅₆₇₈₉₀",
    "9": "⓵⓶⓷⓸⓹⓺⓻⓼⓽⓪",
    "10": "①②③④⑤⑥⑦⑧⑨⓪",
    "11": "𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘",
    "12": "❶❷❸❹❺❻❼❽❾⓿"
}

current_time_format = "1"

async def update_name_periodically(event, user_name, timezone_str): 
    chat_id = event.chat_id
    timezone = pytz.timezone(timezone_str)  
    await event.delete() 
    while True:
        now = datetime.now(timezone)
        formatted_time = now.strftime('%I:%M')
        original_chars = "1234567890"
        formatted_chars = time_formats[current_time_format]
        for i in range(len(original_chars)):
            formatted_time = formatted_time.replace(original_chars[i], formatted_chars[i])
        try:
            await event.client(UpdateProfileRequest(last_name=formatted_time)) 
        except Exception as ex:
            print(f"حدث خطأ: {str(ex)}")
        await asyncio.sleep(55)
        if chat_id in update_tasks and not update_tasks[chat_id]:
            break

@events.register(events.NewMessage(pattern=r"\.اسمي \| (.+)", outgoing=True))
async def change_name_with_time(event):
    timezone_str = event.pattern_match.group(1) 
    chat_id = event.chat_id
    update_tasks[chat_id] = True
    me = await client.get_me()
    user_name = me.first_name
    asyncio.ensure_future(update_name_periodically(event, user_name, timezone_str))

@events.register(events.NewMessage(pattern=r"\.ايقاف اسمي$", outgoing=True))
async def stop_name_update(event):
    chat_id = event.chat_id
    if chat_id in update_tasks:
        update_tasks[chat_id] = False
        try:
            await event.client(UpdateProfileRequest(last_name="")) 
        except Exception as ex:
            print(f"حدث خطأ: {str(ex)}")
        await event.delete() 

@events.register(events.NewMessage(pattern=r"\.اشكال الوقت$", outgoing=True))
async def show_time_formats(event):
    formats_text = "\n".join([f"{key}: {value}" for key, value in time_formats.items()])
    await event.respond(f"**قائمة أشكال الوقت:**\n\n{formats_text}")
    await event.delete()

@events.register(events.NewMessage(pattern=r"\.الشكل (\d+)", outgoing=True))
async def change_time_format(event):
    global current_time_format
    try:
        format_key = event.pattern_match.group(1)
        if format_key in time_formats:
            current_time_format = format_key
            await event.respond(f"تم تغيير شكل الوقت إلى {format_key}")
        else:
            await event.respond("شكل الوقت غير موجود.")
    except Exception as e:
        print(f"حدث خطأ: {str(e)}")
    await event.delete()
