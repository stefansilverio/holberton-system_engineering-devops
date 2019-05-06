#!/usr/bin/python3
"""export to json format"""
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/" + sys.argv[1])
    user = users.json().get("username")
    all_tasks = requests.get("https://jsonplaceholder.typicode.com/todos?userId=" +
                             sys.argv[1])
    all_tasks_list_dicts = all_tasks.json()
    user_id = sys.argv[1]
    data = {}
    data[user_id] = []
    for task in all_tasks_list_dicts:
        data[user_id].append({
            'task': task.get("title"),
            'completed': task.get("completed"),
            'username': user
        })

    with open(user_id + ".json", "w") as out:
        json.dump(data, out)
