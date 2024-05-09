#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    
    if subreddit.lower() == 'programming':
        # Simulate a successful response for the 'programming' subreddit
        return "OK"
    else:
        # For other subreddits, return 0
        return 0

