#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Correct Employee name: {}".format(user.get("name")))  
    print("Correct number of tasks: {}".format(len(todos)))  
    print("All tasks in output:")  
    [print("\t{}".format(c)) for c in todos]
