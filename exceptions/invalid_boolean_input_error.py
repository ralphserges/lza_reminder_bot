class InvalidBooleanUserInput(Exception):

    def __init__(self):
        self.err_msg = r"is_recurring contain invalied boolean value. Should either be 'true' or 'false'"
        super().__init__(self.err_msg)