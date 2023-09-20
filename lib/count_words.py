class CountWords:
    def __init__(self):
        self.count_words = "count words"

    def count(self, text):
        return len(text.split())