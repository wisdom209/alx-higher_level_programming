#!/usr/bin/python3
"""display header with requests"""
import requests
import sys
if __name__ == '__main__':
    """display a header"""
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
