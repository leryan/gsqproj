## Challenge

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def task_tracker(task):

Parameter:
    task: text in a form of a string

Returns:
    Return = existing list with any new tasks added, which includes 'TODO' in the string.
    Otherwise it will return a msg that it is 'not a TODO item' alongside the existing list.

Side Effects:
    None

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
TODO task for the user, it will add the TODO task to the task list

Example input:
    #TODO laundry

Example output:
    ['existing items..', 'laundry']
"""

task_tracker('#TODO laundry') => ['existing items..', 'laundry']

"""
Task does not include '#TODO' string, which will result in the task not being added to the task list

Example input:
    groceries

Example output:
    ['existing items..'] 'groceries not a TODO item'
"""

task_tracker('laundry') => ['existing items..'] 'laundry not a TODO item'

"""
String is empty, which will return a message 'No task specified'

Example input:
    ''

Example output:
    'No task specified'

"""

task_tracker('') => 'No task specified'

## 4. Implement the Behaviour

from lib.task_tracker import task_tracker

