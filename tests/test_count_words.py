from lib.count_words import Count_words

"""
Empty string returns 0 words
"""

def test_count_words_of_empty_string():
    result = Count_words("")
    assert result == 0

"""
7 word string returns 7
"""
def test_seven_word_string_returns_seven():
    result = Count_words("one two three four five six seven")
    assert result == 7

"""
10 word string returns 10
"""
def test_seven_word_string_returns_seven():
    result = Count_words("one two three four five six seven eight nine ten")
    assert result == 10
