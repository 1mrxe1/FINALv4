from telethon import events
from telethon.tl.functions.channels import DeleteMessagesRequest, EditBannedRequest
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights, Channel, InputPeerUser

import FINAL.client
client = FINAL.client.client

muted_users = {}

@events.register(events.NewMessage(pattern=r'.تقييد (\d+)', outgoing=True))
async def mute(event: events.NewMessage.Event):
    chat = await event.get_chat()
    user_id = int(event.pattern_match.group(1))

    try:
        rights = ChatBannedRights(
            until_date=None,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True,
            send_polls=True
        )

        entity = await client.get_entity(chat.id)

        if isinstance(entity, Channel):  
            await client(EditBannedRequest(chat.id, user_id, rights))
            await event.edit(f"تم تقييد المستخدم {user_id} في هذه القناة.")
        else: 
            me = await client.get_me()
            my_permissions = await client.get_permissions(chat, me)

            if my_permissions.is_admin:  
                muted_users[user_id] = chat.id
                await event.edit(f"سيتم حذف رسائل المستخدم {user_id} في هذه الدردشة.")
            else:
                await event.edit("لا يمكنني كتم المستخدمين في هذه الدردشة.")

        await event.delete()

    except Exception as e:
        print(e)
        await event.edit('حدث خطأ أثناء الكتم.')

@events.register(events.NewMessage(pattern=r'.الغاء التقييد (\d+)', outgoing=True))
async def unmute(event: events.NewMessage.Event):
    chat = await event.get_chat()
    user_id = int(event.pattern_match.group(1)) 

    try:
        rights = ChatBannedRights(
            until_date=None,
            send_messages=False,
            send_media=False,
            send_stickers=False,
            send_gifs=False,
            send_games=False,
            send_inline=False,
            embed_links=False,
            send_polls=False
        )

        entity = await client.get_entity(chat.id)

        if isinstance(entity, Channel):
            await client(EditBannedRequest(chat.id, user_id, rights))
        else:
            user_to_unmute = InputPeerUser(user_id, 0)
            await client(EditChatDefaultBannedRightsRequest(peer=user_to_unmute, banned_rights=rights))
            if user_id in muted_users:
                del muted_users[user_id] 

        await event.delete()

    except Exception as e:
        print(e)
        await event.edit('حدث خطأ أثناء السماح.')

@events.register(events.NewMessage)
async def delete_muted_messages(event):
    if event.sender_id in muted_users:
        chat_id = muted_users[event.sender_id]
        await client(DeleteMessagesRequest(chat_id, [event.id])) 

