#!/usr/bin/python3
"""defines a function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    headers = {"User-agent": "MyApp/1.0"}
    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    return res.json().get("data").get("subscribers")
