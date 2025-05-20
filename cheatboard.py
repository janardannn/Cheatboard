import time
import json
import pyperclip
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timedelta, timezone

# Load service account credentials
cred = credentials.Certificate("serviceAccountKey.json")

# Load databaseURL from firebase.json
database_url = "https://cheatboard-35cb3-default-rtdb.asia-southeast1.firebasedatabase.app"

# Initialize Firebase Admin SDK
firebase_admin.initialize_app(cred, {
    'databaseURL': database_url
})

# Reference to the clipboard path
ref = db.reference('clipboard')

last_text = ""

print("🚀 Clipboard listener started. Ready to transmit...")

def safe_paste(retries=5, delay=0.1):
    for _ in range(retries):
        try:
            return pyperclip.paste()
        except pyperclip.PyperclipWindowsException:
            time.sleep(delay)
    return None

# Define IST timezone (+5:30)
IST = timezone(timedelta(hours=5, minutes=30))

while True:
    try:
        current_text = safe_paste()
        if current_text is None:
            print("⚠️ Clipboard busy, retrying...")
            continue

        if current_text != last_text:
            last_text = current_text
            # Get current time in IST with tz info
            now_ist = datetime.now(IST)
            ref.update({
                "latest": current_text,
                "lastUpdated": now_ist.isoformat()
            })
            print(f"📤 Synced at IST {now_ist.isoformat()}: {current_text}")

        time.sleep(0.5)

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        time.sleep(1)
