import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Must have title and contents")
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return self.title + ": " + self.contents

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("You can not read any words - wpm is 0")
        words = (self.contents).split()
        return math.ceil(len(words) / wpm)

    def reading_chunk(self, wpm, minutes):
        words = self.contents.split()
        allowed_words = wpm * minutes
        if self.read_so_far >= len(words):
            self.read_so_far = 0
        start = self.read_so_far
        end = self.read_so_far + allowed_words
        chunk = words[start:end]
        self.read_so_far = end
        return " ".join(chunk)







        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.

        # iterate through words in entry based on the number of words they can read
        # number of words they can read = wpm * minutes
        # return entry[:8].remove()