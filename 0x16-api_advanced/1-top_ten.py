#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of top 10 posts"""
    r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                     format(subreddit), headers={'User-Agent': 'custom'},
                     allow_redirects=False)
    if r.status_code == 200:
        for key in r.json().get('data').get('children'):
            print(key.get('data').get('title'))
    else:
        print(None)
