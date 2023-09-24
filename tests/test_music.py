from lib.music import Music

def test_no_tracks():
    music = Music()
    assert music.list() == ""

def test_add_track():
    music = Music()
    assert music.add("Sunshine") == "Sunshine"
    assert music.add("Wicked") == "Sunshine, Wicked"
    assert music.add("Christmas") == "Sunshine, Wicked, Christmas"


# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.