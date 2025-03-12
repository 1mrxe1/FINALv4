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

