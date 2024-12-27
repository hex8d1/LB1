import asyncio
from telethon import TelegramClient

api_id = ...
api_hash = "..."
phone = "+380"

async def main():
    client = TelegramClient('my_session', api_id, api_hash)
    await client.start(phone=phone)
    participants = await client.get_participants('@...')
    for user in participants:
        print(user.id, user.username, user.first_name, user.last_name)
    await client.send_message('@some_contact', 'Привет!')
    await client.disconnect()

asyncio.run(main())



