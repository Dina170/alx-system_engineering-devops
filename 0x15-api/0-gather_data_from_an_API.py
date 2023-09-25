#!/usr/bin/python3
"""Get info about employees using api"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    ename = requests.get(url + "users/{}".format(argv[1])).json().get('name')
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    completed = []
    for todo in todos:
        if todo.get('completed'):
            completed.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        ename, len(completed), len(todos)))
    for todo in completed:
        print("\t {}".format(todo))
