import base64
import asyncio
from telethon import events
from asyncio import sleep
from telethon.sync import TelegramClient
from telethon import events
from telethon.events import NewMessage
from FINAL import client
import re

finalll = client.client

final = False
async def final_nshr(finalll, sleeptimet, chat, message, seconds):
    global final
    final = True
    while final:
        try:
            if message.media:
                await finalll.send_file(chat, message.media, caption=message.text)
            else:
                await finalll.send_message(chat, message.text)

            await asyncio.sleep(sleeptimet)

        except (ConnectionError, ReadTimeoutError):
            await finalll.disconnect()
            await finalll.connect()
            continue

        except Exception as e:
            print(f"An unexpected error occurred: {e}") 

async def final_allnshr(finalll, sleeptimet, message):
    global final
    final = True
    while final:
        try:
            final_chats = await finalll.get_dialogs()
            for chat in final_chats:
                if chat.is_group:
                    try:
                        if message.media:
                            await finalll.send_file(chat.id, message.media, caption=message.text)
                        else:
                            await finalll.send_message(chat.id, message.text)
                    except Exception as e:
                        print(f"Error in sending message to chat {chat.id}: {e}")
            await asyncio.sleep(sleeptimet)
        except Exception as e:
            print(f"Error in final_allnshr: {e}")

super_groups = ["super", "سوبر"]
async def final_supernshr(finalll, sleeptimet, message):
    global final
    final = True
    while final:
        try:
            final_chats = await finalll.get_dialogs()
            for chat in final_chats:
                chat_title_lower = chat.title.lower()
                if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                    try:
                        if message.media:
                            await finalll.send_file(chat.id, message.media, caption=message.text)
                        else:
                            await finalll.send_message(chat.id, message.text)
                    except Exception as e:
                        print(f"Error in sending message to chat {chat.id}: {e}")
            await asyncio.sleep(sleeptimet)
        except Exception as e:
            print(f"Error in final_supernshr: {e}")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("**▪︎|يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا.**", parse_mode="md")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    finalll = event.client
    global final
    final = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await finalll.get_entity(chat_username)
            await final_nshr(finalll, seconds, chat.id, message, seconds)
        except Exception as e:
            await event.reply(f"**▪︎|لا يمكن العثور على المجموعة او الدردشة {chat_username}: {str(e)}**", parse_mode="md")
        await asyncio.sleep(1)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_كروبات (\d+)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("**▪︎|يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا.**", parse_mode="md")
    finalll = event.client
    global final
    final = True
    await final_allnshr(finalll, sleeptimet, message)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("**▪︎|يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا.**", parse_mode="md")
    finalll = event.client
    global final
    final = True
    await final_supernshr(finalll, sleeptimet, message)

@finalll.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_final(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    global final
    final = False
    await event.edit("**▪︎|تم ايقاف النشر التلقائي بنجاح.**", parse_mode="md")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.(م11)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    if event.pattern_match.group(1) == "م11":
        final_commands = """**

 <━━━[★] اوامر النشــر[★]━━━>
 
`.نشر+ثواني+معرف` : لمجموعة محددة

`.نشر_كروبات+ثواني` :لكل المجموعات 

`.سوبر+ثواني` : لكل السوبرات

`.تناوب+ثواني` : للنشر بالتناوب 

`.خاص` : اذاعة للخاص

`.بلش+ثواني` : لتكرار الرسالة

`.سبام` | `.وسبام` | `.نقط+ثواني` 

`.ايقاف النشر` : لأيقاف جميع انواع النشر اعلاه

• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة.

• مُـلاحظة : جميع الأوامر اعلاه تستقبل صورة واحدة.


    **"""
        await event.respond(final_commands, parse_mode="md")


@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.سبام$"))
async def spam_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("**▪︎|يجب الرد على رسالة نصية لاستخدام هذا الامر.**", parse_mode="md")

    text = message.text
    for char in text:
        await event.respond(char)
        await asyncio.sleep(0.8)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.وسبام$"))
async def word_spam_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("**▪︎|يجب الرد على رسالة نصية لاستخدام هذا الامر.**", parse_mode="md")

    words = message.text.split()
    for word in words:
        await event.respond(word)
        await asyncio.sleep(1)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.تناوب (\d+)$"))
async def rotate_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**▪︎|يجب الرد على رسالة لاستخدام هذا الامر.**", parse_mode="md")

    global final
    final = True
    chats = await finalll.get_dialogs()
    groups = [chat for chat in chats if chat.is_group]
    num_groups = len(groups)
    current_group_index = 0

    while final:
        try:
            if message.media:
                await finalll.send_file(groups[current_group_index].id, message.media, caption=message.text)
            else:
                await finalll.send_message(groups[current_group_index].id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {groups[current_group_index].id}: {e}")

        current_group_index = (current_group_index + 1) % num_groups
        await asyncio.sleep(seconds)
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.خاص$"))
async def private_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**▪︎|يجب الرد على رسالة لاستخدام هذا الامر.**", parse_mode="md")

    chats = await finalll.get_dialogs()
    private_chats = [chat for chat in chats if chat.is_user]

    for chat in private_chats:
        try:
            if message.media:
                await finalll.send_file(chat.id, message.media, caption=message.text)
            else:
                await finalll.send_message(chat.id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {chat.id}: {e}")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.نقط (\d+)$"))
async def dot_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    reply_to_msg = await event.get_reply_message()
    if not reply_to_msg:
        return await event.reply("**▪︎|يجب الرد على رسالة لاستخدام هذا الامر.**", parse_mode="md")

    global final
    final = True

    while final:
        await reply_to_msg.reply(".")
        await asyncio.sleep(seconds)

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^\.بلش (\d+)$"))
async def repeat_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**▪︎|يجب الرد على رسالة لاستخدام هذا الامر.**", parse_mode="md")

    global final
    final = True

    while final:
        await message.respond(message)
        await asyncio.sleep(seconds)
