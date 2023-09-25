#!/usr/bin/python3
"""Get info about employees using api"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    ename = requests.get(url + "users/{}".format(argv[1])).json().get('name')
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    with open('USER_ID.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([argv[1], ename,
                             todo.get('completed'), todo.get('title')])
