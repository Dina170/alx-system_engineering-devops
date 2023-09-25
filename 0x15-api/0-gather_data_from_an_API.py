#!/usr/bin/python3
import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com/"
emp_name = requests.get(url + "users/{}".format(argv[1])).json().get('name')
todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

completed = []
for todo in todos:
    if todo.get('completed'):
        completed.append(todo.get('title'))

print("Employee {} is done with tasks({}/{}):".format(
    emp_name, len(completed), len(todos)))
for todo in completed:
    print("\t {}".format(todo))
