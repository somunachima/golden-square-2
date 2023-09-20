from lib.make_snippet import MakeSnippet

def test_over_five_make_snippet():
    make_snippet = MakeSnippet()
    assert make_snippet.cut("Somunachima") == "Somun..."

def test_exactly_five_snippet():
    make_snippet = MakeSnippet()
    assert make_snippet.cut("Apple") == "Apple"


#takes a string as an argument and returns the first five words and then a '...' if there are more than that