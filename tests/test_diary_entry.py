import pytest
from lib.diary_entry import DiaryEntry

def test_format():
    diary_entry = DiaryEntry("Name", "Somunachima")
    assert diary_entry.format() == "Name: Somunachima"

def test_count_words():
    diary_entry = DiaryEntry("Name", "Somunachima is a software engineering apprentice")
    assert diary_entry.count_words() == 7

def test_empty_title_diary_entry():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "Somunachima")
    assert str(e.value) == "Must have title and contents"

def test_empty_content_diary_entry():
    with pytest.raises(Exception) as e:
        DiaryEntry("Name", "")
    assert str(e.value) == "Must have title and contents"

def test_odd_reading_time():
    diary_entry = DiaryEntry("Role", "Software Engineering Apprentice, Android Health, Data Infrastructure, Backend Engineering")
    # wpm = 2 words per minute
        # 8 words   4 minutes 
    assert diary_entry.reading_time(2) == 5

def test_even_reading_time():
    diary_entry = DiaryEntry("Role", "Software Engineering Apprentice")
    # wpm = 2 words per minute
        # 8 words   4 minutes 
    assert diary_entry.reading_time(2) == 2

def test_zero_reading_time():
    diary_entry = DiaryEntry("Role", "Software Engineering Apprentice")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "You can not read any words - wpm is 0"

def test_first_reading_chunk():
    diary_entry = DiaryEntry("Role", "Software Engineering Apprentice, Android Health, Data Infrastructure, Backend Engineering")
    assert diary_entry.reading_chunk(2, 4) == "Software Engineering Apprentice, Android Health, Data Infrastructure, Backend"

def test_second_reading_chunk():
    diary_entry = DiaryEntry("Role", "Software Engineering Apprentice, Android Health, Data Infrastructure, Backend Engineering")
    assert diary_entry.reading_chunk(2, 1) == "Software Engineering"
    assert diary_entry.reading_chunk(2, 1) == "Apprentice, Android"
    assert diary_entry.reading_chunk(2, 1) == "Health, Data"
    assert diary_entry.reading_chunk(2, 1) == "Infrastructure, Backend"
    assert diary_entry.reading_chunk(1, 1) == "Engineering"

def test_restart_reading_chunk():
    diary_entry = DiaryEntry("Role", "Software Engineering Apprentice, Android Health, Data Infrastructure, Backend Engineering")
    assert diary_entry.reading_chunk(2, 2) == "Software Engineering Apprentice, Android"
    assert diary_entry.reading_chunk(2, 1) == "Health, Data"
    assert diary_entry.reading_chunk(1, 1) == "Infrastructure,"
    assert diary_entry.reading_chunk(2, 1) == "Backend Engineering"
    assert diary_entry.reading_chunk(2, 2) == "Software Engineering Apprentice, Android"

