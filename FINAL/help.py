from telethon import events, Button
import asyncio
import FINAL.client



client = FINAL.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def help(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""**



 
༺☠️༻ FꙆ R E E U S E R B O T ༺☠️༻

┊ ✦ [1] `.اوامر الادمن` لاستعراض اوامر المجموعات والادمن

┊ ✦ [2] `.اوامر الخاص` لاستعراض اوامر الخاص والمحادثات الفردية

┊ ✦ [3] `.تسلية` لاستعراض اوامر التسلية والترفيه

┊ ✦ [4]  `.النشر` لاستعراض اوامر النشر بانواعة

┊ ✦ [5] الأمر `.واو` يستخدم لحفظ الصور والفيديوهات المؤقتة (بالرد على الصورة).

┊ ✦ [6] الأمر `.اسمي` / `.ايقاف اسمي` لوضع اسمك مع ساعة (الأمر مع الاسم الذي تريده).

┊ ✦ [7] `.تقليد` / `.الغاء التقليد ` يستخدم بالرد وسيقوم بتقليد جميع رسائل الشخص مهما كانت

┊ ✦ [8] `.انتحال`/`.اعادة` يستخدم بالرد على الشخص لانتحاله 

┊ ✦ [9] `.اوامر الميمز` لعرض قائمة اوامر الميمز

┊ ✦ [10] `.سؤال` مع السؤال الذي تريده وسيجيبك الذكاء الاصطناعي 7 ثوان انتظار قبل الاجابة

┊ ✦ [11] `.يوت` مع الجملة او الكلمة للبحث عن اغنية على يوتيوب

┊ ✦ [12] `.انطق` رمز اللغة مثلا ar بالرد على الجملة سيقوم بتحويلها صوت

┊ ✦ [13] `.ابلاغ`/`.ايقاف الابلاغ` ...ابلاغ مع الوقت  بالرد على اي رسالة ستذهب مباشرة للدعم

┊ ✦ [14] `.الخطوط` سيعرض لك قائمة الخطوط


╰༺☠️༻ @I0I0II ༺☠️༻╯

**"""))
















@events.register(events.NewMessage(outgoing=True, pattern=".فحص"))
async def hi(event):
    await event.delete()

    chat = await event.get_chat()

    animation_path = "https://t.me/N1NN_N/8"
    animation_caption = "كل شيء يعمل جيدا ياصديقي اكتب `.الاوامر`"

    animation_message = await event.client.send_file(chat, animation_path) 

    words = animation_caption.split()

    for i in range(len(words)):
        caption_text = " ".join(words[:i+1])

        await event.client.edit_message(animation_message, caption_text) 

        await asyncio.sleep(0.4) 









@events.register(events.NewMessage(outgoing=True, pattern=".اوامر الخاص"))
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

8 - ` .اضف اشتراك`/`.تعطيل الاشتراك` الامر مع معرف القناة @I0I0II  يجب ان يشترك ليتحدث معك

9 - ` .كتم ` سيقوم بكتم المستخدم داخل الخاص (بالرد على اي شخص)

10 - `.سماح` /`.الغاء السماح` يستخدم للسماح لشخص معين بارسال الرسائل لك بعد تشغيل الرد التلقائي

**"""))
@events.register(events.NewMessage(outgoing=True, pattern=".اوامر الادمن"))
async def mjm(event):
    await event.delete()
    messagelocation = event.to_id
    await event.client.send_message(messagelocation, ("""**

يجب ان تكون لديك صلاحية كافية للقيام بذلك 

تقييد - طرد - حظر -كتم
.الغاء -التقييد -الكتم -الحظر 
بالرد على المستخدم 
       **"""))


@events.register(events.NewMessage(outgoing=True, pattern=".اوامر الميمز"))
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


@events.register(events.NewMessage(outgoing=True, pattern=".الخطوط"))
async def font(event):
    await event.delete()
    messagelocation = event.to_id
    await event.client.send_message(messagelocation, ("""**

 إليك قائمة اوامر الميمز:

1- `.خط غامق`

2- `.خط رمز`

3- `.خط برنت `

4- `.خط بايثون`

5- `.خط مشطوب`

6- `خط مائل`

* ملاحظة جميع الاوامر اعلاه تتعطل بكتابة نفس الامر 
مثال : خط غامق /تم التفعيل
خط غامق / تم التعطيل 


       **"""))

