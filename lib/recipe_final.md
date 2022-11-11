## Exercise One

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def read_time(num_of_words)

Parameter:
    num_of_words: always an integer

Returns:
    return value = a string e.g. 'x seconds' / 'y minutes'

Side Effects:
    x seconds if x<60 else y minutes

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
Num_of_words is 200 words
It returns one minute expected read time
"""

read_time(200) => "1 mins"

"""
Num_of_words is 100 words
It returns one minute expected read time
"""

read_time(100) => "30 seconds"

"""
Num_of_words is 1000 words
It returns one minute expected read time
"""

read_time(100) => "5 mins"

"""
Num_of_words is a string and not a integer 
It returns error
"""

read_time(string) throws an error

## 4. Implement the Behaviour

    Writing tests etc.


## Exercise Two

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def grammar_check(text_check)

Parameter:
    text_check: always a string

Returns:
    return value = Boolean "True" if meets criteria of Capital letter + suitable sentence-ending punctuation mark
        Otherwise = Will return msg of "Check punctuation" if punctuation criteria isn't met 
            Will return "Check capital letter" if first word is not capitalised 
                Will return "Check capital letter and punctuation" if both criteria is missing

Side Effects:
    None (for now)

```python
# EXAMPLE

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
text_check is string words that meets criteria
It will return True 
"""

text_check("Hello there!") => True

"""
text_check is string words that meets crit of capital letter, but not punctuation crit
It will return "Check punctuation"
"""

text_check("Hello there") => "Check punctuation"

"""
text_check is string words that does not meet the crit of capital letter, but meets the punctuation crit
It will return "Check capital letter"
"""

text_check("hello there!") => "Check capital letter"

"""
text_check is string words that does not meet any of the crit of capital letter + punctuation 
It will return "Check capital letter and punctuation"
"""

text_check("hello there") => "Check capital letter and punctuation"