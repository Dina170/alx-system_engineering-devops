#!/usr/bin/python3
"""Get info about employees using api"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    ename = requests.get(url + "users/{}".format(argv[1]))
    username = ename.json().get('username')
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    with open('{}.json'.format(argv[1]), 'w') as jsonfile:
        json.dump({argv[1]: [{"task": todo.get('title'),
                              "completed": todo.get('completed'),
                              "username": username}
                             for todo in todos]}, jsonfile)
