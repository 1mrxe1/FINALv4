from telethon import events
import FINAL.client
from FINAL.lovely import Lovely
import time
lovely = Lovely()
client = FINAL.client.client

@events.register(events.NewMessage)
async def lovelyrun(event):
    if event.raw_text == '.حب':  
        time.sleep(0.3)
        for d in lovely.lovely:
            time.sleep(0.3)
            await event.edit(d)

