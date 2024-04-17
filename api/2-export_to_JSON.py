#!/usr/bin/python3
"""That export data in the JSON format"""

import requests
import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
    todos_data = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}').json()

    if user_data is None or todos_data is None:
        sys.exit(1)

    employee_name = user_data.get('name')
    data = {"USER_ID": [{"task": task["title"], "completed": task["completed"], "username": employee_name} for task in todos_data]}

    file_name = f'{employee_id}.json'
    with open(file_name, mode='w') as file:
        json.dump(data, file)

    print(f"Data exported to {file_name}")

if __name__ == "__main__":
    main()