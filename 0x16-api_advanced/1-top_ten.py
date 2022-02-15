#!/usr/bin/python3
"""Module that queries and prints the titles
    of the first 10 hot posts listed of a subreddit.
"""

import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles
        of the first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']['children']
        for posts in data[:10]:
            print(posts['data']['title'])
    else:
        print(None)
