#!/usr/bin/python3
"""defines a function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """prints the titles of the first 10 hot posts listed for a given subreddit
    using pagination"""
    if hot_list is None:
        hot_list = []
    headers = {'User-Agent': 'MyApp/1.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']
        if not articles:
            return None
        for article in articles:
            hot_list.append(article['data']['title'])

        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
