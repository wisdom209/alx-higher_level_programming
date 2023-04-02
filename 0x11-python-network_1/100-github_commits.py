#!/usr/bin/python3
"""Get the 10 latest commits"""
import requests
import sys


if __name__ == "__main__":
    """Get the latest 10 commits"""
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?\
            author={owner}&sort=author-date&direction=desc&per_page=10"
    response = requests.get(url)
    json = response.json()
    num = 0
    for i in json:
        sha = i.get('sha')
        author = i.get("commit").get("author").get("name")
        if (sha is not None):
            print(f"{sha}: {author}")
        num += 1
        if (num == 10):
            break
