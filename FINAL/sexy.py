from telethon import events
import asyncio

@events.register(events.NewMessage)
async def sexy(event):
    if event.fwd_from:
        return

    if event.message.text == ".احم":                                                                                                                            animation_interval = 2
        animation_ttl = range(0, 15)
        await event.edit(" كتابة وتعديل فاينل") 
        animation_chars = [
            "قصة قصيرة😜 ",
            "  😐             😕 \n/👕\         <👗\ \n 👖               /|",                                                                                       "  😉          😳 \n/👕\       /👗\ \n  👖            /|",
            "  😚            😒 \n/👕\         <👗> \n  👖             /|",                                                                                         "  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
            "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
            "  😘   😊 \n /👕\/👗\ \n   👖   /|",
            " 😳  😁 \n /|\ /👙\ \n /     / |",
            "😈    /😰\ \n<|\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
            "النهاية 😂..."
        ]

    elif event.message.text == ".غبي":
        animation_interval = 1
        animation_ttl = range(14)
        await event.edit("يتم رمي عقلك في القمامة")
        animation_chars = [
            " عقلك ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
            " عقلك ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
            " عقلك ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
            " عقلك ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
            " عقلك ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
            " عقلك ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
            " عقلك ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
            " عقلك ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
            " عقلك ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
            " عقلك ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
            " عقلك ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
            " عقلك ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
            " عقلك ➡️ 🧠\n\n           (> ^_^)>🗑",
            " عقلك ➡️ 🧠\n\n           عقل المطي  <(^_^ <)🗑",
        ]

    elif event.message.text == ".قمامة":
        animation_interval = 1
        animation_ttl = range(13)
        await event.edit("يتم رميك في القمامة")
        animation_chars = [
            " انتَ ➡️ 🧍\n\n🧍         <(^_^ <)🗑",
            " انتَ ➡️ 🧍\n\n🧍       <(^_^ <)  🗑",                                                   " انتَ ➡️ 🧍\n\n🧍     <(^_^ <)    🗑",
            " انتَ ➡️ 🧍\n\n🧍   <(^_^ <)      🗑",
            " انتَ ➡️ 🧍\n\n🧍<(^_^ <)         🗑",
            " انتَ ➡️ 🧍\n\n(> ^_^)>🧍         🗑",                                                   " انتَ ➡️ 🧍\n\n  (> ^_^)>🧍       🗑",
            " انتَ ➡️ 🧍\n\n    (> ^_^)>🧍    🗑",
            " انتَ ➡️ 🧍\n\n      (> ^_^)>🧍  🗑",
            " انتَ ➡️ 🧍\n\n        (> ^_^)>🧍🗑",
            " انتَ ➡️ 🧍\n\n          (> ^_^)>🧍🗑",                                                                                                                   " انتَ ➡️ 🧍\n\n           (> ^_^)>🗑",
            " انتَ ➡️ 🧍\n\nهذا هو مكانك الصحيح<(^_^ <)🗑",
           " انتَ ➡️ 🧍\n\nهذا هو مكانك الصحيح<(^_^ <)🗑",
        ]

    if event.message.text in [".احم", ".غبي", ".قمامة"]:
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % len(animation_chars)])
