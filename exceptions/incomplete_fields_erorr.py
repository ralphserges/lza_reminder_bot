class IncompleteNewReminderFieldsError(Exception):

    def __init__(self):
        self.err_msg = r'There are missing fields. Please enter /add to see required fields.'
        super().__init__(self.err_msg)