#!/usr/bin/python3
<<<<<<< HEAD
"""Contains top_ten function"""
=======
"""Function to print hot posts on a given Reddit subreddit."""
>>>>>>> 0b84059b007b57f69ef262fb7efdaf900dfb7386
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
<<<<<<< HEAD
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
=======
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
>>>>>>> 0b84059b007b57f69ef262fb7efdaf900dfb7386
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
