## Exercise One

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def read_time(text)

Parameter:
    text: text in the form of a string

Returns:
    return value = a string e.g. 'x seconds' / 'y minutes'

Side Effects:
    x seconds if x<60 else y minutes

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
text length is 200 words
It returns one minute expected read time
"""

read_time('text *200') => "1 mins"

"""
text length is 100 words
It returns one minute expected read time
"""

read_time(100) => "0.5 mins"

"""
text length is 1000 words
It returns five minute expected read time
"""

read_time(100) => "5 mins"

"""
text argument is an empty string returns zero mins reading time
"""

read_time(string) returns zero

## 4. Implement the Behaviour

from lib.read_time import 
def read_time(text)



