#!/usr/bin/python3
"""return number of subscribers for subreddit"""
import requests
import json
import sys


def number_of_subscribers(subreddit):
    """find number of subscribers"""
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    cnt = requests.get(url, headers=headers)
    try:
        (cnt.json()['data']['subscribers'])
    except KeyError:
        return (0)
    return (cnt.json()['data']['subscribers'])
