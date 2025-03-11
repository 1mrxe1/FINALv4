from telethon import events
import FINAL.client
import asyncio
from telethon.tl.types import Message
import re
from telethon.tl.functions.channels import JoinChannelRequest

client = FINAL.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.يوت (.+)'))
async def tconv(event):
    chat = await event.get_chat()
    sentence_to_summarize = event.pattern_match.group(1)

    if sentence_to_summarize.startswith("."):
        sentence_to_summarize = sentence_to_summarize[1:].strip()

    sentence_to_summarize = "يوت " + sentence_to_summarize

    await event.edit("يرجى الانتظار...")

    x = await client.send_message('@AnimeCloudAppbot', sentence_to_summarize)

    async with client.conversation('@AnimeCloudAppbot') as conv:
        audio_clip = None
        timeout = 15
        start_time = asyncio.get_event_loop().time()

        while asyncio.get_event_loop().time() - start_time < timeout:
            response = await conv.get_response(x.id)
            await client.send_read_acknowledge(conv.chat_id)

            if "عليك الأشتراك في قناة البوت" in response.message:
                try:
                    channel_name = re.search(r"قناة البوت : (@\w+)", response.message).group(1)
                    await client(JoinChannelRequest(channel_name))
                    
                    
                    x = await client.send_message('@AnimeCloudAppbot', sentence_to_summarize) 
                    
                except Exception:
                    pass 

            if response.audio:
                audio_clip = response
                break

        if audio_clip:
            new_message = Message(
                id=0,
                peer_id=chat,
                message="",
                media=audio_clip.media,
                entities=None,
                reply_markup=None,
                ttl_period=None
            )

            await client.send_message(chat, new_message, silent=True)
            await event.delete()

            # حذف المحادثة بعد جلب النتائج مباشرة
            await client(DeleteHistoryRequest(peer='@AnimeCloudAppbot', max_id=x.id, just_clear=False, revoke=True)) 

        else:
            await event.edit("المحتوى غير موجود")




@events.register(events.NewMessage(outgoing=True, pattern='\.سوال (.*)'))
async def tco(event):
    chat = await event.get_chat()
    question = event.pattern_match.group(1)
    await event.edit("جارٍ جمع المعلومات انتظر 7 ثوان ...")

    async with client.conversation('@SAMI_PAI_BOT') as conv:
        await conv.send_message(question)

        await asyncio.sleep(7)

        # الحصول على ردين من البوت
        response1 = await conv.get_response()
        response2 = await conv.get_response()

        
        if response1.text == "⌛️ Forming a response ...":
            xx = response2  # استخدام الرسالة الثانية 
        else:
            xx = response1  # استخدام الرسالة الأولى

        text_without_links = re.sub(r'http\S+', '', xx.text)

        await client.send_read_acknowledge(conv.chat_id)
        await client.send_message(chat, text_without_links)
        await event.message.delete()









from telethon import events, types
from telethon.tl.functions.channels import JoinChannelRequest
import asyncio


@events.register(events.NewMessage(outgoing=True, pattern=r'\.حمل (.+)'))
async def download_media(event):
    chat = await event.get_chat()
    link = event.pattern_match.group(1)
    message_to_delete = await event.edit("جاري التحميل...")  # حفظ الرسالة المراد حذفها

    async with client.conversation('@aaazzjbot') as conv:
        try:
            await conv.send_message(link)

            @client.on(events.NewMessage(from_users='@aaazzjbot'))
            async def handle_response(event):
                if event.media:
                    if event.grouped_id:
                        for photo in event.media.photos:
                            await client.send_file(chat, photo)
                    else:
                        await client.send_file(chat, event.media)
                    
                    # حذف رسالة "جاري التحميل..."
                    await message_to_delete.delete() 
                    
                    # انتظار 3 ثواني قبل حذف المحادثة
                    await asyncio.sleep(3)
                    await client(DeleteHistoryRequest(peer='@aaazzjbot', max_id=event.id, just_clear=False, revoke=True))
                    
                    client.remove_event_handler(handle_response)

            try:
                await asyncio.wait_for(
                    client.loop.create_task(conv.get_response()), timeout=10
                )
            except asyncio.TimeoutError:
                await event.edit("اسف ياصديقي لم اجد شيئا")
                client.remove_event_handler(handle_response)


        except Exception as e:
            print(f"حدث خطأ: {e}")
            await event.edit(f"حدث خطأ: {e}")


def extract_channel_link(message):
    """استخراج رابط القناة من رسالة البوت باستخدام تعبير نمطي."""
    try:
        pattern = r"https?:\/\/t\.me\/[a-zA-Z0-9_@]+"
        match = re.search(pattern, message.message)
        if match:
            return match.group(0)
        return None
    except:
        return None



from telethon.tl.types import Message
from telethon.tl.functions.messages import DeleteHistoryRequest
import asyncio
import re

async def handle_conversion(event, command, media_type):
    chat = await event.get_chat()
    reply_msg = await event.get_reply_message()

    if not reply_msg:
        await event.reply("يرجى الرد على ملصق/صورة/فيديو.")
        return

    await event.edit("يتم التحويل انتظر لطفا...")

    try:
        x = await client.forward_messages('@Facnvbot', reply_msg)

        async with client.conversation('@Facnvbot') as conv:
            converted_media = None
            timeout = 15
            start_time = asyncio.get_event_loop().time()

            while asyncio.get_event_loop().time() - start_time < timeout:
                response = await conv.get_response(x.id)
                await client.send_read_acknowledge(conv.chat_id)

                if media_type == 'sticker' and response.sticker:
                    converted_media = response
                    break
                elif media_type == 'photo' and response.photo:
                    converted_media = response
                    break                
                elif media_type == 'audio' and response.audio:
                    converted_media = response
                    break

        if converted_media:
            new_message = Message(
                id=0,
                peer_id=chat,
                message="",
                media=converted_media.media,
                entities=None,
                reply_markup=None,
                ttl_period=None
            )

            await client.send_message(chat, new_message, silent=True)
            await event.delete()

            # انتظار 3 ثواني قبل حذف المحادثة
            await asyncio.sleep(3) 
            await client(DeleteHistoryRequest(peer='@Facnvbot', max_id=x.id, just_clear=False, revoke=True))

        else:
            await event.edit("حدث خطأ أثناء التحويل.")

    except Exception as e:
        print(e)
        await event.edit("حدث خطأ أثناء التحويل.")


@client.on(events.NewMessage(outgoing=True, pattern=r'\.صوره'))
async def sticker_to_photo(event):
    await handle_conversion(event, '.صوره', 'photo')

@client.on(events.NewMessage(outgoing=True, pattern=r'\.صوت'))
async def video_to_audio(event):
    await handle_conversion(event, '.صوت', 'audio')

@client.on(events.NewMessage(outgoing=True, pattern=r'\.ملصق'))
async def photo_to_sticker(event):
    await handle_conversion(event, '.ملصق', 'sticker')



from telethon import events
import asyncio

@events.register(events.NewMessage(outgoing=True, pattern=r'\.تحويل'))
async def tco1(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("يجب الرد على رسالة لاستخدام هذا الأمر.")

    chat = await event.get_chat()
    async with client.conversation('@QuotLyBot') as conv:
        await conv.forward_messages(reply)  # توجيه الرسالة للبوت
        response = await conv.get_response()  # انتظار الملصق
        
        if response.sticker:  # إذا كان الرد ملصقًا
            await client.send_message(chat, file=response.sticker)  # إرسال الملصق
            
            await asyncio.sleep(5)  # الانتظار 3 ثوانٍ
            await client.delete_messages(chat, [response.id, reply.id])  # حذف الرسائل من الطرفين

        else:
            await event.respond("فشل تحويل الرسالة إلى ملصق.")