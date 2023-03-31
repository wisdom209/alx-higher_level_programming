#!/usr/bin/python3
"""prints the X-Request-Id" header"""
import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    """gets the header"""
    url = sys.argv[1]
    request = urllib.request.Request
    with urllib.request.urlopen(request(url)) as response:
        print(response.info().get('X-Request-Id'))
