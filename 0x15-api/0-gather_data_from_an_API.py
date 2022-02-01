#!/usr/bin/python3
"""Write a Python script that, using this REST API,
    for a given employee ID, returns information about
    his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":

    todo_s = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    user_n = user.get('name')
    user_id = user.get('id')
    tasks = []
    d_tasks = 0
    t_tasks = 0

    for stat in todo_s:
        if user_id == stat.get('userId'):
            if stat.get('completed') is True:
                d_tasks = d_tasks + 1
                tasks.append(stat.get('title'))
            t_tasks = t_tasks + 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user_n, d_tasks, t_tasks))

    for data in tasks:
        print('\t', data)