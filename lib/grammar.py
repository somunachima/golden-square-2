class Grammar:
    def __init__(self):
        grammar = "grammar"

    def verify(self, text):
        if text == "":
            return False
        elif (text[0] == text[0].upper()) and (text[-1] in "?!."):
            return True
        else:
            return False