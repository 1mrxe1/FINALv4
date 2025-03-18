from telethon import events
import random

@events.register(events.NewMessage(pattern=r"\.تفاعل\s+(.+)", outgoing=True))
async def react(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1).lower() 

    if input_str == "سعيد":
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "(ʘ‿ʘ)",
            "(✿´‿`)",
            "=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾",
            "(*⌒▽⌒*)θ～♪",
            "°˖✧◝(⁰▿⁰)◜✧˖°",
            "✌(-‿-)✌",
            "⌒°(❛ᴗ❛)°⌒",
            "(ﾟ<|\(･ω･)/|>ﾟ)",
            "ヾ(o✪‿✪o)ｼ",
        ]
    elif input_str == "يفكر":
        emoticons = [
            "(҂⌣̀_⌣́)",
            "（；¬＿¬)",
            "(-｡-;",
            "┌[ O ʖ̯ O ]┐",
            "〳 ͡° Ĺ̯ ͡° 〵",
        ]
    elif input_str == "يلوح":
        emoticons = [
            "(ノ^∇^)",
            "(;-_-)/",
            "@(o・ェ・)@ノ",
            "ヾ(＾-＾)ノ",
            "ヾ(◍’౪`◍)ﾉﾞ♡",
            "(ό‿ὸ)ﾉ",
            "(ヾ(´・ω・｀)",
        ]
    elif input_str == "وتف":
        emoticons = [
            "༎ຶ‿༎ຶ",
            "(‿ˠ‿)",
            "╰U╯☜(◉ɷ◉ )",
            "(;´༎ຶ益༎ຶ`)♡",
            "╭∩╮(︶ε︶*)chu",
            "( ＾◡＾)っ (‿|‿)",
        ]
    elif input_str == "حب":
        emoticons = [
            "乂❤‿❤乂",
            "(｡♥‿♥｡)",
            "( ͡~ ͜ʖ ͡°)",
            "໒( ♥ ◡ ♥ )७",
            "༼♥ل͜♥༽",
        ]
    elif input_str == "مشوش":
        emoticons = [
            "(・_・ヾ",
            "｢(ﾟﾍﾟ)",
            "﴾͡๏̯͡๏﴿",
            "(￣■￣;)!?",
            "▐ ˵ ͠° (oo) °͠ ˵ ▐",
            "(-_-)ゞ゛",
        ]
    elif input_str == "ميت":
        emoticons = [
            "(✖╭╮✖)",
            "✖‿✖",
            "(+_+)",
            "(✖﹏✖)",
            "∑(✘Д✘๑)",
        ]
    elif input_str == "حزين":
        emoticons = [
            "(＠´＿｀＠)",
            "⊙︿⊙",
            "(▰˘︹˘▰)",
            "●︿●",
            "(　´_ﾉ` )",
            "彡(-_-;)彡",
        ]
    elif input_str == "كلب":
        emoticons = [
            "-ᄒᴥᄒ-",
            "◖⚆ᴥ⚆◗",
        ]
    elif input_str == "مساعدة":
        emoticons = ["""اكتب الامر (.تفاعل )مع الرياكشن\nسعيد\nيفكر\nيلوح\nوتف\nحب\n\nمشوش\nميت\nحزين\nكلب"""]

    else:    
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀̿Ĺ̯▀̿ ̿)",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons) - 1) 
    output_str = emoticons[index]
    await event.edit(output_str)
