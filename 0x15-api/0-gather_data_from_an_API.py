#!/usr/bin/python3
"""return TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/" +
                         sys.argv[1])
    user = users.json().get("name")
    all_tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1])
    all_tasks_list = all_tasks.json()
    total_tasks = len(all_tasks_list)
    done_tasks = 0
    done_task_titles = []
    for task in all_tasks_list:
        if task.get("completed") is True:
            done_tasks += 1
            done_task_titles.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(user, done_tasks,
                                                          total_tasks))
    for title in done_task_titles:
        print(" \t{}".format(title))
