#!/usr/bin/python3
"""return number of subscribers for subreddit"""
import requests
import json
import sys


def number_of_subscribers(subreddit):
    """find number of subscribers"""
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    url = 'https://www.reddit.com/api/search_reddit_names.json'
    valid = requests.get(url, headers=headers, params={'query': subreddit})\
                    .json()
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'

    if subreddit in valid['names']:
        sub = requests.get(url,
                           headers=headers).json()
        return (sub['data']['subscribers'])
    else:
        return (0)
