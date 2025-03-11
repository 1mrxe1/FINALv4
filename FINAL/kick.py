from telethon import events
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
import FINAL.client
client = FINAL.client.client

antiflood_enabled = False
antirepeat_enabled = False

@events.register(events.NewMessage(outgoing=True, pattern=r'\.(حظر|طرد|تقييد)'))
async def runkick(event):
    await event.edit("جارٍ...")
    await event.delete()
    command = event.pattern_match.group(1)
    getmessage = await event.get_reply_message()

    if getmessage:
        targetuser = getmessage.sender_id
    else:  
        try:
            targetuser = int(event.text.split(" ", 1)[1])
        except (ValueError, IndexError):
            if event.message.entities:
                for entity in event.message.entities:
                    if hasattr(entity, 'user_id'):
                        targetuser = entity.user_id
                        break
                    elif hasattr(entity, 'username'):
                        try:
                            targetuser = (await client.get_entity(entity.username)).id
                            break
                        except ValueError:
                            await event.respond("لم يتم العثور على مستخدم بهذا الاسم.")
                            return
            else:  
                await event.respond("يرجى الرد على المستخدم لاتمام الامر")
                return

    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    getreason = event.message.raw_text.splitlines()
    replacecmd = getreason[0].replace(f".{command} ", "")
    reason = replacecmd.splitlines()[0]
    client.parse_mode = "html"

    try:
        if command == "طرد":
            await event.client.kick_participant(messagelocation, targetuser)
            action = "تم طرده"
        elif command == "حظر":
            await client(EditBannedRequest(messagelocation, targetuser, ChatBannedRights(until_date=None, view_messages=True)))
            action = "تم حظره"
        elif command == "تقييد":
            await client(EditBannedRequest(messagelocation, targetuser, ChatBannedRights(until_date=None, send_messages=True)))
            action = "تم تقييده"

        if reason:
            if f".{command}" in reason:
                await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}")
            else:
                await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}\nسبب: {reason}")
        else:
            await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}")

    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")


@events.register(events.NewMessage(outgoing=True, pattern=r'\.(الغاء الحظر|الغاء التقييد)'))
async def unrunkick(event):
    await event.edit("جارٍ...")
    await event.delete()
    command = event.pattern_match.group(1)
    getmessage = await event.get_reply_message()

    if getmessage:
        targetuser = getmessage.sender_id
    else:  
        try:
            targetuser = int(event.text.split(" ", 1)[1])
        except (ValueError, IndexError):
            if event.message.entities:
                for entity in event.message.entities:
                    if hasattr(entity, 'user_id'):
                        targetuser = entity.user_id
                        break
                    elif hasattr(entity, 'username'):
                        try:
                            targetuser = (await client.get_entity(entity.username)).id
                            break
                        except ValueError:
                            await event.respond("لم يتم العثور على مستخدم بهذا الاسم.")
                            return
            else: 
                await event.respond(". يرجى الرد على المستخدم")
                return

    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    client.parse_mode = "html"

    try:
        await client(EditBannedRequest(messagelocation, targetuser, ChatBannedRights(until_date=None, view_messages=False, send_messages=False)))

        if command == "الغاء الحظر":
            action = "تم إلغاء حظره"
        elif command == "الغاء التقييد":
            action = "تم إلغاء تقييده"

        await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}")

    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")

    client.parse_mode = "markdown"  



@events.register(events.NewMessage(outgoing=True, pattern=r'\.مغادرة القنوات'))
async def leave_channels(event):
    await event.edit("**جارٍ مغادرة القنوات...**")
    async for dialog in client.iter_dialogs():
        if dialog.is_channel and not (dialog.is_group or dialog.entity.admin_rights or dialog.entity.creator):
            await client.delete_dialog(dialog)
    await event.edit("**تم مغادرة جميع القنوات**")



@events.register(events.NewMessage(outgoing=True, pattern=r'\.مغادرة الكروبات'))
async def leave_groups(event):
    await event.edit("**جارٍ مغادرة الكروبات...**")
    async for dialog in client.iter_dialogs():
        if dialog.is_group and not (dialog.entity.admin_rights or dialog.entity.creator):
            try:
                await client.delete_dialog(dialog)
            except Exception as e:
                print(f"حدث خطأ أثناء مغادرة الكروب {dialog.name}: {e}")  # طباعة الخطأ للمساعدة في تحديد المشكلة
    await event.edit("**تم مغادرة جميع الكروبات**")

    
@events.register(events.NewMessage(outgoing=True, pattern=r'\.مغادرة الخاصة'))
async def leave_private_channels(event):
    await event.edit("**جارٍ مغادرة القنوات الخاصة...**")
    async for dialog in client.iter_dialogs():
        if dialog.is_channel and not dialog.is_group and not dialog.entity.broadcast:
            if dialog.entity.owner:
                await client.delete_dialog(dialog)  # لمغادرة القنوات التي أنت مالكها
            else:
                await client.leave_channel(dialog)  # لمغادرة القنوات التي أنت عضو فيها
    await event.edit("**تم مغادرة جميع القنوات الخاصة**")



    client.parse_mode = "markdown"  
