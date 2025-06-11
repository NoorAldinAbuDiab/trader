import re
import asyncio
import logging
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

# تحميل المتغيرات من ملف .env
load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
SOURCE_CHANNEL = os.getenv('SOURCE_CHANNEL')
TRADE_BOT_USERNAME = os.getenv('TRADE_BOT_USERNAME')

# تعبير منتظم لاكتشاف عناوين العملات
TOKEN_PATTERN = re.compile(r'\b[a-zA-Z0-9]{30}pump\b', re.IGNORECASE)

# إعداد السجلات
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def main():
    client = TelegramClient('nour_trader', API_ID, API_HASH)
    await client.start(bot_token=BOT_TOKEN)  # <-- هنا التصحيح

    logger.info("Bot started successfully! Listening for messages...")
    print("Bot is running. Press Ctrl+C to stop.")

    @client.on(events.NewMessage(chats=SOURCE_CHANNEL))
    async def handle_new_message(event):
        try:
            # استخراج النص من الرسالة
            message_text = event.message.text or ""
            logger.info(f"Received message from source channel")

            # البحث عن عناوين العملات
            tokens = TOKEN_PATTERN.findall(message_text)

            if tokens:
                unique_tokens = set(tokens)  # إزالة التكرارات
                logger.info(f"Found {len(unique_tokens)} unique tokens")

                for token in unique_tokens:
                    # إرسال كل عنوان إلى بوت التداول
                    try:
                        await client.send_message(
                            entity=TRADE_BOT_USERNAME,
                            message=token
                        )
                        logger.info(f"Successfully sent token to trade bot: {token}")
                        await asyncio.sleep(2)  # تأخير 2 ثواني بين الرسائل
                    except Exception as send_error:
                        logger.error(f"Failed to send token {token}: {send_error}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")

    await client.run_until_disconnected()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped by user")
