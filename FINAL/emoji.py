from telethon import events 
import FINAL.client
from FINAL import emojify
client = FINAL.client.client


@events.register(events.NewMessage(outgoing=True, pattern=r"^\.ايموجي (.*)$"))
async def itachi(event):
    args = event.pattern_match.group(1)  
    if not args:
        await event.edit_or_reply(event, "اكتب الحرف أو الكلمة بعد الأمر.")
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.oofman:
            char = emojify.offman[emojify.oofman.index(a)]
            result += char
        else:
            result += a
    await event.edit(result)
