from lib.todo_list import TodoList
from lib.todo import Todo

def test_todo_list_empty():
    todo_list = TodoList()
    assert todo_list.list == []

def test_add_todo_to_list_and_share_incomplete_tasks():
    todo_list = TodoList()
    todo_1 = Todo("Clean room")
    todo_list.add(todo_1)
    assert todo_list.incomplete() == "Clean room"

def test_add_todo_to_list_and_share_completed_tasks():
    todo_list = TodoList()
    todo_2 = Todo("Gym")
    todo_3 = Todo("Meditate")
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    todo_2.mark_complete()
    todo_3.mark_complete()
    assert todo_list.complete() == "Gym, Meditate"

def test_marked_all_tests_as_complete():
    todo_list = TodoList()
    todo_1 = Todo("Clean room")
    todo_2 = Todo("Gym")
    todo_3 = Todo("Meditate")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    todo_1.mark_complete()
    todo_2.mark_complete()
    todo_3.mark_complete()
    assert todo_list.complete() == "Clean room, Gym, Meditate"

