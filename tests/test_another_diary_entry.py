from lib.another_diary_entry import AnotherDiaryEntry

def test_count_words():
    another_diary_entry = AnotherDiaryEntry("Monday", "Hello Som")
    assert another_diary_entry.count_words() == 2

def test_reading_time_for_each_entry():
    another_diary_entry = AnotherDiaryEntry("Monday", "Hello Som, have fun")
    assert another_diary_entry.reading_time(2) == 2