#!/usr/bin/python3
"""Make a post request"""
import sys
import urllib.request


if __name__ == '__main__':
    """Makes a post request"""
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('ascii')
    request = urllib.request.Request
    with urllib.request.urlopen(request(url, data)) as response:
        print(response.read().decode('utf-8'))
