from telethon import events, Button
import asyncio
import FINAL.client



client = FINAL.client.client
@events.register(events.NewMessage(outgoing=True, pattern=r".م(\d+)"))
async def help(event):
    await event.delete()
    messagelocation = event.to_id
    command_group = int(event.pattern_match.group(1))

    commands = {
        8: {
            "انتحال": "يقوم هذا الامر بنسخ حساب الشخص الاخر ..الامر بالرد.",
            "اعادة": "يقوم بإرجاع حسابك الى وضعه السابق."
        },
        3: {
            "اسمي | Asia/Baghdad": "يجب وضع المنطقة الزمنيه كما موضح",
            "اشكال الوقت": "لعرض اشكال ارقام الساعة .",
            "الشكل مع رقم": "مثلا .الشكل 4 سيتم تعيين هذا الشكل للساعة في اسمك.",
            "ايقاف اسمي": "لايقاف الوقت .",
            "اسم مع عدد الدقائق": "مثلا .اسم  50 يقوم هذا الامر بوضع وقت مع اسمك ولكن بعد 50 دقيقه يتوقف وحسب الوقت الذي تقوم بتعيينة", 
            "بايو مع عدد الدقائق": "سيعرض الساعة واليوم والشهر والسنة في البايو وحسب العدد كما في امر (.اسم)",
            "مؤقت": "يقوم بالعد لمدة 60 ثانية",
            "تنازلي مع الرقم": "يقوم بالعد تنازليا وحسب الوقت الذي قمت بتعيينة"
        },
        2: {
            "سوال": "مع السؤال الذي تريده وسيجيبك الذكاء الاصطناعي.",
        },
        1: {
            "يوت": "مع الجملة او الكلمة للبحث عن اغنية على يوتيوب",
            "انمي": "سيقوم هذا الامر بعرض صورة انمي عشوائية لك",
            "كت": "سيقوم هذا الامر بعرض سؤال عشوائي لك (كت تويت)"
        },
        15: {
            "انطق": "رمز اللغة مثلا ar بالرد على الجملة سيقوم بتحويلها صوت",
            "حمل": "والرابط ،  سيقوم بتحميل من جميع مواقع التواصل الاجتماعي .تيك. بنتر. فيس. انستا. تويت. يوت."
        },
        13: {
            "واو": "يستخدم لحفظ الصور والفيديوهات المؤقتة (بالرد على الصورة).",
            "حفظ الذاتية": "سيقوم هذا الامر بعد تفعيلة بحفظ الصور والفيديوهات المؤقته تلقائيا ."
        },        
        10: {
            "تقليد": "يستخدم بالرد وسيقوم بتقليد جميع رسائل الشخص",
            "الغاء التقليد": "لإيقاف تقليد رسائل الشخص."
        },  

        12: {
            "اضف اشتراك": "الامر مع معرف القناة @I0I0II  يجب ان يشترك ليتحدث معك",
            "تعطيل الاشتراك": "يقوم بتعطيل الاشتراك الاجباري الذي وضعته"
        }

    }


    if command_group in commands:
        message = ""
        for command, description in commands[command_group].items():
            message += f"~ `.{command}`\n{description}\n\n"

        await event.client.send_message(messagelocation, message)
    
  



from telethon import events
import datetime
import time

start_time = datetime.datetime.now()

@events.register(events.NewMessage(outgoing=True, pattern=r"\.فحص(?:\s|$)([\s\S]*)"))
async def hi(event):
    try:
        user = await event.client.get_me()
        name = user.first_name
        mention = f"[{name}](tg://user?id={user.id})"
        uptime = datetime.datetime.now() - start_time
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        uptime_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        start = time.time()
        await event.edit("** يتـم التـأكـد انتـظر قليلا رجاءا**")
        end = time.time()
        ping = (end - start) * 1000
        message = f"""
⋆┄─┄──┄┄⋆
⚡ NAME       ⇰ {mention}
⚡ TIME UP   ⇰ {uptime_str}
⚡ PING        ⇰ {ping:.2f}
⋆┄─┄ @i0i0ii ┄┄⋆

"""
        await event.edit(message)

    except Exception as e:
        print(f"حدث خطأ: {e}")
        await event.edit(f"حدث خطأ: \n`{e}`")


@events.register(events.NewMessage(outgoing=True, pattern="\.م5"))
async def kas(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""**

1 - `.تشغيل الرد` لتشغيل رد تلقائي تضعة انت سيظهر لكل من يقوم بمراسلتك

2 - `.كليشة الرد` لتعين كليشة الرد التلقائي [يستخدم بالرد على الرسالة]

3 - `.المخصص تشغيل` لتشغيل الردود المخصصة

4 - ` .رد ` الامر مع الرد الذي تود تخصيصة [يستعمل بالرد على اي رسالة ]

5 - ` .حذف رد` لحذف الردود التي قمت بتخصيصها سابقا

6 - ` .تعطيل الرد` لتعطيل كلاً من الردود المخصصة والرد التلقائي

7 - `.تفعيل التخزين` قم بإنشاء مجموعة جديدة بأسم (التخزين) واكتب فيها الامر وسيتم جعلها مجموعة لتخزين الرسائل

8 - ` .كتم ` سيقوم بكتم المستخدم داخل الخاص (بالرد على اي شخص)

9 - `.سماح` /`.الغاء السماح` يستخدم للسماح لشخص معين بارسال الرسائل لك بعد تشغيل الرد التلقائي

10 - `.ابلاغ` / `.الغاء الابلاغ` بالرد على  اي رساله وسيتم ارسالها للدعم مباشرة [.ابلاغ 5 مثلا بالرد على الرسالة]

**"""))
@events.register(events.NewMessage(outgoing=True, pattern="\.م4"))
async def mjm(event):
    await event.delete()
    messagelocation = event.to_id
    await event.client.send_message(messagelocation, ("""**

يجب ان تكون لديك صلاحية كافية للقيام بذلك 

تقييد - طرد - حظر -كتم
.الغاء -التقييد -الكتم -الحظر 
بالرد على المستخدم 

`.تاك_للكل` او `.all` :
- يقوم هذا الامر بعمل تاك او منشن جماعي [يمكنك وضع رسالة مع الامر]

`.كشف المحذوفين`:
- يقوم هذا الامر بعرض عدد المحذوفين في مجموعتك

`.اطرد المحذوفين`:
-يقوم هذا الامر بطرد المحذوفين من مجموعتك

⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆

`.اجمع ` + الرابط
- تضع رابط المجموعة مع الامر سيقوم بجمع الاعضاء منها 

`.اضف` + الرابط
- تضع رابط المجموعه التي تريد نقل الاعضاء اليها .وسيبدا باضافة ماجمعه سابقا
ملاحظة الامرين اجمع و اضف يستخدمان لجمع واضافة الاعضاء الظاهريين فقط

⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
`.فلش` 
- هذا الامر يقوم بازالة جميع الاعضاء من المجموعة اذا كانت لديك صلاحية كافية لفعل ذلك

#سيتم اضافة بعض الاشياء هنا قريبا .....
       **"""))


@events.register(events.NewMessage(outgoing=True, pattern="\.م7"))
async def memz(event):
    await event.delete()
    messagelocation = event.to_id
    await event.client.send_message(messagelocation, ("""**

 إليك قائمة اوامر الميمز:

1- .ميمز [الرابط ] [الكلمة] : هذا الأمر يسمح لك بإضافة ميم جديد إلى القائمة.

2- .ازالة [الكلمة] : هذا الأمر يسمح لك بحذف ميم معين من القائمة باستخدام الكلمة المرتبطة به.

3- .ازالة_البصمات : هذا الأمر يحذف جميع الميمز المحفوظة في القائمة.

4- .قائمة الميمز : يعرض لك هذا الأمر قائمة بجميع الكلمات المحفوظة للميمز.

5- .[الكلمة ] : عند كتابة النقطة متبوعة بإحدى الكلمات  المحفوظة، سيرسل الميم المرتبط بتلك الكلمة.


       **"""))


@events.register(events.NewMessage(outgoing=True, pattern="\.م14"))
async def font(event):
    await event.delete()
    messagelocation = event.to_id
    await event.client.send_message(messagelocation, ("""**

 اليك قائمة الخطوط:

1- `.خط غامق`

2- `خط مشطوب`

3- `.خط رمز`

4- `.خط بايثون`

5- `.خط برنت `

6- `.خط لافتة `

جميع الخطوط اعلاه تتوقف بكتابة نفس امر التشغيل 
مثال 

.خط غامق /تم التفعيل 
.خط غامق / تم التعطيل

       **"""))
       
@events.register(events.NewMessage(outgoing=True, pattern="\.م6"))
async def mssx(event):
    await event.delete()
    messagelocation = event.to_id
    await event.client.send_message(messagelocation, ("""**

 - `.مسح رسائلي `
 يقوم هذا الامر بمسح جميع رسائلك بنفس المحادثة
 
 - `.مسح +العدد `
 يمسح الرسائل من الطرفين للكل اذا كنت تمتلك الصلاحية وحسب العدد المحدد
 
 - `.مسح الكل `
 
 يقوم بمسح جميع الرسائل اذا كانت لديك الصلاحية لفعل ذلك 
 
 **ملاحظة :اذا كنت لاتمتلك الصلاحية لحذف الرسائل سيتم حذف الدردشة فقط من طرفك .اما رسائلك فستمسح من الطرفين 
 

       **"""))


@events.register(events.NewMessage(outgoing=True, pattern=r"(\.ياعلي|\.الاوامر)"))
async def yaali(event):
    await event.delete()
    messagelocation = event.to_id

    if event.pattern_match.group(1) == ".ياعلي":
        message = """
        ```
        ⣿⣿⣿⣿⣿⢿⠛⢛⠿⠉⠉⠉⡉⢙⣻⠻⠻⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⠟⢁⡠⠀⠄⠀⠀⠀⠉⠙⠒⠃⠾⠹⣲⡘⠿⣿⣿⣿
        ⣿⡿⠁⠀⠀⠀⠈⠛⠚⠉⠉⠛⠉⠙⠳⠖⣤⢌⡑⠂⠞⢿⣿
        ⡟⠐⠂⠅⡠⠂⠁⠀⠀⢀⣴⣦⣶⣶⣶⣦⣌⠘⢮⡔⡈⠙⣿
        ⠁⢀⠄⡈⠄⢀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⡆⠈⢣⠈⠜⣿
        ⠄⠑⡨⠈⠀⢠⣴⠿⡿⣿⣿⣿⣿⣿⣿⡿⠟⠻⡄⠈⢸⡀⠚
        ⡤⠪⠀⠀⢠⣿⣥⡴⠦⠤⠉⣙⣿⣿⠡⡔⠾⠟⣾⠀⠨⢀⠘
        ⠃⠀⠀⠀⢸⣿⣤⡠⠧⢤⡻⢼⣿⣿⣼⣿⣤⣧⣿⠀⡄⢸⠀
        ⠀⣀⠀⠀⠀⣿⣿⣿⣷⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡄⢀⢸⠀
        ⠠⡇⠀⠀⠀⢹⣿⡿⣿⣿⣏⡖⢿⣿⢓⣽⣿⣿⣿⠁⢨⢸⠀
        ⠠⠇⠀⠀⠀⠀⠫⣿⣿⠟⠉⠀⠀⠄⠀⠉⠙⢿⡟⠀⠈⠸⠀
        ⡐⡆⠀⠀⠀⠀⠀⠘⠁⠀⢀⡐⠒⠒⠢⠂⠀⠀⠂⠀⢀⠀⠀
        ⣹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢰
        ⢺⠀⠀⠀⠈⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡘
        ⡎⠀⠀⠀⠀⠄⣇⠠⢄⠀⠀⠀⠀⠀⠀⣀⡀⡄⠀⠀⠀⠀⡇
        ⠄⠀⠀⠀⠀⡇⣷⡀⠩⡇⣠⣮⣶⣿⠿⣫⡾⠀⠀⠀⠀⠀⠁
        ⠀⠀⠀⠀⠀⣷⠑⠳⠋⣾⡿⠟⣫⢵⡿⠟⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠐⠁⢀⣴⠀⣩⡖⡽⠝⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢠⣴⡏⣫⣾⠟⠉⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⣿⢟⠕⠋⢀⣠⣲⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠠⣷⠋⣠⠞⣰⣿⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⣾⠁⣼⡟⣼⡏⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⢁⣾⣯⢃⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⣿⣿⢤⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⢸⣿⣲⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⡿⣜⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⢠⡟⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠸⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


              ```
              """
    elif event.pattern_match.group(1) == ".الاوامر":
        message = """**
               ء⋆┄─┄─┄─┄@I0I0II┄─┄─┄┄┄⋆ء
        `.م1 ` ➪ اوامــر اليوتـيوب والتـرفيـه
        `.م2 ` ➪ اوامــر الذكـاء الاصـطنـاعي
        `.م3 ` ➪ اوامــر الـوقتــي
        `.م4 ` ➪ اوامــر المجمــوعــه
        `.م5 ` ➪ اوامــر الخــاص
        `.م6 ` ➪ اوامــر  المـسح
        `.م7 ` ➪ اوامــر المـيمـز
        `.م8 ` ➪ اوامــر الـانتحـال
        `.م9 ` ➪ اوامــر التســليـه
        `.م10` ➪ اوامــر التـقليد
        `.م11` ➪ اوامــر النشــر التلقــائي
        `.م12` ➪ اوامــر الاشتــراك الاجبــاري
        `.م13` ➪ اوامــر الـذاتيــة
        `.م14` ➪ اوامــر الـخطـوط
        `.م15` ➪ اوامــر الـنطق والتـحميل

         
        **"""

    await event.client.send_message(messagelocation, message)
