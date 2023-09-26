import math

class Diary:
    def __init__(self):
        self.list = []

    def add(self, entry):
        self.list.append(entry)

    def all(self):
        return self.list

    def count_words(self):
        count = 0
        for entry in self.list:
            count += entry.count_words()
        return count

    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.

        reading_times = {}
        reading_time_allowed = wpm * minutes

        for entry in self.list:
        # calculate reading time for each entry
        # store reading times in dict (reading time, diary entry instance name) if less than reading time allowed (wpm * minutes)
            if entry.reading_time(wpm) <= reading_time_allowed:
                reading_times[entry] = entry.reading_time(wpm)
        # sort dict in order of reading times from lowest to highest
        best_entry = sorted(reading_times.items(), key=lambda item: item[1])[-1][0]
        # return the highest/last reading time in the dict
        return best_entry


