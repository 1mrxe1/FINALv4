from telethon import events
import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def help(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""**



 
༺☠️༻ FꙆ R E E U S E R B O T ༺☠️༻

┊ ✦ [1] الأمر `.طرد` يستخدم للطرد داخل المجموعة.

┊ ✦ [2] الأمر `.تشغيل الرد`/`.تعطيل الرد` يقوم بتشغيل/تعطيل الرد التلقائي للخاص.

┊ ✦ [3] الأمر `.تاك_للكل` يقوم بعمل تاك لكل أعضاء المجموعة.

┊ ✦ [4] الأمر `.ايدي` يستخدم لعرض معلومات المستخدم (بالرد على الشخص).

┊ ✦ [5] الأمر `.واو` يستخدم لحفظ الصور والفيديوهات المؤقتة (بالرد على الصورة).

┊ ✦ [6] الأمر `.اسمي` يستخدم لتغيير اسمك على شكل ساعة (الأمر مع الاسم الذي تريده).

┊ ✦ [7] الأمر `.تقييد` / `.الغاء التقييد` لتقييد المستخدم داخل المجموعات والقنوات.

┊ ✦ [8] الأمر `.اضف مجموعة التخزين` بالرد على ايدي المجموعة التي تريدها لتخزين الرسائل.

┊ ✦ [9] الأمر `.المخصص تشغيل` لتشغيل الردود المخصصة.

┊ ✦ [10] الأمر `.كليشة الرد` بالرد على أي كليشة، سيقوم بتعيينها كرسالة تظهر لكل من يقوم بمراسلتك على الخاص.

┊ ✦ [11] الأمر `.كتم` /`الغاء الكتم` يقوم بكتم المستخدم في كل مكان (بالرد على المستخدم)
┊ ✦ [12] الأمر `.رد ` (مثلا هلو) بالرد على أي رسالة مثلا "أهلا"، سيقوم بإرسال "هلو" كلما أرسل أحد إليك "أهلا".

╰༺☠️༻ 🅕🅘🅝🅐🅛 ༺☠️༻╯

* [++] اكتب `.النشر` لاستعراض أنواع النشر.

* [++] اكتب `.تسلية` لاستعراض أوامر التسلية.


Deve: @I0I0II 


**"""))

@events.register(events.NewMessage(outgoing=True, pattern=".فحص"))
async def hi(event):
    await event.delete()
    messagelocation = event.to_id

    # لك الحمد مهما استطال البلاء
    video_path = "https://t.me/N1NN_N/4"  
    video_caption = "انا والسورس في خدمتك اكتب `.الاوامر`"

    # يابقية الله
    await event.client.send_file(messagelocation, video_path, caption=video_caption)


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
7 - ` .اضف مجموعة التخزين ` بالرد على ايدي المجموعة -100
8 - ` .اضف اشتراك`/`.تعطيل الاشتراك` الامر مع معرف القناة @I0I0II  يجب ان يشترك ليتحدث معك
9 - ` .كتم ` سيقوم بكتم المستخدم داخل الخاص (بالرد على اي شخص)

**""")
@events.register(events.NewMessage(outgoing=True, pattern=".اوامر الادمن"))
async def mjm(event):
        await event.delete()
        messagelocation = event.to_id
        await event.client.send_message(messagelocation, ("""**

يجب ان تكون لديك صلاحية كافية للقيام بذلك 

تقييد - طرد - حظر -كتم
.الغاء -التقييد -الكتم -الحظر 
بالرد على المستخدم 
       **""")
      
