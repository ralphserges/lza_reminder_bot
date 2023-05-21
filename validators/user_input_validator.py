from enum import IntEnum
from exceptions import IncompleteNewReminderFieldsError,DateIsPastError, TimeForTodayIsPastError,InvalidBooleanUserInput
from datetime import datetime
from dto import Reminder

import logging
import my_logs

logger = logging.getLogger(__name__)

class NewReminderFields(IntEnum):
    action_idx = 0
    reminder_name_idx = 1
    date_idx = 2
    time_idx = 3
    is_recurring_idx = 4
    description_idx = 5

class UserInputValidator:
    def __init__(self):
        self.new_reminder_field_correct_size = 6
    
    def validate_new_reminder_input(self, message:str, sender_username:str) -> Reminder :
        logger.info('validating new reminder user input')
        new_reminder_fields = message.splitlines()
        self.__check_new_reminder_field_complete(new_reminder_fields)
        
        valid_is_recurring_input = self.__check_is_recurring_value_valid(new_reminder_fields[NewReminderFields.is_recurring_idx])
        valid_date_input = self.__check_date_format_correct(new_reminder_fields[NewReminderFields.date_idx])
        valid_time_input = self.__check_time_format_correct(
            valid_date_input,
            new_reminder_fields[NewReminderFields.time_idx], 
            valid_is_recurring_input)
            
        logger.info('validation complete. user input OK')

        return Reminder(
            reminder_name=new_reminder_fields[NewReminderFields.reminder_name_idx], 
            creator_name=sender_username,
            date=valid_date_input,
            time=valid_time_input,
            is_recurring=valid_is_recurring_input, 
            reminder_description=new_reminder_fields[NewReminderFields.description_idx])

    def __check_new_reminder_field_complete(self, new_reminder_fields:list):
        if not (len(new_reminder_fields) == self.new_reminder_field_correct_size):
            raise IncompleteNewReminderFieldsError
        logger.debug('new add reminder fields are all present. valid.')

    def __check_is_recurring_value_valid(self, is_recurring:str) -> str:
        if not (is_recurring.lower() == 'true' or is_recurring.lower() == 'false'):
            raise InvalidBooleanUserInput
        logger.debug('is_recurring value is valid.')
        return is_recurring

    def __check_date_format_correct(self, date_input:str) -> datetime.date:
        date_correct_format = r'%Y-%m-%d'
        date_input = datetime.strptime(date_input,date_correct_format).date() #will throw ValueError if date input format not right
        logger.debug('date input format is valid.')
        return date_input

    def __check_time_format_correct(self, date_input:datetime.date, time:str, is_recurring:str) -> datetime.time:
        time_correct_format = r'%H%M'
        time_input = datetime.strptime(time,time_correct_format).time() #will throw ValueError if time input format not right
        self.__check_datetime_is_past(time_input,date_input,is_recurring)
        logger.debug('time input format is valid.')
        return time_input
        
    def __check_datetime_is_past(self, time_input:datetime.time, date_input:datetime.date, is_recurring:str):
        if(date_input < datetime.now().date()):
            raise DateIsPastError
        
        if(date_input == datetime.now().date()):
            if(time_input < datetime.now().time() and is_recurring.lower() == 'false'):
                raise TimeForTodayIsPastError        


