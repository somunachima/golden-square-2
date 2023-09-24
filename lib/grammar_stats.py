import math

class GrammarStats:
    def __init__(self):
        self.good = 0
        self.bad = 0
        self.calculate = 0
  
    def check(self, text):
        if text == "":
            raise Exception("Must include text")
        elif (text[0] == text[0].upper()) and (text[-1] in "?!."):
            return True
        else:
            return False
  
    def percentage_good(self, text):
        if self.check(text) == True:
            self.good += 1
        else:
            self.bad += 1
        self.calculate = (self.good / (self.bad + self.good)) * 100
        start_percent = math.ceil(self.calculate)
        return start_percent