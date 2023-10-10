#!/usr/bin/python3
"""defines a function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """prints the titles of first 10 hot posts listed for given subreddit"""
    headers = {"User-agent": "MyApp/1.0"}
    res = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit), headers=headers)
    if res.status_code != 200:
        print('None')
        return 0
    for t in res.json().get('data').get('children'):
        print(t.get('data').get('title'))
