#!/usr/bin/python3
"""print titles of hot top ten"""
import json
import requests
import sys


def top_ten(subreddit):
    """print hot top ten"""
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    url = 'https://www.reddit.com/api/search_reddit_names.json'
    valid = requests.get(url, headers=headers, params={'query': subreddit})\
                    .json()
    if subreddit in valid['names']:
        top = requests.get('https://www.reddit.com/r/' + subreddit + '.json',
                           headers=headers).json()
        cnt = 0
        for dicti in top['data']['children']:
            if cnt < 10:
                print(dicti['data']['title'])
            cnt += 1
    else:
        print(None)
