#A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.
from lib.make_snippet import Make_snippet

def test_make_snippet_empty_string():
    result = Make_snippet("")
    assert result == ""

"""
String returns exactly five words
"""

def test_make_snippet_return_five_word_string():
    result = Make_snippet("Hey there, how are you?")
    assert result == "Hey there, how are you?"

"""
String with more than 5 words, returns five words + ...
"""

def test_make_snippet_return_five_word_and_ellipses():
    result = Make_snippet("Hey Sanam and Ryan, how are you?")
    assert result == "Hey Sanam and Ryan, how..."


"""
String with 12 words, returns five words + ...
"""

def test_make_snippet_return_five_word_and_ellipses():
    result = Make_snippet("Hey Joao and Sanam, how are you and how was your weekend?")
    assert result == "Hey Joao and Sanam, how..."