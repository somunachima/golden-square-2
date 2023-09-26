class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    # i = 0
    # self.text[:0] = ""
    # self.text[0+1:] = "eiou"
    # self.text = "" + "eiou"
    # self.text = "eiou"

    # self.text = "eiou"
    # i = 1
    # self.text[:1] = "e"
    # self.text[2:] = "ou"
    # self.text = "e" + "ou"
    # self.text = "eou"

    # i = 2
    # self.text = "eou"
    # self.text[:2] = "eo"
    # self.text[3:] = ""
    # self.text = ""

    # i = 3

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            i += 1
        return self.text
    
remover = VowelRemover("aeiou")
print(remover.remove_vowels())



# class VowelRemover:
#     def __init__(self, text):
#         self.text = text
#         self.vowels = ["a", "e", "i", "o", "u"]

#     def remove_vowels(self):
#         i = 0
#         self.text = list(self.text)
#         while i < len(self.text):
#             if self.text[i].lower() in self.vowels:
#                 self.text[i] = ""
#             i += 1
#         return "".join(self.text)
    
# remover = VowelRemover("aeiou")
# print(remover.remove_vowels())


