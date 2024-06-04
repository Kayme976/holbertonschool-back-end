#!/usr/bin/python3
"""Script to export data in the JSON format"""

import json
import requests


def api():
    """
    dictionary
    """
    user_link = requests.get('https://jsonplaceholder.typicode.com/users')

    all_users_tasks = {}

    for user in user_link.json():
        user_id = user['id']
        user_name = user['username']

        todos_link = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

        tasks_list = []
        for todo in todos_link.json():
            task_dict = {"username": user_name,
                         "task": todo['title'],
                         "completed": todo['completed']}
            tasks_list.append(task_dict)

        all_users_tasks[user_id] = tasks_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_users_tasks, file)


if __name__ == "__main__":
    try:
        api()
    except Exception as e:
        pass
