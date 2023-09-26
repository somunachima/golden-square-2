from lib.vowel_remover import *

def test_simple_ab_vowel_remover():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_simple_a_vowel_remover():
    remover = VowelRemover("a")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""

def test_simple_e_vowel_remover():
    remover = VowelRemover("e")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""

def test_simple_i_vowel_remover():
    remover = VowelRemover("i")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""

def test_simple_o_vowel_remover():
    remover = VowelRemover("o")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""

def test_simple_u_vowel_remover():
    remover = VowelRemover("u")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""

def test_simple_aeiou_vowel_remover():
    remover = VowelRemover("aeiou")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."