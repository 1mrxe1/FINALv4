from telethon import events
import base64
from time import sleep

@events.register(events.NewMessage(outgoing=True, pattern=r'\.تشفير$'))
async def runb64(event):
    await event.edit("wait...")
    options = event.message.raw_text.split()
    selectsecretmessage = await event.get_reply_message()
    try:
        if options[1] == "en":
            secretmessage = selectsecretmessage.message
            secretmessagebytes = secretmessage.encode("ascii")
            encodesecretmessage = base64.b64encode(secretmessagebytes)
            encodesecretmessagebytes = encodesecretmessage.decode("ascii")
            await event.edit("التشفير...")
            sleep(2)
            await event.edit(f"{encodesecretmessagebytes}")
        elif options[1] == "de":
            secretkey = selectsecretmessage.message
            secretkeybytes = secretkey.encode("ascii")
            decodesecretkey = base64.b64decode(secretkeybytes)
            decodesecretkeybytes = decodesecretkey.decode("ascii")
            await event.edit("فك التشفير...")
            sleep(2)
            await event.edit(f"الرسالة المفككة: {decodesecretkeybytes}")
        else:
            await event.edit("خطأ!!!")
    except IndexError:
        await event.edit("لكتابة ترميز او فك الترميز اكتب .تشفير بالرد على الرسالة")
    except:
        await event.edit("بعض الاخطاء!!!") 
