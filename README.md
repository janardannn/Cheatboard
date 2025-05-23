# Cheatboard — Firebase Setup & Running Guide

Welcome to **Cheatboard!** 📍 Your real-time clipboard sidekick. Follow these steps to get Firebase up and your project running smoothly.

---

## Step 1: Create a Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com).
2. Click **Add project**, name it something cool like `cheatboard`.
3. Follow the prompts to finish creating the project.

## Step 2: Setup Realtime Database

1. In the sidebar, go to **Build > Realtime Database**.
2. Click **Create Database**.
3. Choose **Start in test mode**.
4. Copy the database URL — it looks like:
   `https://your-project-id.firebaseio.com/`

## Step 3: Download Service Account Key

1. Go to **Project Settings (gear icon) > Service Accounts**.
2. Click **Generate new private key**.
3. Download the `.json` file (e.g., `serviceAccountKey.json`). **Keep it secret, keep it safe!**

## Step 4: Add Config Files to Project Root

Place these files at your project root:

- `serviceAccountKey.json` (your downloaded Firebase admin key)

Populate the index.html with your firebase config

```json
{
  "apiKey": "YOUR_API_KEY",
  "authDomain": "your-project.firebaseapp.com",
  "databaseURL": "https://your-project.firebaseio.com",
  "projectId": "your-project",
  "storageBucket": "your-project.appspot.com",
  "messagingSenderId": "YOUR_SENDER_ID",
  "appId": "YOUR_APP_ID",
  "measurementId": "YOUR_MEASUREMENT_ID"
}
```

---

## Step 5: Install Python Dependencies

Make sure you have Python installed (3.7+ recommended).

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Step 6: Run the Clipboard Listener

This Python script listens to your clipboard and sends updates to Firebase in real-time.

Run it with:

```bash
py cheatboard.py
```

You’ll see:

```
🚀 Clipboard listener started. Ready to transmit...
📋 Copied: [your clipboard content]
```

---

## Step 7: Open the Web Client

Open `index.html` in your browser (ideally on HTTPS)

It will display the latest clipboard content live!

Click the **📋 Copy Text** button to copy the text from the web interface back to your clipboard (android/ios).

---
