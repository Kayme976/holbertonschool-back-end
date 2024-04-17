#!/usr/bin/python
"""That utilizes a REST API to retrieve information about
the progress of the TODO list for a specified employee ID."""

import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]

    infos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user = infos.json()
    employee = user.get("name")

    infos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userID={}'.format(user_id))
    todos = infos.json()
    total_tasks = len(todos)

    tasks_done = [task for task
                            in todos if task.get("completed") is True]

    print("Employee {} is done with task({}/{}):".format
          (employee, len(tasks_done), total_tasks))

    for task in tasks_done:
        print("\t {}".format(task.get("title")))