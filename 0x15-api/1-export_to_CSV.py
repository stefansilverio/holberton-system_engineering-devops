#!/usr/bin/python3
"""write to a CSV file"""
import csv
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/" + sys.argv[1])
    user = users.json().get("username")
    all_tasks = requests.get("https://jsonplaceholder.typicode.com/todos?userId=" +
                             sys.argv[1])
    all_tasks_list = all_tasks.json()
    user_id = sys.argv[1]
    with open(user_id + ".csv",'w') as task_record:
        for task in all_tasks_list:
            status = task.get("completed")
            title = task.get("title")
            task_format = csv.writer(task_record, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_ALL)
            task_format.writerow([str(user_id), str(user), str(status), str(title)])
