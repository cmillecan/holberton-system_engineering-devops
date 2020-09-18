#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
"""
def number_of_subscribers(subreddit):
    """Returns number of subscribers"""
    r = get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers={'User-agent': 'custom'}, allow_redirects=False)
    if r.status_code != 200:
        return 0
    return r.json().get('data').get('subscribers')
