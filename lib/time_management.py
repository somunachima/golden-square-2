class TimeManagement():
    def __init__(self):
        self.time_management = "time_management"

    def estimate(self, words):
        minutes = round(words / 200)
        return f"{minutes} minutes"


# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute