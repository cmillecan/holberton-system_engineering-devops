#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], next_page=None):
    """Returns list of titles"""
    r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                     format(subreddit, next_page),
                     headers={'User-Agent': 'custom'},
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    if next_page is None:
        return hot_list
    for thread in r.json().get('data').get('children'):
        hot_list += [thread.get('data').get('title')]
    next_page = r.json().get('data').get('next_page')
    recurse(subreddit, hot_list, next_page)
    return hot_list
