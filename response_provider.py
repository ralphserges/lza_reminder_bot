class ResponseProvider:
    def __init__(self):
        pass

    def welcome_response(self, username:str): 
        return f'Hi <i>{username}</i>, welcome back.\n\n'\
        'type /view to view specific reminder\n'\
        'type /add to add reminder\n'\
        'type /remove to remove reminder'
    
    def access_denied_response(self):
        return 'Sorry, you are not authorized to use this bot.'
    
    def add_reminder_instruction(self):
        return f'Please send new reminder in the following format. \n\n'\
        '<strong><u>Format</u></strong>\n'\
        'add_reminder\n'\
        'reminder_name\n'\
        'date_trigger(yyyy-mm-dd)\n'\
        'time_trigger(military time)\n'\
        'to_recur(true/false)\n'\
        'description\n\n'\
        '<strong><u>Example</u></strong>\n'\
        'add_reminder\n'\
        'my mother birthday\n'\
        '2023-05-15\n'\
        '1500\n'\
        'true\n'\
        'rmb to buy bird nest for her'
        



