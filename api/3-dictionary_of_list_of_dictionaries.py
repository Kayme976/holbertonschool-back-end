#!/usr/bin/8python3
"""That export data in the JSON format"""

import requests
import json
import sys

def fetch_all_employees_data():
    users_data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos_data = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    all_employee_data = {}

    for user in users_data:
        user_id = user['id']
        user_name = user['name']
        user_tasks = []

        for task in todos_data:
            if task['userId'] == user_id:
                user_tasks.append({
                    "username": user_name,
                    "task": task["title"],
                    "completed": task["completed"]
                })

        all_employee_data[user_id] = user_tasks

    return all_employee_data

def export_to_json(data):
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)

    print("Data exported to todo_all_employees.json")

if __name__ == "__main__":
    all_employee_data = fetch_all_employees_data()
    export_to_json(all_employee_data)