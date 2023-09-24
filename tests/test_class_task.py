import pytest
from lib.class_task import ClassTask

def test_no_tasks():
    class_task = ClassTask()
    assert class_task.list() == ""

def test_track_task():
    class_task = ClassTask()
    assert class_task.add("Clean bedroom") == "Clean bedroom"

def test_track_multiple_tasks():
    class_task = ClassTask()
    assert class_task.add("Clean bedroom") == "Clean bedroom"
    assert class_task.add("Cook lunch") == "Clean bedroom, Cook lunch"
    assert class_task.add("Fry plantain") == "Clean bedroom, Cook lunch, Fry plantain"
    assert class_task.list() == "Clean bedroom, Cook lunch, Fry plantain"

def test_mark_completed():
    class_task = ClassTask()
    assert class_task.add("Clean bedroom") == "Clean bedroom"
    assert class_task.add("Cook lunch") == "Clean bedroom, Cook lunch"
    assert class_task.add("Fry plantain") == "Clean bedroom, Cook lunch, Fry plantain"
    assert class_task.mark_completed("Clean bedroom") == "Cook lunch, Fry plantain"
    assert class_task.mark_completed("Fry plantain") == "Cook lunch"

def test_mark_completed_task_does_not_exist():
    class_task = ClassTask()
    assert class_task.add("Cook lunch") == "Cook lunch"
    with pytest.raises(Exception) as e:
        class_task.mark_completed("Wash Hair")
    assert str(e.value) == "No such task exists"

def test_list_incomplete_task():
    class_task = ClassTask()
    assert class_task.add("Clean bedroom") == "Clean bedroom"
    assert class_task.add("Cook lunch") == "Clean bedroom, Cook lunch"
    assert class_task.add("Fry plantain") == "Clean bedroom, Cook lunch, Fry plantain"