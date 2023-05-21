from datetime import datetime
class Reminder:
    def __init__(self, reminder_name:str, creator_name:str, date:datetime.date, time:datetime.time, is_recurring:bool, reminder_description:str):
        self.reminder_name = reminder_name
        self.creator_name = creator_name
        self.date = date
        self.time = time
        self.is_recurring = is_recurring
        self.reminder_description = reminder_description
        
