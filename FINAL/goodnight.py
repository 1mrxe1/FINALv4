from telethon import events
import FINAL.client
client = FINAL.client
import random

gn = ["""
🌙.     *       ☄️      
🌟   .  *       .         
                       *   .      🛰     .        ✨      *
  .     *   روح نام         🚀     
      .              . . احلام سعيدة 🌙
. *       🌏 بيباي         *
                     🌙.     *       ☄️      
🌟   .  *       .         
                       *   .      🛰     .        ✨      *
"""]

@events.register(events.NewMessage(pattern=".نام"))
async def goodnight(event):
  ggn = random.choice(gn)
  return await event.edit(ggn)
