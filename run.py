import asyncio
import random
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest

# Your credentials for connecting to Telegram API
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'

# Source channel link (from where messages will be forwarded)
source_channel_link = 'https://t.me/your_source_channel'
# Target chat links (where messages will be forwarded)
target_chat_links = [
    'https://t.me/your_target_chat_1',
    'https://t.me/your_target_chat_2',
    # Add other chat links here
]
# Interval in seconds
interval = 1800

async def get_channel_id(client, link):
    username = link.split('/')[-1]
    try:
        result = await client(ResolveUsernameRequest(username))
        return result.peer.channel_id
    except Exception as e:
        print(f"Error getting ID for {link}: {e}")
        return None

async def main():
    client = TelegramClient('anon', api_id, api_hash)
    await client.start(phone=phone_number)
    print("Client Created")

    # Get the ID of the source channel
    source_channel_id = await get_channel_id(client, source_channel_link)
    if not source_channel_id:
        print(f"Failed to get source channel ID for {source_channel_link}")
        return

    # Get IDs of target chats
    target_chat_ids = []
    for link in target_chat_links:
        chat_id = await get_channel_id(client, link)
        if chat_id:
            target_chat_ids.append(chat_id)
        else:
            print(f"Failed to get chat ID for {link}")

    if not target_chat_ids:
        print("No valid target chat IDs found.")
        return

    while True:
        try:
            # Get the latest message from the source channel
            result = await client(GetHistoryRequest(
                peer=PeerChannel(int(source_channel_id)),
                limit=1,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))

            if result.messages:
                message = result.messages[0]
                print(f"Forwarding message with ID {message.id}")

                success_count = 0
                skip_count = 0

                for chat_id in target_chat_ids:
                    try:
                        await client.forward_messages(int(chat_id), message)
                        success_count += 1
                        print(f"Message forwarded to chat ID {chat_id}")
                    except Exception as e:
                        print(f"Error forwarding message to chat ID {chat_id}: {e}")
                        skip_count += 1
                        continue  # Proceed to the next chat in case of an error

                    # Random delay between sending messages to different chats
                    delay = random.randint(2, 10)
                    print(f"Waiting for {delay} seconds before sending to the next chat...")
                    await asyncio.sleep(delay)

                print(f"Messages successfully sent to {success_count} chats.")
                print(f"Skipped {skip_count} chats.")

            await asyncio.sleep(interval)
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())
