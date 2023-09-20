from lib.count_words import CountWords

def test_count_words():
    count_words = CountWords()
    assert count_words.count("darwin was a notable scientist") == 5

# takes a string as an argument and returns the number of words in that string.

