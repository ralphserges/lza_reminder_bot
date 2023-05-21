import re
from bot_starter_pack import BotStarterPack, events
from exceptions import IncompleteNewReminderFieldsError, DateIsPastError, TimeForTodayIsPastError,InvalidBooleanUserInput
import logging
import my_logs

logger = logging.getLogger(__name__)
bot_starter_pack = BotStarterPack()
response_provider = bot_starter_pack.response_provider
user_authorization_validator = bot_starter_pack.user_validator
user_input_validator = bot_starter_pack.user_input_validator
bot = bot_starter_pack.telegram_bot

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    sender_username = sender.username
    if not user_authorization_validator.is_user_authorized(username=sender_username):  
        logger.warn('Unauthorized user,{sender_username}, tried to use the bot.')
        await event.respond(response_provider.access_denied_response())
    else:
        logger.info('{sender_username} sent /start request')
        await event.respond(response_provider.welcome_response(username=sender_username),parse_mode='HTML')

@bot.on(events.NewMessage(pattern='/add'))
async def add_instruction(event):
    sender = await event.get_sender()
    sender_username = sender.username
    if not user_authorization_validator.is_user_authorized(username=sender_username): 
        logger.warn('Unauthorized user,{sender_username}, tried to use the bot.')
        await event.respond(response_provider.access_denied_response())
    else:
        logger.info('{sender_username} sent /add request')
        await event.respond(response_provider.add_reminder_instruction())

@bot.on(events.NewMessage(pattern=re.compile(r'add_reminder', re.IGNORECASE)))
async def add_reminder(event):
    sender = await event.get_sender()
    sender_username = sender.username
    if not user_authorization_validator.is_user_authorized(username=sender_username): 
        logger.warn('Unauthorized user,{sender_username}, tried to use the bot.')
        await event.respond(response_provider.access_denied_response())
    else:
        try:
            logger.info('{sender_username} send request to add new reminder')
            user_input = event.message.message
            valid_new_reminder = user_input_validator.validate_new_reminder_input(user_input,sender_username)
        
        except Exception as error:
            logger.error(error.err_msg)
        except ValueError as wrong_datetime_format_err:
            logger.error('Date/Time format is wrong. Correct Date Format(YYYY-MM-DD). Correct Time Format(HHMM)')


def start_bot():
    bot.run_until_disconnected()

if __name__ == '__main__':
    start_bot()