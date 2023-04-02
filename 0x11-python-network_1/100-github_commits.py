#!/usr/bin/python3
"""
This module contains script that uses the github api to display 10 commits
from a github repository. The repo name and owner name are passed
as command line arguments
"""
import requests
from sys import argv


def get_commits():
    """
    Lists 10 commits from a github repository using the github
    API by : '<sha>: <author name>'
    """
    _, repo, owner = argv
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?per_page=10'
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        for item in data:
            sha = f"{item.get('sha')}: "
            name = f"{item.get('commit').get('author').get('name')}"
            print(sha + name)
    except requests.exceptions.HTTPError as err:
        continue


if __name__ == '__main__':
    get_commits()

"""
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
"""
