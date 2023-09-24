import pytest
from lib.grammar_stats import GrammarStats

def test_true_exlamation_grammarStats():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Wicked!") == True

def test_false_no_punctuation_grammarStats():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Wicked") == False

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

def test_empty_grammarStats():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
    assert str(e.value) == "Must include text"

def test_percentage_bad():
    grammar_stats = GrammarStats()
    assert grammar_stats.percentage_good("Wicked") == 0

def test_percentage_good():
    grammar_stats = GrammarStats()
    assert grammar_stats.percentage_good("Wicked.") == 100

# def test_mix_percentage_good_and_bad():
#     grammar_stats = GrammarStats()
#     assert grammar_stats.percentage_good("Wicked.") == 100
#     assert grammar_stats.percentage_good("Wicked?") == 100
#     assert grammar_stats.percentage_good("Wicked!") == 100
#     assert grammar_stats.percentage_good("Wicked.") == 75
#     assert grammar_stats.percentage_good("Wicked?") == 60
#     assert grammar_stats.percentage_good("Wicked!") == 50

 # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        