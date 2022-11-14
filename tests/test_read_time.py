from lib.read_time import read_time

"""
text length is 200 words
It returns one minute expected read time
"""
def test_200_length_text_returns_one_minute():
    result = read_time('text '*200)
    assert result == '1.0 mins'


"""
text length is 100 words
It returns one minute expected read time
"""
def test_100_length_text_returns_one_minute():
    result = read_time('text '*100)
    assert result == '0.5 mins'

"""
text length is 1000 words
It returns one minute expected read time
"""

def test_1000_length_text_returns_one_minute():
    result = read_time('text '*1000)
    assert result == '5.0 mins'

"""
text argument is an empty string returns zero seconds reading time
"""

def test_empty_string_text_returns_zero():
    result = read_time('')
    assert result == '0.0 mins'