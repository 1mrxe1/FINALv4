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
delete_previous_message = False

import asyncio
import logging
from telethon import TelegramClient, events
from telethon.errors import (
    FloodWaitError,
    ChatWriteForbiddenError,
    UserBannedInChannelError,
    PeerIdInvalidError,
)
Force_repeat_count = False

async def reconnect(finalll, max_retries=5):
    retry_count = 0
    wait_time = 1
    while retry_count < max_retries:
        try:
            await finalll.connect()
            return True
        except (ConnectionError, ReadTimeoutError):
            await asyncio.sleep(wait_time)
            wait_time *= 2
            retry_count += 1
    return False

async def start_p1(finalll, sleeptimet, chat, message):
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
            if not await reconnect(finalll):
                break
        except (FloodWaitError, ChatWriteForbiddenError, UserBannedInChannelError, PeerIdInvalidError):
            break

async def start_p2(finalll, sleeptimet, message):
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
                        await asyncio.sleep(1)
                    except (FloodWaitError, ChatWriteForbiddenError, UserBannedInChannelError, PeerIdInvalidError):
                        pass
            await asyncio.sleep(sleeptimet)
        except (ConnectionError, ReadTimeoutError):
            if not await reconnect(finalll):
                break

super_groups = ["super", "سوبر"]
async def start_p3(finalll, sleeptimet, message):
    global final
    final = True
    while final:
        try:
            final_chats = await finalll.get_dialogs()
            for chat in final_chats:
                if chat.is_group and any(keyword in chat.title.lower() for keyword in super_groups):
                    try:
                        if message.media:
                            await finalll.send_file(chat.id, message.media, caption=message.text)
                        else:
                            await finalll.send_message(chat.id, message.text)
                        await asyncio.sleep(1)
                    except (FloodWaitError, ChatWriteForbiddenError, UserBannedInChannelError, PeerIdInvalidError):
                        pass
            await asyncio.sleep(sleeptimet)
        except (ConnectionError, ReadTimeoutError):
            if not await reconnect(finalll):
                break

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^.انشر (\d+)\s+(.+)$"))
async def start_p4(event):
    await event.delete()
    seconds_str, chat_usernames_str = event.pattern_match.groups()
    try:
        seconds = int(seconds_str)
    except ValueError:
        return await event.reply("**⪼ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا .**", parse_mode="markdown")
    chat_usernames = re.split(r"\s*\|\s*", chat_usernames_str)
    finalll = event.client
    global final
    final = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await finalll.get_entity(chat_username)
            await start_p1(finalll, seconds, chat, message)
        except:
            await event.reply(f"**⪼ لا يمكن العثور على المجموعة أو الدردشة {chat_username} .**", parse_mode="markdown")
            await event.delete()

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^.نشر_كروبات (\d+)$"))
async def start_p5(event):
    await event.delete()
    try:
        sleeptimet = int(event.pattern_match.group(1))
    except ValueError:
        return await event.reply("**⪼ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا .**", parse_mode="markdown")
    finalll = event.client
    global final
    final = True
    message = await event.get_reply_message()
    await start_p2(finalll, sleeptimet, message)
    await event.delete()

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^.سوبر (\d+)$"))
async def start_p6(event):
    await event.delete()
    try:
        sleeptimet = int(event.pattern_match.group(1))
    except ValueError:
        return await event.reply("**⪼ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا .**", parse_mode="markdown")
    finalll = event.client
    global final
    final = True
    message = await event.get_reply_message()
    await start_p3(finalll, sleeptimet, message)
    await event.delete()

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^.ايقاف النشر$"))
async def start_p6(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    global final
    final = False
    await event.reply("**⪼ تم ايقاف جميع عمليات النشر الحالية .**", parse_mode="markdown")
    await event.delete()
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^.(م11)$"))
async def start_p6(event):
    await event.delete()
    if event.pattern_match.group(1) == "م11":
        final_commands = """** 
⌯————— اوامر النشر —————⌯

`.انشر+ثواني+يوزر`: لمجموعة محددة

`.نشر_كروبات+ثواني`: لكل المجموعات

`.سوبر+ثواني`: لكل السوبرات

`.تناوب+ثواني`: للنشر بالتناوب

`.خاص`: اذاعة للخاص

`.بلش+ثواني`: لتكرار الرسالة

`.ايقاف النشر`: لإيقاف جميع أنواع النشر أعلاه

• مُـلاحظة : جميع الأوامر أعلاه تستخدم بالرد على الرسالة.
• مُـلاحظة : جميع الأوامر أعلاه تستقبل صورة واحدة. **"""
        await event.respond(final_commands, parse_mode="markdown")

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^.تناوب (\d+)$"))
async def start_p6(event):
    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**⪼ يجب الرد على رسالة لاستخدام هذا الأمر .**", parse_mode="markdown")
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
        except:
            pass
        current_group_index = (current_group_index + 1) % num_groups
        await asyncio.sleep(seconds)
        await event.delete()
@finalll.on(events.NewMessage(outgoing=True, pattern=r"^.خاص$"))
async def start_p6(event):
    await event.delete()
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**⪼ يجب الرد على رسالة لاستخدام هذا الأمر .**", parse_mode="markdown")
    chats = await finalll.get_dialogs()
    private_chats = [chat for chat in chats if chat.is_user]
    for chat in private_chats:
        try:
            if message.media:
                await finalll.send_file(chat.id, message.media, caption=message.text)
            else:
                await finalll.send_message(chat.id, message.text)
        except:
            pass
        await event.delete()

@finalll.on(events.NewMessage(outgoing=True, pattern=r"^.بلش (\d+)$"))
async def start_p6(event):
    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**⪼ يجب الرد على رسالة لاستخدام هذا الأمر .**", parse_mode="markdown")
    global final
    final = True
    while final:
        await message.respond(message)
        await asyncio.sleep(seconds)
        await event.delete()
