import subprocess
import time
import logging
from aiogram import Bot
import asyncio

API_TOKEN = '7360021855:AAHed9aMVMRD6YcGUQ4TqkhIgOI770XK05I'
ADMIN_ID = '6304585161'
MAX_RESTARTS = 5
RESTART_PERIOD = 60  # Seconds

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
bot = Bot(API_TOKEN)

def start_bot():
    """Start the bot script as a subprocess."""
    return subprocess.Popen(['python', '3.py'])

async def notify_admin(message):
    """Send a notification message to the admin via Telegram."""
    try:
        await bot.send_message(ADMIN_ID, message)
        logging.info("Admin notified: %s", message)
    except Exception as e:
        logging.error("Failed to send message to admin: %s", e)

async def main():
    """Main function to manage bot process lifecycle."""
    restart_count = 0
    last_restart_time = time.time()
    
    while True:
        if restart_count >= MAX_RESTARTS:
            current_time = time.time()
            if current_time - last_restart_time < RESTART_PERIOD:
                wait_time = RESTART_PERIOD - (current_time - last_restart_time)
                logging.warning("Maximum restart limit reached. Waiting for %.2f seconds...", wait_time)
                await notify_admin(f"⚠️ Maximum restart limit reached. Waiting for {int(wait_time)} seconds before retrying.")
                await asyncio.sleep(wait_time)
            restart_count = 0
            last_restart_time = time.time()

        logging.info("Starting the bot...")
        process = start_bot()
        await notify_admin("🚀 Your Codes Was Successful By @SASUKEPIRO Bot is starting...")

        while process.poll() is None:
            await asyncio.sleep(5)
        
        logging.warning("Bot process terminated. Restarting in 10 seconds...")
        await notify_admin("⚠️ The bot has crashed Because Of Error Please Check In Your Codespace Terminal If It Is A Syntax Problem Contact Me :- @SASUKEPIRO If It Is Not 🚫 Dont DM Just Chill.")
        restart_count += 1
        await asyncio.sleep(10)
        

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Watcher script terminated by user.")
