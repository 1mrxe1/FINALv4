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
@client.on(events.NewMessage(outgoing=True, pattern=r"\.جلسة (.+)$"))
async def add_session(event):
    global phone_number_pending, phone_code_hash_pending, new_client
    phone_number = event.pattern_match.group(1)
    phone_number_pending = phone_number
    
    new_client = TelegramClient(StringSession(), api_id, api_hash)
    await new_client.connect()

    if not await new_client.is_user_authorized():
        sent_code = await new_client.send_code_request(phone_number)
        phone_code_hash_pending = sent_code.phone_code_hash
        await event.respond('⪼تم إرسال الكود. الرجاء إرسال الكود باستخدام الأمر `.رمز <الكود>` (مع مسافة بين الأرقام)', parse_mode="markdown")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.رمز (.+)$"))
async def add_code(event):
    global phone_number_pending, phone_code_hash_pending, new_client 
    if phone_number_pending is None:
        await event.respond('⪼الرجاء إرسال رقم الهاتف أولاً باستخدام الأمر `.جلسة <رقم الهاتف>`', parse_mode="markdown")
        return

    code = event.pattern_match.group(1).replace(" ", "") 
    try:
        await new_client.sign_in(phone_number_pending, code, phone_code_hash=phone_code_hash_pending)
        save_session(new_client, phone_number_pending)
        await event.respond(f'⪼تمت إضافة الجلسة لرقم الهاتف {phone_number_pending} بنجاح✅️', parse_mode="markdown")
        phone_number_pending = None
        phone_code_hash_pending = None
        new_client = None 
    except SessionPasswordNeededError:
        await event.respond('⪼يتطلب هذا الحساب تحقق بخطوتين. الرجاء إرسال كلمة المرور باستخدام الأمر `.تحقق <كلمة المرور>`', parse_mode="markdown")
    except Exception as e:
        await event.respond(f'حدث خطأ أثناء إضافة الجلسة: {str(e)}')

@client.on(events.NewMessage(outgoing=True, pattern=r"\.تحقق (.+)$"))
async def add_password(event):
    global phone_number_pending, new_client
    if phone_number_pending is None:
        await event.respond('⪼الرجاء إرسال رقم الهاتف أولاً باستخدام الأمر `.جلسة <رقم الهاتف>`', parse_mode="markdown")
        return

    password = event.pattern_match.group(1)
    try:
        await new_client.sign_in(phone_number_pending, password=password)  
        save_session(new_client, phone_number_pending)
        await event.respond(f'⪼تمت إضافة الجلسة لرقم الهاتف {phone_number_pending} بنجاح✅️', parse_mode="markdown")
        phone_number_pending = None
        new_client = None
    except Exception as e:
        await event.respond(f'⪼حدث خطأ أثناء إضافة الجلسة: {e}', parse_mode="markdown")
