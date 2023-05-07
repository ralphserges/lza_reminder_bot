from yaml.loader import SafeLoader
from pathlib import Path
import yaml

class AppConfig:
    def __init__(self):
        self.config_filepath = Path('configuration/appconfig.yaml')

        all_configs = self.get_all_configs(self.config_filepath)
        self.bot_api_key = all_configs.get('telegram_api_bot_key')
        self.tele_api_id = all_configs.get('telegram_api_id')
        self.tele_api_hash = all_configs.get('telegram_api_hash')
    
    def get_all_configs(self, config_filepath): 
        with open(config_filepath) as config_file:
            all_configs = yaml.load(config_file, Loader=SafeLoader)
            return all_configs



