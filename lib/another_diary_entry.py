import math

class AnotherDiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents

    def count_words(self):
        words = self.contents.split()
        return len(words)

    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        words = self.contents.split()
        allowed_words = wpm * minutes
        if self.read_so_far >= len(words):
            self.read_so_far = 0
            
        start = self.read_so_far
        end = self.read_so_far + allowed_words
        chunk = words[start:end]
        self.read_so_far = end
        return " ".join(chunk)