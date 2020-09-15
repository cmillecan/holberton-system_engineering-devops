#!/usr/bin/python3
"""Export data in the CSV format"""
import requests
import sys
import csv

if __name__ == '__main__':
    user_id = sys.arg[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id))

    username = user.json()[0].get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': user_id})
    todos = todos.json()

    with open('{}.csv'.format(user_id), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

        for task in todos:
            writer.writerow([user_id, username, str(task.get('completed')),
                            task.get('title')])
