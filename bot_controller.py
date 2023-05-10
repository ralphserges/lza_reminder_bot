from telethon import TelegramClient, events
from pathlib import Path
from configuration.appconfig import AppConfig
from validation.user_authorization_validator import UserAuthorizationValidator
from formatter.response_provider import ResponseProvider

appconfig = AppConfig()
BOT_TOKEN = appconfig.bot_api_key
TELE_API_ID = appconfig.tele_api_id
TELE_API_HASH = appconfig.tele_api_hash

AUTHORIZED_USER = appconfig.authorized_users
user_authorization_validator = UserAuthorizationValidator(authorized_users_list=AUTHORIZED_USER)
response_provider = ResponseProvider()

bot = TelegramClient(session='sessions/', api_id=TELE_API_ID, api_hash=TELE_API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    sender_username = sender.username
    if not user_authorization_validator.is_user_authorized(username=sender_username):  
        await event.respond(response_provider.access_denied_response())
    else:
        await event.respond(response_provider.welcome_response(username=sender_username),parse_mode='HTML')

@bot.on(events.NewMessage(pattern='/add'))
async def start(event):
    sender = await event.get_sender()
    sender_username = sender.username
    if not user_authorization_validator.is_user_authorized(username=sender_username):  
        await event.respond(response_provider.access_denied_response())
    else:
        await event.respond(response_provider.add_reminder_template_response(),parse_mode='HTML')

@bot.on(events.NewMessage(pattern='[aA]dd_reminder*'))
async def add_reminder(event):
    sender = await event.get_sender()
    sender_username = sender.username
    if not user_authorization_validator.is_user_authorized(username=sender_username):  
        await event.respond(response_provider.access_denied_response())
    else:
        await event.respond(response_provider.add_reminder_template_response(),parse_mode='HTML')

def start_bot():
    bot.run_until_disconnected()

if __name__ == '__main__':
    start_bot()