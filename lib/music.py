class Music:
    def __init__(self):
        self.tracks = []

    def list(self):
        return ", ".join(self.tracks)
    
    def add(self, track):
        self.tracks.append(track)
        return self.list()

# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.