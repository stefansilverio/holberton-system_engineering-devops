#!/usr/bin/python3
"""return number of subscribers for subreddit"""
import json
import sys
import requests


def number_of_subscribers(subreddit):
    """find number of subscribers"""
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'

    sub = requests.get(url,
                       headers=headers, allow_redirects=False)

    if (sub.status_code != 200):
        return 0

    sub = sub.json()

    if 'subscribers' in sub['data']:
            return (sub['data']['subscribers'])
