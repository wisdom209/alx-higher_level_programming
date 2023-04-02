#!/usr/bin/python3
""" This module contains """


if __name__ == '__main__':
    """Lists 10 commits from a github"""
    import requests
    import sys
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?\
    per_page=10'
    res = requests.get(url)
    # res.raise_for_status()
    data = res.json()
    for item in data:
        sha = item.get('sha')
        name = item.get('commit').get('author').get('name')
        print(sha + ": " + name)
