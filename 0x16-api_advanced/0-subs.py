#!/usr/bin/python3
"""return number of subscribers for subreddit"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """find number of subscribers"""
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = 'https://www.reddit.com/api/search_reddit_names.json'
    valid = requests.get(url, headers=headers, params={'query': subreddit})\
                    .json()
    if subreddit in valid['names']:
        url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
        sub = requests.get(url,
                           headers=headers, allow_redirects=False)
        if (sub.status_code != 200):
            return 0
        sub = sub.json()
        return (sub['data']['subscribers'])
    return 0
