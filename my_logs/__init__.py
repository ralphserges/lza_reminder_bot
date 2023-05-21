from pathlib import Path
import yaml
import logging.config

logfilepath = Path('my_logs/log_configuration.yaml')
with open(logfilepath,'r') as log_configfile:
    config = yaml.safe_load(log_configfile.read())
    logging.config.dictConfig(config)


    