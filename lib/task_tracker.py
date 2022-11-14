def task_tracker(task):
    list = ['existing items...']
    if task == '':
        return 'No task specified'
    elif '#TODO' in task:
        list.append(task.replace('#TODO ',''))
        return list
    else:
        return str(list) + ' ' + task + ' not a TODO item'