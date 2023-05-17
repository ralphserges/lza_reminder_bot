from telethon import TelegramClient, events
from configuration.appconfig import AppConfig
from validators import UserAuthorizationValidator,UserInputValidator
from response_provider import ResponseProvider

class BotStarterPack:
    def __init__(self):
        appconfig = AppConfig()
        self.telegram_bot = TelegramClient(session='sessions/',api_id=appconfig.tele_api_id,api_hash=appconfig.tele_api_hash).start(bot_token=appconfig.bot_api_key)
        self.response_provider = ResponseProvider()
        self.user_validator = UserAuthorizationValidator(authorized_users_list=appconfig.authorized_users)
        self.user_input_validator = UserInputValidator()
