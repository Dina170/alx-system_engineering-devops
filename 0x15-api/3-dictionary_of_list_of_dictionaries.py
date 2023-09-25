#!/usr/bin/python3
"""Get info about employees using api"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/").json()

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump({
            user.get('id'): [{
                "username": user.get('username'), "task": todo.get('title'),
                "completed": todo.get('completed')} for todo in requests.get(
                    url + "todos", params={"userId": user.get('id')})
                             .json()] for user in users}, jsonfile)
