#!/usr/bin/python3
"""Export data in JSON format"""


if __name__ == '__main__':
    import requests
    import sys
    import csv

    user_id = sys.arg[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id))

    username = user.json()[0].get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/',
                         params={'userId': user_id})
    todos = todos.json()

    employee = {}
    employee[user_id] = []

    for tasks in todos:
        t = {}
        t['username'] = username
        t['task'] = tasks.get('title')
        t['completed'] = tasks.get('completed')
        employee[user_id].append(t)

    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(employee, f)
