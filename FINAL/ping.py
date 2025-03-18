from telethon import events
import FINAL.client
from datetime import datetime

client = FINAL.client.client


@events.register(events.NewMessage(pattern=r'\.بنك$'))
async def ping(event):
    client.parse_mode = "markdown" 
    start = datetime.now()
    msg = await event.edit("سرعة الانترنيت!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"**سرعة انترنيتك!!**\n`{ms} ms`")
