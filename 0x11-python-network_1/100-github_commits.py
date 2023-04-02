#!/usr/bin/python3
"""
This module contains script that uses the github api to display 10 commits
from a github repository. The repo name and owner name are passed
as command line arguments"""


if __name__ == '__main__':
    """python script"""
    import requests
    import sys

    def get_commits():
        """
        Lists 10 commits from a github repository using the github
        API by : '<sha>: <author name>'
        """
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = f'https://api.github.com/repos/{owner}/{repo}/commits?\
        per_page=10'
        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()
            for item in data:
                sha = f"{item.get('sha')}: "
                name = item.get('commit').get('author').get('name')
                print(sha + name)
        except requests.exceptions.HTTPError as err:
            pass
    get_commits()
