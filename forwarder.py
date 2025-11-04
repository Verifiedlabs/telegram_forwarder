import asyncio
import os
from telethon import TelegramClient, events

# API Telegram
api_id = '22741270'
api_hash = '43c0fd23c22c8ba19b34cb0caec30260'
session_name = 'cupang'

# ID Grup Sumber
source_group = 2294721332  # ID grup sumber

# Username Grup Tujuan (tanpa @)
destination_group_username = "degendek"

# Direktori penyimpanan media sementara
download_path = "downloads/"
os.makedirs(download_path, exist_ok=True)

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def forward_message(event):
    try:
        message_text = event.message.message or ""

        if event.message.media:
            file_path = await client.download_media(event.message.media, file=download_path)
            if file_path:
                await client.send_file(destination_group_username, file_path, caption=message_text)
                print(f"✅ Media + teks dikirim ke @{destination_group_username}")
                os.remove(file_path)
        else:
            await client.send_message(destination_group_username, message_text)
            print(f"✅ Teks dikirim ke @{destination_group_username}: {message_text}")

    except Exception as e:
        print(f"❌ Error: {e}")

async def main():
    await client.start()
    print("🚀 Bot sedang berjalan...")
    await client.run_until_disconnected()

asyncio.run(main())
