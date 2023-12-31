from lib.time_management import TimeManagement

def test_time_management():
    time_management = TimeManagement()
    assert time_management.estimate(600) == "3 minutes"

def test_no_words_time_management():
    time_management = TimeManagement()
    assert time_management.estimate(0) == "0 minutes"