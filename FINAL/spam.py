from FINAL import client
from telethon import TelegramClient, events
import asyncio

client = client.client
active_tasks = {}

@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    text = event.message.message.strip()
    chat_id = event.chat_id
    reply_to_msg_id = event.message.reply_to_msg_id
    message = event.message

    try:
        if text.startswith('.انشر ') and reply_to_msg_id:
            try:
                seconds, target = text.split(maxsplit=2)[1:]
                seconds = int(seconds)
                entity = await client.get_entity(target)
                if not hasattr(entity, 'id'):
                    raise ValueError("لم يتم العثور على يوزر أو مجموعة بهذا الاسم.")

                active_tasks['global_task'] = {
                    'type': 'انشر',
                    'seconds': seconds,
                    'target': entity,
                    'message': await event.get_reply_message()
                }
                await message.delete()
                await start_p1()
            except (ValueError, IndexError):
                await event.reply("** ⌯ خطأ، الصحيح هو: .انشر + الثواني + @اليوزر **", parse_mode="markdown")
                await message.delete()

        elif text.startswith('.نشر_كروبات ') and reply_to_msg_id:
            try:
                seconds = int(text.split()[1])
                active_tasks['global_task'] = {
                    'type': 'نشر_كروبات',
                    'seconds': seconds,
                    'message': await event.get_reply_message()
                }
                await message.delete()
                await start_p2()
            except ValueError:
                await event.reply("** ⌯ خطأ، الصحيح هو: .نشر_كروبات + الثواني **", parse_mode="markdown")
                await message.delete()

        elif text.startswith('.سوبر ') and reply_to_msg_id:
            try:
                seconds = int(text.split()[1])
                dialogs = await client.get_dialogs()
                supergroups = [
                    dialog.entity for dialog in dialogs
                    if dialog.is_group and ("سوبر" in dialog.name or "super" in dialog.name.lower())
                ]
                active_tasks['global_task'] = {
                    'type': 'سوبر',
                    'seconds': seconds,
                    'supergroups': supergroups,
                    'message': await event.get_reply_message()
                }
                await message.delete()
                await start_p3()
            except ValueError:
                await event.reply("** ⌯ خطأ، الصحيح هو: .سوبر + الثواني **", parse_mode="markdown")
                await message.delete()

        elif text.startswith('.تناوب ') and reply_to_msg_id:
            try:
                seconds = int(text.split()[1])
                dialogs = await client.get_dialogs()
                groups = [dialog.entity for dialog in dialogs if dialog.is_group]
                active_tasks['global_task'] = {
                    'type': 'تناوب',
                    'seconds': seconds,
                    'groups': groups,
                    'message': await event.get_reply_message()
                }
                await message.delete()
                await start_p4()
            except ValueError:
                await event.reply("** ⌯ خطأ، الصحيح هو: .تناوب + الثواني **", parse_mode="markdown")
                await message.delete()

        elif text.startswith('.بلش ') and reply_to_msg_id:
            try:
                seconds = int(text.split()[1])
                active_tasks['global_task'] = {
                    'type': 'بلش',
                    'seconds': seconds,
                    'chat_id': chat_id,
                    'message': await event.get_reply_message()
                }
                await message.delete()
                await start_p5()
            except ValueError:
                await event.reply("** ⌯ خطأ، الصحيح هو: .بلش + الثواني **", parse_mode="markdown")
                await message.delete()

        elif text == '.ايقاف النشر':
            if 'global_task' in active_tasks:
                del active_tasks['global_task']
                await event.reply("** ⌯ تم إيقاف جميع عمليات النشر بنجاح. **", parse_mode="markdown")
            else:
                await event.reply("** ⌯ لا يوجد نشر جاري حالياً لإيقافه. **", parse_mode="markdown")
            await message.delete()

        elif text == '.م11':
            final_commands = """**      
    ⌯—————  اوامر النشر —————⌯

    `.انشر+ثواني+معرف` : لمجموعة محددة  

    `.نشر_كروبات+ثواني` : لكل المجموعات  

    `.سوبر+ثواني` : لكل السوبرات  

    `.تناوب+ثواني` : للنشر بالتناوب  

    `.خاص` : اذاعة للخاص  

    `.بلش+ثواني` : لتكرار الرسالة  

    `.ايقاف النشر` : لإيقاف جميع أنواع النشر أعلاه  

    • مُـلاحظة : جميع الأوامر أعلاه تستخدم بالرد على الرسالة.  
    • مُـلاحظة : جميع الأوامر أعلاه تستقبل صورة واحدة.  
    **"""
            await event.respond(final_commands, parse_mode="markdown")
            await asyncio.sleep(2)
            await message.delete()

        elif text == '.خاص' and reply_to_msg_id:
            try:
                message_to_send = await event.get_reply_message()
                peer_list = []

                async for dialog in client.iter_dialogs():
                    if dialog.is_user:
                        peer_list.append(dialog.entity)

                active_tasks['global_task'] = {
                    'type': 'خاص',
                    'peers': peer_list,
                    'message': message_to_send
                }
                await message.delete()
                await start_p6()
            except Exception as e:
                print(f"An error occurred in .خاص: {e}")
                await event.reply("** ⌯ حدث خطأ غير متوقع. **", parse_mode="markdown")
                await message.delete()


    except Exception as e:
        print(f"An error occurred: {e}")
        await event.reply("** ⌯ حدث خطأ غير متوقع. **", parse_mode="markdown")
        await message.delete()


async def start_p1():
    task = active_tasks.get('global_task')
    if task:
        while 'global_task' in active_tasks:
            try:
                await client.send_message(task['target'].id, task['message'])
                await asyncio.sleep(task['seconds'])
            except Exception as e:
                print(f"Error in start_p1: {e}")
                break

async def start_p2():
    task = active_tasks.get('global_task')
    if task:
        while 'global_task' in active_tasks:
            try:
                dialogs = await client.get_dialogs()
                for dialog in dialogs:
                    if dialog.is_group:
                        try:
                            await client.send_message(dialog.entity.id, task['message'])
                        except Exception as e:
                            print(f"Error sending to group {dialog.entity.id}: {e}")
                await asyncio.sleep(task['seconds'])
            except Exception as e:
                print(f"General error in start_p2: {e}")
                break

async def start_p3():
    task = active_tasks.get('global_task')
    if task:
        while 'global_task' in active_tasks:
            try:
                for supergroup in task['supergroups']:
                    await client.send_message(supergroup.id, task['message'])
                await asyncio.sleep(task['seconds'])
            except Exception as e:
                print(f"Error in start_p3: {e}")
                break

async def start_p4():
    task = active_tasks.get('global_task')
    if task:
        while 'global_task' in active_tasks:
            try:
                for group in task['groups']:
                    if 'global_task' not in active_tasks:
                        break
                    await client.send_message(group.id, task['message'])
                    await asyncio.sleep(task['seconds'])
            except Exception as e:
                print(f"Error in start_p4: {e}")
                break
async def start_p5():
    task = active_tasks.get('global_task')
    if task:
        while 'global_task' in active_tasks:
            try:
                await client.send_message(task['chat_id'], task['message'])
                await asyncio.sleep(task['seconds'])
            except Exception as e:
                print(f"Error in start_p5: {e}")
                break

async def start_p6():
    task = active_tasks.get('global_task')
    if task:
        try:
            for peer in task['peers']:
                await client.send_message(peer, task['message'])
            del active_tasks['global_task']
        except Exception as e:
            print(f"Error in start_p6: {e}")

