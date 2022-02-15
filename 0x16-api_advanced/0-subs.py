#!/usr/bin/python3
"""Module to that queries and returns
    the number of subscribers of a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns
    the number of subscribers for a given subreddit"""
    reddit_url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(reddit_url, headers=headers)

    if response.status_code == 200:
        suscribers = response.json()['data']['subscribers']
        return suscribers
    return 0
