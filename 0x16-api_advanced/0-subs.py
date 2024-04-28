#!/usr/bin/python3
<<<<<<< HEAD
"""
Contains the number_of_subscribers function
"""

=======
"""Function to query subscribers on a given Reddit subreddit."""
>>>>>>> 0b84059b007b57f69ef262fb7efdaf900dfb7386
import requests


def number_of_subscribers(subreddit):
<<<<<<< HEAD
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
=======
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
>>>>>>> 0b84059b007b57f69ef262fb7efdaf900dfb7386
