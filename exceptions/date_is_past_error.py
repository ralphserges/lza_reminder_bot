class DateIsPastError(Exception):

    def __init__(self):
        self.err_msg = r'Input date is in the past. Please input date as of today or later'
        super().__init__(self.err_msg)