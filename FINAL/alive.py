from telethon import events
import FINAL.client
import time
import os

client = FINAL.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.م17$'))
async def alive(event):
    client = event.client
    me = await client.get_me()
    username = me.username
    img = await client.download_profile_photo(username)
    time.sleep(0.5)
    await event.respond(f"""**
<━━━[★] اوامر التنصيب [★]━━━>

▪︎`.جلسة+رقم الهاتف` 
اكتب رقم الهاتف مع رمز الدولة
مثال : .جلسة +964770000


▪︎ `.رمز+الكود`:
ضع مسافة بين الارقام
مثال : .رمز 1 2 3 4


▪`.تحقق+الباسوورد`: 
باسوورد التحقق بخطوتين.
مثال : .تحقق gggg

▪︎||مـلاحظة لايمكنك التنصيب لاشخاص اخرين الا اذا كنت المالك الحقيقي للسيرفر. 


**""", file=img, parse_mode="markdown")
    await event.message.delete()
    os.remove(img)
