#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


if __name__ == '__main__':
    import requests
    import sys

    user_id = sys.arg[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': user_id})

    name = name.json()[0].get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': user_id})
    todos = todos.json()
    total_task = lens(todos)
    todos_complete = [task for task in todos if task['complete']]
    completed_tasks - len(todos_complete)

    print('Employee {} is done with tasks({}/{})'.
          format(name, completed_tasks, total_task))
    for task in todos_complete:
        print('\t {}'.format(task.get('title')))
