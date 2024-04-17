#!/usr/bin/8python3
"""That export data in the JSON format"""

import requests
import json
import sys

def export_todo_data():
    """ Fetch and display TODO list progress for all employees """

    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    try:
        response_users = requests.get(users_url)
        response_todos = requests.get(todos_url)

        users = response_users.json()
        todos = response_todos.json()

        user_dict = {}

        for user in users:
            user_id = str(user.get("id"))
            username = user.get("username")
            tasks = []

            for todo in todos:
                if todo.get("userId") == user.get("id"):
                    task_data = {
                        "username": username,
                        "task": todo.get("title"),
                        "completed": todo.get("completed")
                    }
                    tasks.append(task_data)

            user_dict[user_id] = tasks

        json_file_name = "todo_all_employees.json"
        with open(json_file_name, "w") as json_file:
            json.dump(user_dict, json_file)


    except requests.exceptions.RequestException as e:
        print("Error fetching data: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    # Call the export_todo_data function
    export_todo_data()