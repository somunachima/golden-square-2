from lib.diary import Diary
from lib.another_diary_entry import AnotherDiaryEntry

def test_no_diary_entries_have_been_made():
    diary = Diary()
    assert diary.all() == []

def test_add_diary_entry_to_entries_list():
    diary = Diary()
    entry_1 = AnotherDiaryEntry("Monday", "Hello")
    entry_2 = AnotherDiaryEntry("Wednesday", "Goodbye")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

def test_count_number_of_words_in_entries():
    diary = Diary()
    entry_1 = AnotherDiaryEntry("Monday", "Hello")
    entry_2 = AnotherDiaryEntry("Wednesday", "Goodbye")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 2

def test_estimate_reading_time_in_minutes_one_entry():
    diary = Diary()
    entry_1 = AnotherDiaryEntry("Monday", "Hello Som")
    diary.add(entry_1)
    assert diary.reading_time(2) == 1

def test_estimate_reading_time_in_minutes_all_entries():
    diary = Diary()
    entry_1 = AnotherDiaryEntry("Monday", "Hello Som")
    entry_2 = AnotherDiaryEntry("Wednesday", "Goodbye")
    entry_3 = AnotherDiaryEntry("Friday", "Preekend")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.reading_time(2) == 2

def test_estimate_the_best_entry_for_reading_time():
    diary = Diary()
    entry_1 = AnotherDiaryEntry("Monday", "Hello Som how was")
    entry_2 = AnotherDiaryEntry("Wednesday", "Goodbye Som")
    entry_3 = AnotherDiaryEntry("Friday", "TGIF")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(1, 5) == entry_1
    