from telethon import events
from time import sleep
from urllib.request import urlopen
import json

@events.register(events.NewMessage(outgoing=True, pattern=r'\.بحث ايبي$'))
async def iptrace(event):
    getip = event.message.raw_text.split()
    messagelocation = event.to_id
    await event.edit("يبحث...")
    sleep(2)
    await event.delete()
    targetip = getip[1]
    url = "http://ip-api.com/json/"
    start = urlopen(url+targetip)
    ipdata = start.read()
    information = json.loads(ipdata)
    await event.client.send_message(messagelocation, f"هدف IP: {information['query']}\nدولة: {information['country']}\nكود الدولة: {information['countryCode']}\nمنطقة: {information['region']}\nاسم المنطقة: {information['regionName']}\nمدينة: {information['city']}\nZip: {information['zip']}\nخط العرض: {information['lat']}\nخط الطول: {information['lon']}\nوحده زمنية: {information['timezone']}\nISP: {information['isp'].عنوان()}\nمنظمة: {information['org'].عنوان()}\nASN: {information['as']}\n")

