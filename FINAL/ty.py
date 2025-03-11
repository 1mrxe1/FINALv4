from telethon import events
import time

import FINAL.client
client = FINAL.client.client


@events.register(events.NewMessage(outgoing=True, pattern=r'^\.طباعة (.+)'))
async def ple(event):
    orig_text = event.pattern_match.group(1)
    text = orig_text
    pb = ""
    typing_symbol = "▒"
    while(pb != orig_text):
        try:
            await event.edit(pb + typing_symbol)
            time.sleep(0.05)
            pb += text[0]
            text = text[1:]
            await event.edit(pb)
            time.sleep(0.05)
        except Exception as e:
            print(e)
