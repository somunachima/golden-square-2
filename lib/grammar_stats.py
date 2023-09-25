import math

class GrammarStats:
    def __init__(self):
        self.good = 0
        self.bad = 0
  
    def check(self, text):
        if text == "":
            raise Exception("Must include text")
        elif (text[0] == text[0].upper()) and (text[-1] in "?!."):
            self.good += 1
            return True
        else:
            self.bad += 1
            return False
  
    def percentage_good(self):
        # calculating percentage and using math.ceil to round the float
        percent = math.ceil((self.good / (self.bad + self.good)) * 100)
        return percent