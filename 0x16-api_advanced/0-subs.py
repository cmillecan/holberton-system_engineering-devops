#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers"""
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit), headers={'User-Agent': 'custom'},
                     allow_redirects=False)
    if r.status_code != 200:
        return 0
    else:
        return r.json().get('data').get('subscribers')
