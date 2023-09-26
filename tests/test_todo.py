from lib.todo import Todo

def test_all_todo_are_initially_incomplete():
    todo_1 = Todo("Clean room")
    assert todo_1.completed == False

def test_all_todo_are_marked_as_complete():
    todo_2 = Todo("Gym")
    todo_3 = Todo("Meditate")
    todo_2.mark_complete()
    todo_3.mark_complete()
    assert todo_2.completed == True
    assert todo_3.completed == True