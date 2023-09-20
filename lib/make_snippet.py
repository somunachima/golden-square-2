class MakeSnippet:
    def __init__(self):
        self.make_snippet = "make snippet"

    def cut(self, text):
        if len(text) > 5:
            return text[0:5] + "..."
        else:
            return text