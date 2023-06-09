from yaml.loader import SafeLoader
from pathlib import Path
import yaml

class AppConfig:
    def __init__(self):
        self.config_filepath = Path('configuration/appconfig.yaml')

        all_configs = self.__get_all_configs(self.config_filepath)
        self.bot_api_key = all_configs.get('telegram_api_bot_key')
        self.tele_api_id = all_configs.get('telegram_api_id')
        self.tele_api_hash = all_configs.get('telegram_api_hash')
        self.authorized_users = all_configs.get('authorized_users')
        self.list_of_prompts = all_configs.get('list_of_prompts')
    
    def __get_all_configs(self, config_filepath:str) : 
        with open(config_filepath) as config_file:
            all_configs = yaml.load(config_file, Loader=SafeLoader)
            return all_configs



