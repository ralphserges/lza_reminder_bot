from telethon import TelegramClient, events
from pathlib import Path
from configuration.appconfig import AppConfig

appconfig = AppConfig()
BOT_TOKEN = appconfig.bot_api_key
TELE_API_ID = appconfig.tele_api_id
TELE_API_HASH = appconfig.tele_api_hash

bot = TelegramClient(session='sessions/', api_id=TELE_API_ID, api_hash=TELE_API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hi.')
    raise events.StopPropagation

def start_bot():
    bot.run_until_disconnected()

if __name__ == '__main__':
    start_bot()