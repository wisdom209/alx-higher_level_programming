#!/usr/bin/python3
"""handle errors in http requests"""
import urllib.request
from urllib.error import HTTPError
import sys
url = sys.argv[1]
request = urllib.request.Request
if __name__ == '__main__':
    """handle the errors"""
    try:
        with urllib.request.urlopen(request(url)) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
