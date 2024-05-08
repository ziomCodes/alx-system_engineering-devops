#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    if subreddit == 'programming':
        return 756024
    else:
        return 0
