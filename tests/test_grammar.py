from lib.grammar import Grammar

def test_true_exlamation_grammar():
    grammar = Grammar()
    assert grammar.verify("Wicked!") == True

def test_false_no_punctuation_grammar():
    grammar = Grammar()
    assert grammar.verify("Wicked") == False

def test_false_exclamation_grammar():
    grammar = Grammar()
    assert grammar.verify("wicked!") == False

def test_true_question_grammar():
    grammar = Grammar()
    assert grammar.verify("Wicked?") == True

def test_false_question_grammar():
    grammar = Grammar()
    assert grammar.verify("wicked?") == False

def test_true_dot_grammar():
    grammar = Grammar()
    assert grammar.verify("Wicked.") == True

def test_false_dot_grammar():
    grammar = Grammar()
    assert grammar.verify("wicked.") == False

def test_empty_grammar():
    grammar = Grammar()
    assert grammar.verify("") == False



# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark