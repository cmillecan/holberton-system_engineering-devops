#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == '__main__':

    user_id = sys.argv[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': user_id})
    name = name.json()[0].get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': user_id})
    todos = todos.json()
    total_task = len(todos)
    todos_complete = [task for task in todos if task['completed']]
    completed_task = len(todos_complete)

    print("Employee {} is done with tasks({}/{}):".
          format(name, completed_task, total_task))
    for task in todos_complete:
        print("\t {}".format(task.get('title')))
