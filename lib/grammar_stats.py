import math

class GrammarStats:
    def __init__(self):
        pass
  
    def check(self, text):
        if text == "":
            raise Exception("Must include text")
        elif (text[0] == text[0].upper()) and (text[-1] in "?!."):
            return True
        else:
            return False
  
    def percentage_good(self, text):
        good = 0
        bad = 0
        if self.check(text) == True:
            good += 1
        else:
            bad += 1
        return math.ceil((good / (bad + good)) * 100)