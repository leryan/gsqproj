from lib.grammar_check import grammar_check

"""
text_check is string words that meets criteria
It will return True 
"""
def test_grammar_check_with_correct_criteria():
    result = grammar_check("Hello there!")
    assert result == True


"""
text_check is string words that meets crit of capital letter, but not punctuation crit
It will return "Check punctuation"
"""

def test_grammar_check_with_only_capital_letter_criteria():
    result = grammar_check("Hello there")
    assert result == "Check punctuation"


"""
text_check is string words that does not meet the crit of capital letter, but meets the punctuation crit
It will return "Check capital letter"
"""

def test_grammar_check_with_only_punctuation_criteria():
    result = grammar_check("hello there!")
    assert result == "Check capital letter"

"""
text_check is string words that does not meet any of the crit of capital letter + punctuation 
It will return "Check capital letter and punctuation"
"""

def test_grammar_check_with_no_valid_criteria():
    result = grammar_check("hello there")
    assert result == "Check capital letter and punctuation"