class Tasks:
    def action(self, text):
        if "#TODO" in text:
            return True
        else:
            return False