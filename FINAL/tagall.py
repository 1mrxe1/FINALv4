from telethon import events
import FINAL.client
import asyncio
import telethon.tl.types

client = FINAL.client.client

@client.on(events.NewMessage(outgoing=True, pattern=r"(.تاك_للكل|.all)(.*)"))
async def tagall(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    client.parse_mode = "html"
    message_text = event.pattern_match.group(2).strip()
    chat = await event.get_input_chat()
    me = await client.get_me()
    permissions = await client.get_permissions(chat, me)

    if not permissions.is_admin:
        await event.respond("عذرًا، لا أملك صلاحية ذكر الجميع في هذه المجموعة.")
        return

    all_participants = await client.get_participants(chat)
    hidden_members_found = False

    async def get_members():
        for user in all_participants:
            if not user.deleted:
                try:
                    participant = await client.get_entity(user.id)
                    if not (isinstance(participant, telethon.tl.types.ChannelParticipant) and participant.is_hidden):
                        yield user
                except ValueError:
                    pass

    
    temp_mentions = []  
    async for user in get_members():
        temp_mentions.append(f"<a href='tg://user?id={user.id}'>{user.first_name}</a>")
        
        if len(temp_mentions) == 20:  
            final_mentions = ""
            if message_text:
                final_mentions += f"<b>{message_text}</b>\n"
            final_mentions += " ".join(temp_mentions) + "\n\n"
            if hidden_members_found:
                final_mentions += "(لا يمكن ذكر الأعضاء المخفيين)\n"
            await client.send_message(chat, final_mentions, parse_mode="html")
            await asyncio.sleep(1)
            
            temp_mentions = []  

  
    if temp_mentions:  
        final_mentions = ""
        if message_text:
            final_mentions += f"<b>{message_text}</b>\n"
        final_mentions += " ".join(temp_mentions) + "\n\n"
        if hidden_members_found:
            final_mentions += "(لا يمكن ذكر الأعضاء المخفيين)\n"
        await client.send_message(chat, final_mentions, parse_mode="html")
        
    client.parse_mode = "markdown"  
