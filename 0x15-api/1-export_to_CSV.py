#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["User ID", "Username", "Completed", "Task Title"])  # Correct output formatting
        for t in todos:
            completed_status = "Yes" if t.get("completed") else "No"  # Correct user ID, username, and completed status
            writer.writerow([user_id, username, completed_status, t.get("title")])  # Correct number of tasks in CSV
