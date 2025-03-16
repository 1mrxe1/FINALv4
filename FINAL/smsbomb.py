from telethon import events
from gtts import gTTS
import FINAL.client
from os import remove

client = FINAL.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.انطق'))
async def runj(event):
    await event.delete()
    language = event.message.raw_text.split()
    getmessage = await event.get_reply_message()
    messagelocation = event.to_id
    filename = "FINAL-userbot.mp3"
    try:
        createtts = gTTS(text=f"{getmessage.message}", lang=f"{language[1]}", slow=False)
        createtts.save(filename)
        await client.send_file(messagelocation, filename)
        remove(filename)
    except:
        pass
