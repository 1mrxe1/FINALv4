from telethon import TelegramClient, events, sync 
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
import os
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
import os
import pickle
import sys
import asyncio
import re
from telethon import TelegramClient, Button, events
from telethon.events import CallbackQuery

api_id = 29914850
api_hash = "de7b0ee6f49fff7b4a5f0e5c015972ce"

os.system("clear")
print("""\033[031m
─────▄████▀█▄
───▄█████████████████▄
─▄█████.▼.▼.▼.▼.▼.▼▼▼▼
███████    𝙁𝙄𝙉𝘼𝙇𝙐𝙎𝙍𝘽𝙊𝙏
████████▄▄▲.▲▲▲▲▲▲▲
████████████████████▀▀


𝐃𝐞𝐯: @𝐈𝟎𝐈𝟎𝐈𝐈
""")

def get_session_filename(phone_number):
    return f'session_{phone_number}.pkl'

def load_or_create_session(phone_number, session_file=None):
    if session_file:
        try:
            with open(session_file, 'rb') as f:
                string = pickle.load(f)
            client = TelegramClient(StringSession(string), api_id, api_hash)
            print(f"\033[032mSession loaded from {session_file} successfully!")
            return client
        except FileNotFoundError:
            print(f"\033[031mSession file not found: {session_file}")
            return None
        except Exception as e:
            print(f"\033[031mError loading session from {session_file}: {e}")
            return None
    else:
        filename = get_session_filename(phone_number)
        try:
            with open(filename, 'rb') as f:
                string = pickle.load(f)
            client = TelegramClient(StringSession(string), api_id, api_hash)
            print(f"\033[032mSession for {phone_number} loaded successfully!") 
            return client
        except FileNotFoundError:
            return None

def save_session(client, phone_number):
    filename = get_session_filename(phone_number)
    with open(filename, 'wb') as f:
        pickle.dump(client.session.save(), f)
    print(f"\033[032mSession for {phone_number} saved successfully!")

def get_session_files():
    session_files = []
    for filename in os.listdir():
        if filename.startswith("session_") and filename.endswith(".pkl"):
            session_files.append(filename)
    return session_files


if len(sys.argv) > 1:
    session_file = sys.argv[1] 
    client = load_or_create_session(None, session_file)
else:
    client = None
    for filename in os.listdir():
        if filename.startswith("session_") and filename.endswith(".pkl"):
            try:
                with open(filename, 'rb') as f:
                    string = pickle.load(f)
                client = TelegramClient(StringSession(string), api_id, api_hash)
                client.connect()
                print(f"\033[032mSession loaded successfully from {filename}!")
                break
            except Exception as e:
                print(f"Error loading session from {filename}: {e}")

    if client is None or not client.is_user_authorized():
        while True:
            phone_number = input("\033[032mPlease enter your phone +964: ") 
            client = load_or_create_session(phone_number)

            if client is None:
                client = TelegramClient(StringSession(), api_id, api_hash)
                client.connect()

                if not client.is_user_authorized():
                    client.send_code_request(phone_number)
                    try:
                        client.sign_in(phone_number, input('\033[032mPlease enter the code you received: '))
                    except SessionPasswordNeededError:
                        password = input('\033[032mPlease enter your password: ')
                        client.sign_in(password=password)

                    save_session(client, phone_number)

            print(f"Session for {phone_number} started.")
            break


phone_number_pending = None
phone_code_hash_pending = None
new_client = None
installation_active = False

@client.on(events.NewMessage(pattern=r"\.تفعيل التنصيب$"))
async def enable_installation(event):
    global installation_active
    installation_active = True
    await event.respond("✅| تم تفعيل روبوت التنصيب في هذه المحادثة.\n\n🤖| مرحبًا، أنا روبوت التنصيب. سأرشدك خلال الخطوات، فقط نفذ ما أطلبه منك.")
    await asyncio.sleep(2)
    await event.respond("📱| أولًا، قم بنسخ رقم هاتفك من تيليجرام وأرسله هنا، مع التأكد أنه يبدأ بـ `+`.")

@client.on(events.NewMessage(pattern=r"\.تعطيل التنصيب$"))
async def disable_installation(event):
    global installation_active
    installation_active = False
    await event.respond("❌| تم تعطيل روبوت التنصيب في هذه المحادثة.")

@client.on(events.NewMessage())
async def handle_installation(event):
    global phone_number_pending, phone_code_hash_pending, new_client, installation_active

    if not installation_active:
        return

    if phone_number_pending is None and event.text.startswith("+"):
        phone_number_pending = event.text.strip()
        new_client = TelegramClient(StringSession(), api_id, api_hash)
        await new_client.connect()

        if not await new_client.is_user_authorized():
            sent_code = await new_client.send_code_request(phone_number_pending)
            phone_code_hash_pending = sent_code.phone_code_hash
            await event.respond(f"✅| تم إرسال رمز التحقق إلى `{phone_number_pending}`.\nرجاءً أعد إرساله هنا مع وضع مسافات بين كل رقم، مثل: `1 2 3 4 5`.")
        return

    if phone_number_pending and phone_code_hash_pending and event.text.replace(" ", "").isdigit():
        code = event.text.replace(" ", "")
        try:
            await new_client.sign_in(phone_number_pending, code, phone_code_hash=phone_code_hash_pending)
            save_session(new_client, phone_number_pending)
            await event.respond(f"🎉| تم تسجيل الدخول بنجاح لرقم الهاتف `{phone_number_pending}` ✅")
            phone_number_pending = None
            phone_code_hash_pending = None
            new_client = None
        except SessionPasswordNeededError:
            await event.respond("🔑| حسابك يتطلب التحقق بخطوتين.\nرجاءً أرسل كلمة المرور الخاصة بك داخل قوسين، مثل:\n`(MySecretP@ssword)`")
        except Exception as e:
            await event.respond(f"⚠️| حدث خطأ أثناء تسجيل الدخول: {str(e)}\n\n🔄| هل تريد إعادة المحاولة؟ أرسل `.نعم` أو `.لا`.")
        return

    if phone_number_pending and new_client:
        match = re.search(r"[(](.*?)[)]", event.text.strip())
        if match:
            password = match.group(1).strip()
            try:
                await new_client.sign_in(phone_number_pending, password=password)
                save_session(new_client, phone_number_pending)
                await event.respond(f"🎉| تم تسجيل الدخول بنجاح لرقم الهاتف `{phone_number_pending}` ✅")
                phone_number_pending = None
                new_client = None
                return
            except Exception as e:
                await event.respond(f"⚠️| حدث خطأ أثناء تسجيل الدخول: {str(e)}\n\n🔄| هل تريد إعادة المحاولة؟ أرسل `.نعم` أو `.لا`.")
        else:
            await event.respond("⚠️| الرجاء إرسال كلمة المرور بين قوسين بهذه الطريقة: `(كلمة المرور هنا)`")
        return

@client.on(events.NewMessage(pattern=r"\.نعم$"))
async def retry_verification(event):
    global phone_number_pending, phone_code_hash_pending, new_client, installation_active
    if not installation_active:
        return
    if phone_number_pending and phone_code_hash_pending and new_client:
        sent_code = await new_client.send_code_request(phone_number_pending)
        phone_code_hash_pending = sent_code.phone_code_hash
        await event.respond(f"🔄| تم إعادة إرسال رمز التحقق إلى `{phone_number_pending}`.\n\nرجاءً أعد إرساله هنا مع وضع مسافات بين كل رقم، مثل: `1 2 3 4 5`.")

@client.on(events.NewMessage(pattern=r"\.لا$"))
async def cancel_verification(event):
    global phone_number_pending, phone_code_hash_pending, new_client, installation_active
    if not installation_active:
        return
    phone_number_pending = None
    phone_code_hash_pending = None
    new_client = None
    await event.respond("❌| تم إلغاء العملية")