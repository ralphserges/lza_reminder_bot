import re
from bot_starter_pack import BotStarterPack, events
from exceptions import IncompleteNewReminderFieldsError, DateIsPastError, TimeForTodayIsPastError

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
        await event.respond(response_provider.access_denied_response())
    else:
        await event.respond(response_provider.welcome_response(username=sender_username),parse_mode='HTML')

@bot.on(events.NewMessage(pattern='/add'))
async def add_instruction(event):
    sender = await event.get_sender()
    sender_username = sender.username
    if not user_authorization_validator.is_user_authorized(username=sender_username):  
        await event.respond(response_provider.access_denied_response())
    else:
        await event.respond(response_provider.add_reminder_instruction())

@bot.on(events.NewMessage(pattern=re.compile(r'add_reminder', re.IGNORECASE)))
async def add_reminder(event):
    sender = await event.get_sender()
    sender_username = sender.username
    if not user_authorization_validator.is_user_authorized(username=sender_username):  
        await event.respond(response_provider.access_denied_response())
    else:
        user_input = event.message.message
        try:
            user_input_validator.validate_new_reminder_input(user_input)
        except IncompleteNewReminderFieldsError as incomplete_input_err:
            print(incomplete_input_err.err_msg)
        except ValueError as wrong_datetime_format_err:
            print('Date/Time format is wrong. Correct Date Format(YYYY-MM-DD). Correct Time Format(HHMM)')
        except DateIsPastError as date_is_past_err:
            print(date_is_past_err.err_msg)
        except TimeForTodayIsPastError as time_past_err:
            print(time_past_err.err_msg)
        
        

def start_bot():
    bot.run_until_disconnected()

if __name__ == '__main__':
    start_bot()