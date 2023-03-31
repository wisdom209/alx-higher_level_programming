#!/usr/bin/python3
"""module to implement GET with urllib"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
request = urllib.request.Request
if __name__ == '__main__':
    """run the code"""
    with urllib.request.urlopen(request(url)) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
