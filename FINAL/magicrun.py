from telethon import events
import FINAL.client
from FINAL.magic import Magic
import time
magic = Magic()
client = FINAL.client.client
@events.register(events.NewMessage)
async def magicrun(event):
		if event.raw_text == '.سحر':  
			time.sleep(0.3)
			for d in magic.magic:
				time.sleep(0.3)
				await event.edit(d)