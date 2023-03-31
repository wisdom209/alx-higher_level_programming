#!/usr/bin/python3
"""Get response based on error code"""
import requests
import sys

if __name__ == '__main__':
    """Get error based on status code"""
    url = sys.argv[1]
    response = requests.get(url)
    status = eval(f"response.status_code")
    if status >= 400:
        print("Error code:", status)
    else:
        print(response.text)
