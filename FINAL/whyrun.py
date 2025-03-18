import logging
logging.getLogger('telethon').setLevel(logging.CRITICAL)
from telethon import events
import FINAL.client
import random
import requests
from telethon.errors.rpcerrorlist import WebpageMediaEmptyError
client = FINAL.client.client

questions_list = [
    "حكي ودك يوصل للشخص المطلوب ؟",
    "منشن شخص تسولف معه تنسى هموم الدنيا ؟",
    "مقوله او مثل او بيت شعر قريب من قلبك؟",
    "اكثر مكان تحب تروح له ف الويكند ؟",
    "كم وجبه تآكل ف اليوم ؟",
    "كم ساعه تنام ف اليوم ؟",
    "هل وثقت ف احد و خذلك ؟",
    "كلمه تعبر عن شعورك ؟",
    "منشن شخص فاهمك ف كل شيء ؟",
    "منشن شخص تسولف معه تنسى هموم الدنيا ؟",
    "اصدقاء المواقع افضل من الواقع تتفق؟",
    "كلمه معينه م يفهمها الا اصحابك ؟",
    "كل شيء يهون الا ؟",
    "كلمه تعبر عن شعورك ؟",
    "كيف تتصرف مع شخص تكلمه في سالفه مهمه ويصرفك ومعد يرد ابداً؟",
    "ثلاث اشياء جنبك الحين ؟",
    "تشوف انو التواصل بشكل يومي من اساسيات الحب ؟",
    "نوعيات ودك ينقرضون من تويتر؟",
    "ماذا تفعل عندما تري دموع زوجتك..؟",
    "ما هي هوايتك المفضلة؟",
    "لو خيروك تسافر لأي مكان في العالم، وين بتروح؟",
    "ايش اكثر اكلة تحبها؟",
    "ايش اكثر لون تحبه؟",
    "تحب القهوة او الشاي؟",
    "ايش موقف صار لك ما تنساه؟",
    "ايش اكثر شيء يضايقك؟",
    "ايش اكثر شيء يسعدك؟",
    "ايش هي امنيتك في الحياة؟",
    "لو كان بإمكانك تغيير شيء واحد في العالم، ماذا سيكون؟",
    "هل تؤمن بالحب من اول نظرة؟",
    "هل انت شخص صباحي او مسائي؟",
    "ما هو برجك؟",
    "ما هو فيلمك المفضل؟",
    "ما هي اغنيتك المفضلة؟",
    "ما هي فرقتك الموسيقية المفضلة؟",
    "ما هو كتابك المفضل؟",
    "ما هو مسلسل Netflix  المفضل لديك؟",
    "هل تفضل الصيف او الشتاء؟",
    "هل تفضل العيش في المدينة او الريف؟",
    "هل تفضل الكلاب او القطط؟",
    "ما هو رأيك في وسائل التواصل الاجتماعي؟",
    "ما هي نصيحتك لأي شخص يمر بيوم سيء؟",
    "ما هو الشيء الذي تفتخر به؟",
    "ما هو الشيء الذي تخاف منه؟",
    "ما هو الشيء الذي يجعلك تضحك؟",
    "ما هو الشيء الذي يجعلك تبكي؟",
    "ما هو الشيء الذي يجعلك تشعر بالامتنان؟",
    "ما هو تعريفك للسعادة؟",
    "ما هو تعريفك للنجاح؟",
    "لو كان بإمكانك امتلاك اي قوة خارقة، ماذا ستختار؟",
    "لو كان بإمكانك العودة بالزمن، الى اي فترة زمنية ستعود؟",
    "من هو مثلك الأعلى؟",
    "ما هي أكبر غلطة سويتها في حياتك؟",
    "ما هو الدرس اللي تعلمته من هذي الغلطة؟",
    "ما هي أفضل نصيحة  انعطت لك؟",
    "ايش اكثر شيء تعلمته من والديك؟",
    "ايش اكثر شيء تحبه في نفسك؟",
    "ايش اكثر شيء تكرهه في نفسك؟",
    "كيف تصف نفسك في ثلاث كلمات؟",
    "ما هو الشيء الذي يميزك عن غيرك؟",
    "ما هي طموحاتك المستقبلية؟",
    "ما هو الشيء الذي تتمنى تحقيقه قبل ما تموت؟",
    "هل تؤمن بالحياة بعد الموت؟",
    "هل تؤمن بالأشباح؟",
    "هل تؤمن بالكائنات الفضائية؟",
    "ما هو رأيك في الذكاء الاصطناعي؟",
    "هل تعتقد أن الروبوتات ستسيطر على العالم؟",
    "ما هو الشيء الذي يجعلك تشعر بالغضب؟",
    "ما هو الشيء الذي يجعلك تشعر بالخجل؟",
    "ما هو الشيء الذي يجعلك تشعر بالذنب؟",
    "ما هو الشيء الذي يجعلك تشعر بالخوف؟",
    "ما هو الشيء الذي يجعلك تشعر بالحزن؟",
    "ما هو الشيء الذي يجعلك تشعر بالوحدة؟",
    "ما هو الشيء الذي يجعلك تشعر بالقلق؟",
    "ما هو الشيء الذي يجعلك تشعر بالإحباط؟",
    "ما هو الشيء الذي يجعلك تشعر بالملل؟",
    "ما هو الشيء الذي يجعلك تشعر بالتعب؟",
    "ما هو الشيء الذي يجعلك تشعر بالجوع؟",
    "ما هو الشيء الذي يجعلك تشعر بالعطش؟",
    "ما هو الشيء الذي يجعلك تشعر بالنعاس؟",
    "ما هو الشيء الذي يجعلك تشعر بالبرد؟",
    "ما هو الشيء الذي يجعلك تشعر بالحر؟",
    "ما هو الشيء الذي يجعلك تشعر بالألم؟",
    "ما هو الشيء الذي يجعلك تشعر بالراحة؟",
    "ما هو الشيء الذي يجعلك تشعر بالحب؟",
    "ما هو الشيء الذي يجعلك تشعر بالكراهية؟",
    "ما هو الشيء الذي يجعلك تشعر بالغيرة؟",
    "ما هو الشيء الذي يجعلك تشعر بالحسد؟",
    "ما هو الشيء الذي يجعلك تشعر بالندم؟",
    "ما هو الشيء الذي يجعلك تشعر بالذل؟",
    "ما هو الشيء الذي يجعلك تشعر بالمهانة؟",
    "ما هو الشيء الذي يجعلك تشعر بالظلم؟",
    "ما هو الشيء الذي يجعلك تشعر بالغفران؟",
    "ما هو الشيء الذي يجعلك تشعر بالشكر؟",
    "ما هو الشيء الذي يجعلك تشعر بالاحترام؟",
    "ما هو الشيء الذي يجعلك تشعر بالتقدير؟",
    "ما هو الشيء الذي يجعلك تشعر بالثقة؟",
    "ما هو الشيء الذي يجعلك تشعر بالأمان؟",
    "ما هو الشيء الذي يجعلك تشعر بالسعادة؟"
]


image_links = [
    "https://t.me/CNN9N/10",
    "https://t.me/CNN9N/11",
    "https://t.me/CNN9N/12",
    "https://t.me/CNN9N/13",
    "https://t.me/CNN9N/14",
    "https://t.me/CNN9N/15",
    "https://t.me/CNN9N/16",
    "https://t.me/CNN9N/17",
    "https://t.me/CNN9N/18",
    "https://t.me/CNN9N/19",
    "https://t.me/CNN9N/20",
    "https://t.me/CNN9N/21",
    "https://t.me/CNN9N/22",
    "https://t.me/CNN9N/23",
    "https://t.me/CNN9N/24",
    "https://t.me/CNN9N/25",
    "https://t.me/CNN9N/26",
    "https://t.me/CNN9N/27",
    "https://t.me/CNN9N/28",
    "https://t.me/CNN9N/29",
    "https://t.me/CNN9N/30",
    "https://t.me/CNN9N/31",
    "https://t.me/CNN9N/32",
    "https://t.me/CNN9N/33",
    "https://t.me/CNN9N/34",
    "https://t.me/CNN9N/35",
    "https://t.me/CNN9N/36",
    "https://t.me/CNN9N/37",
    "https://t.me/CNN9N/38",
    "https://t.me/CNN9N/39",
    "https://t.me/CNN9N/40",
    "https://t.me/CNN9N/41",
    "https://t.me/CNN9N/42",
    "https://t.me/CNN9N/43",
    "https://t.me/CNN9N/44",
    "https://t.me/CNN9N/45",
    "https://t.me/CNN9N/46",
    "https://t.me/CNN9N/47",
    "https://t.me/CNN9N/48",
    "https://t.me/CNN9N/49",
    "https://t.me/CNN9N/50",
    "https://t.me/CNN9N/51",
    "https://t.me/CNN9N/52",
    "https://t.me/CNN9N/53",
    "https://t.me/CNN9N/54",
    "https://t.me/CNN9N/55",
    "https://t.me/CNN9N/56",
    "https://t.me/CNN9N/57",
    "https://t.me/CNN9N/58",
    "https://t.me/CNN9N/59",
    "https://t.me/CNN9N/60",
    "https://t.me/CNN9N/61",
    "https://t.me/CNN9N/62",
    "https://t.me/CNN9N/63",
    "https://t.me/CNN9N/64",
    "https://t.me/CNN9N/65",
    "https://t.me/CNN9N/66",
    "https://t.me/CNN9N/67",
    "https://t.me/CNN9N/68",
    "https://t.me/CNN9N/69",
    "https://t.me/CNN9N/70",
    "https://t.me/CNN9N/71",
    "https://t.me/CNN9N/72",
    "https://t.me/CNN9N/73",
    "https://t.me/CNN9N/74",
    "https://t.me/CNN9N/75",
    "https://t.me/CNN9N/76",
    "https://t.me/CNN9N/77",
    "https://t.me/CNN9N/78",
    "https://t.me/CNN9N/79",
    "https://t.me/CNN9N/80",
    "https://t.me/CNN9N/81",
    "https://t.me/CNN9N/82",
    "https://t.me/CNN9N/83",
    "https://t.me/CNN9N/84",
    "https://t.me/CNN9N/85",
    "https://t.me/CNN9N/86",
    "https://t.me/CNN9N/87",
    "https://t.me/CNN9N/88",
    "https://t.me/CNN9N/89",
    "https://t.me/CNN9N/90",
    "https://t.me/CNN9N/91",
    "https://t.me/CNN9N/92",
    "https://t.me/CNN9N/93",
    "https://t.me/CNN9N/94",
    "https://t.me/CNN9N/95",
    "https://t.me/CNN9N/96",
    "https://t.me/CNN9N/97"
]













@events.register(events.NewMessage(outgoing=True, pattern=r"(^\.كت|\s\.كت)\b|\.انمي"))
async def why(event):
    await event.delete()
    chat = await event.get_chat()

    matched_command = event.pattern_match.string
    if matched_command == ".كت":
        message = random.choice(questions_list)
        await event.client.send_message(chat, message)

    elif matched_command == ".انمي":
        while True:
            try:
                random_image_link = random.choice(image_links)
                channel_name, message_id = random_image_link.split('/')[-2:]
                message = await client.get_messages(channel_name, ids=int(message_id))
                await client.send_message(chat, "اتمنى ان تنال اعجابك :", file=message, silent=True)
                break
            except WebpageMediaEmptyError:
                pass
