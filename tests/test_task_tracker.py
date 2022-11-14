from lib.task_tracker import task_tracker

"""
TODO task for the user, it will add the TODO task to the task list
"""

def test_task_tracker_with_valid_todo_item_returns_updated_task_list():
    result = task_tracker('#TODO laundry')
    assert result == ['existing items...', 'laundry']

"""
Task does not include '#TODO' string, which will result in the task not being added to the task list
"""

def test_task_tracker_with_invalid_todo_item_returns_existing_task_list():
    result = task_tracker('groceries')
    assert result == str(['existing items...']) + ' groceries not a TODO item'

"""
String is empty, which will return a message 'No task specified'

"""

def test_task_tracker_with_empty_todo_item_returns_message_of_no_task_specified():
    result = task_tracker('')
    assert result == 'No task specified'