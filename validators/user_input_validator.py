from enum import IntEnum
from exceptions import IncompleteNewReminderFieldsError,DateIsPastError, TimeForTodayIsPastError
from datetime import datetime


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
    
    def validate_new_reminder_input(self, message:str):
        new_reminder_fields = message.splitlines()
        self.__check_new_reminder_field_complete(new_reminder_fields)
        self.__check_datetime_format_correct(
            new_reminder_fields[int(NewReminderFields.date_idx)],
            new_reminder_fields[int(NewReminderFields.time_idx)], 
            new_reminder_fields[NewReminderFields.is_recurring_idx])
    
    def __check_new_reminder_field_complete(self, new_reminder_fields:list):
        if not (len(new_reminder_fields) == self.new_reminder_field_correct_size):
            raise IncompleteNewReminderFieldsError

    def __check_datetime_format_correct(self, date:str, time:str, is_recurring:str):
        date_correct_format = r'%Y-%m-%d'
        date_input = datetime.strptime(date,date_correct_format).date()
        print(date_input)

        time_correct_format = r'%H%M'
        time_input = datetime.strptime(time,time_correct_format).time()
        print(time_input)
        #will throw ValueError if date/time input format not right

        self.__check_datetime_is_past(time_input,date_input,is_recurring)
        
    def __check_datetime_is_past(self, time_input:datetime.time, date_input:datetime.date, is_recurring:str):
        if(date_input < datetime.now().date()):
            raise DateIsPastError
        
        if(date_input == datetime.now().date()):
            if(time_input < datetime.now().time() and is_recurring.lower() == 'false'):
                raise TimeForTodayIsPastError        


