class TimeForTodayIsPastError(Exception):

    def __init__(self):
        self.err_msg = r"Time is already past to set for today's reminder."
        super().__init__(self.err_msg)