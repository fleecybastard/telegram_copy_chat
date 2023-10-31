import asyncio

from pyrogram import Client
from pyrogram.enums import ChatType

API_ID = 1  # ENTER YOUR API ID
API_HASH = ''  # ENTER YOUR API HASH

TO_CHAT_ID = 1  # ENTER YOUR CHAT ID

app = Client('my_account', api_id=API_ID, api_hash=API_HASH)


async def get_all_channels() -> list[list[str, int]]:
    channels = []
    async for dialog in app.get_dialogs():
        if dialog.chat.type == ChatType.CHANNEL:
            channels.append([dialog.chat.title, dialog.chat.id])
    return channels


async def pick_channel() -> int:
    channels = await get_all_channels()
    print(f'PICK CHANNEL:')
    for i, channel in enumerate(channels):
        print(f'{i} - {channel[0]}')
    while True:
        channel_number = input('ENTER CHANNEL NUMBER: ')
        try:
            return channels[int(channel_number)][-1]
        except:
            print('WRONG NUMBER, TRY AGAIN')


async def resend_chat_history(chat_id: int, receiver_id: int) -> None:
    counter = 0
    async for message in app.get_chat_history(chat_id=chat_id):
        counter += 1
        try:
            if message.video is not None:
                await app.send_video(chat_id=receiver_id, video=message.video.file_id, caption=message.caption)
            elif message.photo is not None:
                await app.send_photo(chat_id=receiver_id, photo=message.photo.file_id, caption=message.caption)
            elif message.voice is not None:
                await app.send_voice(chat_id=receiver_id, voice=message.voice.file_id)
            elif message.video_note is not None:
                await app.send_video_note(chat_id=receiver_id, video_note=message.video_note.file_id)
            elif message.document is not None:
                await app.send_document(chat_id=receiver_id, document=message.document.file_id, caption=message.caption)
            elif message.audio is not None:
                await app.send_audio(chat_id=receiver_id, audio=message.audio.file_id, caption=message.caption)
            elif message.text is not None:
                await app.send_message(chat_id=receiver_id, text=message.text)
        except:
            pass
        if counter % 5 == 0:
            await asyncio.sleep(5)


async def main():
    async with app:
        channel_id = await pick_channel()
        await resend_chat_history(chat_id=channel_id, receiver_id=TO_CHAT_ID)


app.run(main())
