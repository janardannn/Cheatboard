import time
import json
import pyperclip
import firebase_admin
from firebase_admin import credentials, db

# Load service account credentials
cred = credentials.Certificate("serviceAccountKey.json")

# Load databaseURL from firebase.json
with open("firebase.json", "r") as f:
    config = json.load(f)
    database_url = config.get("databaseURL")
    if not database_url:
        raise ValueError("Missing 'databaseURL' in firebase.json")

# Initialize Firebase Admin SDK
firebase_admin.initialize_app(cred, {
    'databaseURL': database_url
})

# Reference to the clipboard path
ref = db.reference('clipboard/latest')

last_text = ""

print("🚀 Clipboard listener started. Ready to transmit...")

def safe_paste(retries=5, delay=0.1):
    for _ in range(retries):
        try:
            return pyperclip.paste()
        except pyperclip.PyperclipWindowsException:
            time.sleep(delay)
    return None

while True:
    try:
        current_text = safe_paste()
        if current_text is None:
            print("⚠️ Clipboard busy, retrying...")
            continue

        if current_text != last_text:
            last_text = current_text
            ref.set(current_text)
            print("📤 Synced:", current_text)

        time.sleep(0.5)


    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        time.sleep(1)
