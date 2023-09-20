from lib.tasks import Tasks

def test_action_tasks():
    tasks = Tasks()
    assert tasks.action("You need #TODO some Leetcode asap") == True

def test_no_action_tasks():
    tasks = Tasks()
    assert tasks.action("Holiday in barbados! Relax!") == False

def test_empty_tasks():
    tasks = Tasks()
    assert tasks.action("") == False


# I want to check if a text includes the string "#TODO".