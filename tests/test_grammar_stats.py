import pytest
from lib.grammar_stats import GrammarStats

def test_for_zero_good_stats():
    grammer_stats = GrammarStats()
    assert grammer_stats.good == 0

def test_for_zero_bad_stats():
    grammer_stats = GrammarStats()
    assert grammer_stats.good == 0

def test_empty_grammarStats():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
    assert str(e.value) == "Must include text"

def test_true_exlamation_grammarStats():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked!") == True

def test_true_exlamation_and_count_for_good_grammarStats():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked!") == True
    assert grammar_stats.good == 1

def test_true_exlamation_two_grammarStats():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked!") == True
    grammar_stats.check("Wicked?") == True
    assert grammar_stats.good == 2

def test_false_no_punctuation_grammarStats():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked") == False

def test_false_no_punctuation_and_count_one_bad_grammarStats():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked") == False
    assert grammar_stats.bad == 1

def test_false_no_punctuation_and_count_two_bad_grammarStats():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked") == False
    grammar_stats.check("wicked") == False
    assert grammar_stats.bad == 2

def test_false_exclamation_grammarStats():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("wicked!") == False

def test_true_question_grammarStats():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Wicked?") == True

def test_false_question_grammarStats():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("wicked?") == False

def test_true_dot_grammarStats():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Wicked.") == True

def test_false_dot_grammarStats():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("wicked.") == False

def test_two_bad_and_one_good_grammarStats():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked!") == True
    grammar_stats.check("Wicked") == False
    grammar_stats.check("wicked") == False
    assert grammar_stats.bad == 2
    assert grammar_stats.good == 1

def test_percent_good_when_two_bad_and_one_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked!") == True
    grammar_stats.check("Wicked") == False
    grammar_stats.check("wicked") == False
    grammar_stats.bad == 2
    grammar_stats.good == 1
    assert grammar_stats.percentage_good() == 34

def test_percent_good_when_two_bad_and_two_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked!") == True
    grammar_stats.check("Wicked?") == True
    grammar_stats.check("Wicked") == False
    grammar_stats.check("wicked") == False
    grammar_stats.bad == 2
    grammar_stats.good == 2
    assert grammar_stats.percentage_good() == 50

def test_percent_good_when_three_bad_and_two_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked!") == True
    grammar_stats.check("Wicked?") == True
    grammar_stats.check("Wicked") == False
    grammar_stats.check("wicked") == False
    grammar_stats.check("wicked.") == False
    grammar_stats.bad == 3
    grammar_stats.good == 2
    assert grammar_stats.percentage_good() == 40

def test_percent_good_when_two_bad_and_three_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("Wicked!") == True
    grammar_stats.check("Wicked?") == True
    grammar_stats.check("Wicked.") == True
    grammar_stats.check("wicked") == False
    grammar_stats.check("wicked.") == False
    grammar_stats.bad == 2
    grammar_stats.good == 3
    assert grammar_stats.percentage_good() == 60


 # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        